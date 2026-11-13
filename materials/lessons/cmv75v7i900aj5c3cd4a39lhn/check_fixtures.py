"""Check exact fixture integrity and mask/pair consistency, not image quality or listening."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent


def text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def elements(name):
    root = ET.fromstring(text(name))
    return {element.attrib["id"]: ET.tostring(element)
            for element in root.iter() if "id" in element.attrib}


original = elements("garden-original.svg")
flawed = elements("garden-flawed.svg")
corrected = elements("garden-corrected.svg")
for diagram in (original, flawed, corrected):
    assert sum(key.startswith("person-") for key in diagram) == 6
    assert sum(key.startswith("table-") for key in diagram) == 4
assert "ramp" in original and "ramp" not in flawed and "ramp" in corrected
assert "bin" in original and "bin" not in flawed and "bin" not in corrected
assert "Accessible entrance" in text("garden-original.svg")
assert "Access entrance" in text("garden-flawed.svg")
assert "Accessible entrance" in text("garden-corrected.svg")
assert {key: value for key, value in original.items() if key != "bin"} == corrected
for key in original:
    if key not in {"bin", "ramp", "sign"}:
        assert original[key] == flawed[key]
assert "solo si" in text("notice-es.txt")
assert "only if accompanied by an adult" in text("translation-reference.txt")
assert "and can be accompanied" in text("translation-flawed.txt")
assert "Bring fifteen folding chairs to the east gate" in text("audio-script.txt")
assert "We should not lock the east gate" in text("transcript-reference.txt")
assert "Sameer: Bring fifty folding chairs to the west gate" in text("transcript-flawed.txt")

# Actual supplied binary integrity and decoded-pixel preservation checks.
import array
import hashlib
import json
import struct
import wave
import zlib


def decode_png(name):
    raw = (ROOT / name).read_bytes()
    assert raw.startswith(b"\x89PNG\r\n\x1a\n"), name
    offset = 8
    compressed = bytearray()
    width = height = channels = None
    while offset < len(raw):
        length = struct.unpack(">I", raw[offset:offset + 4])[0]
        assert offset + 12 <= len(raw), "Truncated PNG chunk"
        assert offset + 12 + length <= len(raw), "PNG chunk length exceeds file"
        kind = raw[offset + 4:offset + 8]
        payload = raw[offset + 8:offset + 8 + length]
        crc = struct.unpack(">I", raw[offset + 8 + length:offset + 12 + length])[0]
        assert zlib.crc32(kind + payload) & 0xffffffff == crc, (name, kind)
        if kind == b"IHDR":
            width, height, depth, color, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
            assert depth == 8 and color in (2, 6) and compression == filtering == interlace == 0
            channels = 3 if color == 2 else 4
        elif kind == b"IDAT":
            compressed.extend(payload)
        offset += length + 12
        if kind == b"IEND":
            break
    assert kind == b"IEND" and length == 0 and offset == len(raw), "Missing IEND or trailing bytes"
    assert width == 1536 and height == 1024
    inflated = zlib.decompress(compressed)
    stride = width * channels
    assert len(inflated) == (stride + 1) * height
    previous = bytearray(stride)
    rgba = bytearray()
    for y in range(height):
        start = y * (stride + 1)
        filter_kind = inflated[start]
        row = bytearray(inflated[start + 1:start + 1 + stride])
        assert filter_kind in range(5)
        for index in range(stride):
            left = row[index - channels] if index >= channels else 0
            above = previous[index]
            diagonal = previous[index - channels] if index >= channels else 0
            if filter_kind == 1:
                prediction = left
            elif filter_kind == 2:
                prediction = above
            elif filter_kind == 3:
                prediction = (left + above) // 2
            elif filter_kind == 4:
                estimate = left + above - diagonal
                distances = [abs(estimate - value) for value in (left, above, diagonal)]
                prediction = (left, above, diagonal)[distances.index(min(distances))]
            else:
                prediction = 0
            row[index] = (row[index] + prediction) & 255
        if channels == 4:
            rgba.extend(row)
        else:
            for index in range(0, stride, 3):
                rgba.extend(row[index:index + 3])
                rgba.append(255)
        previous = row
    return width, height, rgba


def inside_or_edge(x, y, polygon, radius=1.5):
    inside = False
    for first, second in zip(polygon, polygon[1:] + polygon[:1]):
        ax, ay = first
        bx, by = second
        dx, dy = bx - ax, by - ay
        length_squared = dx * dx + dy * dy
        assert length_squared > 0, "Degenerate polygon edge"
        fraction = max(0, min(1, ((x - ax) * dx + (y - ay) * dy) / length_squared))
        if (x - ax - fraction * dx) ** 2 + (y - ay - fraction * dy) ** 2 <= radius * radius:
            return True  # Explicit selection/edge tolerance, never inferred from changed pixels.
        if (ay > y) != (by > y) and x < (bx - ax) * (y - ay) / (by - ay) + ax:
            inside = not inside
    return inside


def inside_polygon(x, y, polygon):
    # Exact strict ray-crossing definition used by the original editor-core.
    # Boundary inclusion is intentionally not added to historical measurements.
    inside = False
    for first, second in zip(polygon, polygon[1:] + polygon[:1]):
        ax, ay = first
        bx, by = second
        if (ay > y) != (by > y) and x < (bx - ax) * (y - ay) / (by - ay) + ax:
            inside = not inside
    return inside


def polygon(value):
    assert isinstance(value, list) and len(value) >= 3, "Actual polygon required"
    assert all(isinstance(p, list) and len(p) == 2 and all(type(v) in (int, float) for v in p)
               and 0 <= p[0] < 1536 and 0 <= p[1] < 1024 for p in value), "Polygon bounds"
    assert len({tuple(p) for p in value}) == len(value), "Duplicate polygon vertex"
    return value


def validate_pair(width, height, source_pixels, corrected_pixels, flawed_pixels, editor):
    assert (editor["width"], editor["height"]) == (width, height)
    OLD_BIN_MASK = [[1250, 605], [1267, 580], [1294, 566], [1315, 543], [1345, 550], [1374, 536], [1400, 557], [1395, 581], [1438, 585], [1465, 609], [1462, 660], [1455, 777], [1454, 859], [1437, 886], [1478, 902], [1460, 916], [1290, 914], [1269, 883], [1275, 858], [1266, 701], [1253, 644]]
    assert editor["oldBinMask"] == OLD_BIN_MASK, "Historical underinclusive bin mask must remain explicit"
    SELECTION = [[1240, 605], [1258, 572], [1288, 557], [1308, 535], [1342, 540], [1374, 524], [1410, 549], [1404, 572], [1448, 579], [1477, 607], [1474, 660], [1467, 777], [1466, 862], [1449, 889], [1490, 902], [1470, 928], [1280, 926], [1258, 890], [1263, 858], [1254, 701], [1241, 644]]
    assert editor["selectionPolygon"] == SELECTION, "Exact actual GIMP selection required"
    assert editor["selectionFeatherRadius"] == 3, "Actual GIMP feather radius is 3px; no broader change allowance"
    rampsign = [polygon(editor["rampMask"]), polygon(editor["signMask"])]
    protected = editor["protectedMasks"]
    assert protected == [[[1430, 565], [1464, 565], [1464, 591], [1430, 591]]], "Exact actual hard-protected table-leg submask required"
    protected_polygons = [polygon(p) for p in protected]
    assert editor["savedCorrectionReopenedExact"] is True and editor["savedFlawedReopenedExact"] is True
    assert isinstance(editor["operations"], list) and editor["operations"], "Actual operations missing"
    assert isinstance(editor["executionEvidence"], dict) and editor["executionEvidence"].get("path") and len(editor["executionEvidence"].get("sha256", "")) == 64, "Actual retained execution reference required"
    changed = changed_flawed = changed_outside_old = 0
    for offset in range(0, len(source_pixels), 4):
        before = source_pixels[offset:offset + 4]
        fixed = corrected_pixels[offset:offset + 4]
        flawed = flawed_pixels[offset:offset + 4]
        if before == fixed == flawed:
            continue
        pixel = offset // 4
        x, y = pixel % width + 0.5, pixel // width + 0.5
        in_bin = inside_or_edge(x, y, SELECTION, radius=3)
        if before != fixed:
            assert in_bin, "Correction changes pixels outside bin"
            assert not any(inside_or_edge(x, y, p, radius=0) for p in protected_polygons), "Correction changes protected table/path pixels"
            changed += 1
            if not inside_polygon(x, y, OLD_BIN_MASK):
                changed_outside_old += 1
        if in_bin:
            assert fixed == flawed, "Bin correction must be identical in both derivatives"
        if fixed != flawed:
            assert not in_bin and (inside_or_edge(x, y, rampsign[0], radius=1) or inside_or_edge(x, y, rampsign[1], radius=0)), "Flawed derivative changes more than ramp/sign"
            assert not any(inside_or_edge(x, y, p, radius=0) for p in protected_polygons), "Flawed derivative changes protected table/path pixels"
            changed_flawed += 1
    assert changed > 0 and changed_flawed > 0
    assert editor["changedOutsideSelectionAndFeather"] == 0 and editor["changedInsideSelectionAndFeather"] == changed
    assert editor["changedOutsideOldMask"] == changed_outside_old, "Disclose changes outside historical mask"
    assert editor["changedFromCorrectedToFlawed"] == changed_flawed
    return changed, changed_flawed, changed_outside_old


provenance = json.loads(text("fixture-provenance.json"))
proof = json.loads(text("image-operation-proof.json"))
assert proof.get("state") == "ACTUAL_SAVED_REOPENED_CANDIDATE_PAIR_REQUIRES_INDEPENDENT_REVIEW", "Actual successor pair remains unbound"
assert provenance["imageDerivatives"].get("state") == proof["state"], "Derivative state mismatch"
assert provenance["imageDerivatives"]["operationProofSha256"] == hashlib.sha256((ROOT / "image-operation-proof.json").read_bytes()).hexdigest()
assert proof["files"] == provenance["files"], "Two file ledgers differ"
assert provenance["files"]["garden-original.png"]["sha256"] == "ae536777c5e16a6d68f25e9a1a200ef4bf3fe69aa0d4da33ee6fe2d8709c5c70"
assert provenance["files"]["garden-planning-recording.wav"]["sha256"] == "cce280e4c6a30571cda088e88362d18b8e88934c189aba2be57a75082cbef33f"
for name, binding in provenance["files"].items():
    data = (ROOT / name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == binding["sha256"], name
    assert len(data) == binding["bytes"], name
assert provenance["files"]["garden-corrected.png"]["sha256"] != "e8c0062ac14ca26111ecbb9b2a3b0948853ab63948235b562d5c0aa2d02dfca4", "Earlier rejected patch is not a repaired successor"
assert provenance["files"]["garden-illustrative-flawed.png"]["sha256"] != "dcbc42259a787b0a8c5065ff61575c31a2db103a87e6d2b5227a78aa5618fcc7", "Earlier rejected flawed pair retained"
pixels = {}
for name in ("garden-original.png", "garden-corrected.png", "garden-illustrative-flawed.png"):
    width, height, rgba = decode_png(name)
    assert proof["decodedRGBA"][name] == hashlib.sha256(rgba).hexdigest(), "Decoded RGBA binding changed: " + name
    pixels[name] = rgba
source_pixels, corrected_pixels, flawed_pixels = (pixels[n] for n in ("garden-original.png", "garden-corrected.png", "garden-illustrative-flawed.png"))
assert source_pixels != flawed_pixels and source_pixels != corrected_pixels
validate_pair(width, height, source_pixels, corrected_pixels, flawed_pixels, proof["editorProof"])
with wave.open(str(ROOT / "garden-planning-recording.wav"), "rb") as recording:
    assert recording.getframerate() == 22050 and recording.getnchannels() == 1
    assert recording.getsampwidth() == 2 and recording.getnframes() == 48 * 22050
    samples = array.array("h", recording.readframes(recording.getnframes()))
for start, end in [(0, 4), (10, 12), (18, 19), (42, 44)]:
    assert max(abs(value) for value in samples[start * 22050:end * 22050]) > 0
assert max(abs(value) for value in samples[5 * 22050:9 * 22050]) == 0
assert "00:42 [unclear]" in text("transcript-reference.txt")
assert provenance["audio"]["realHumanRecording"] is False
assert provenance["audio"]["independentHumanListeningApproval"] is False
print("PASS: exact file/RGBA hashes and PNG/WAV structure; actual selection+3px feather/protected masks and ramp-sign pair consistency. In-mask naturalness, raster feature counts, acoustic meaning, native execution and release approval are not certified.")
