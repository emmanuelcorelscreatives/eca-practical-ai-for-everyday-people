"""Rebuild the three sample exports locally; never publish or mark human review done.

Requirements: Python 3, LibreOffice, Node.js plus `npm install sharp`, eSpeak NG,
and FFmpeg with libass/libx264. Run from this file's directory.
"""
from pathlib import Path
import json
import subprocess
import tempfile
import wave

ROOT = Path(__file__).resolve().parent

def run(args):
    subprocess.run(args, check=True, timeout=240)

def timestamp(seconds):
    n = round(seconds * 1000)
    return f"{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}"

def main():
    source = ROOT / '02_Working_Files'
    exports = ROOT / '03_Exports'
    exports.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='academy-kit-') as scratch:
        temporary = Path(scratch)
        profile = (temporary / 'office-profile').as_uri()
        run(['libreoffice', '-env:UserInstallation=' + profile, '--headless',
             '--convert-to', 'pdf', '--outdir', str(temporary),
             str(source / 'Event_Information_Sheet.odt')])
        (exports / 'Riverside_Reading_Circle_Info_v1.pdf').write_bytes(
            (temporary / 'Event_Information_Sheet.pdf').read_bytes())
        run(['node', '-e', "require('sharp')(process.argv[1]).png().toFile(process.argv[2])",
             str(source / 'Riverside_Reading_Circle_Visual_v1.svg'),
             str(exports / 'Riverside_Reading_Circle_Visual_v1.png')])
        lines = (source / 'Media_Script.txt').read_text(encoding='utf-8').splitlines()
        parts, captions, offset, expected_format = [], [], 0.0, None
        for index, line in enumerate(lines):
            if not line.strip():
                continue
            audio = temporary / f'sentence-{index}.wav'
            run(['espeak-ng', '-v', 'en', '-s', '140', '-w', str(audio), line])
            with wave.open(str(audio), 'rb') as reader:
                audio_format = (reader.getnchannels(), reader.getsampwidth(), reader.getframerate())
                if expected_format is not None and audio_format != expected_format:
                    raise RuntimeError('Sentence audio formats differ; no lossy join allowed')
                expected_format = audio_format
                duration = reader.getnframes() / reader.getframerate()
                parts.append(reader.readframes(reader.getnframes()))
                captions.append((offset, offset + duration, line))
                offset += duration
        if not expected_format:
            raise RuntimeError('The checked speech script is empty')
        with wave.open(str(source / 'Narration_v1.wav'), 'wb') as writer:
            writer.setnchannels(expected_format[0])
            writer.setsampwidth(expected_format[1])
            writer.setframerate(expected_format[2])
            writer.writeframes(b''.join(parts))
        (source / 'corrected.srt').write_text('\n'.join(
            f'{i+1}\n{timestamp(a)} --> {timestamp(b)}\n{text}\n'
            for i, (a, b, text) in enumerate(captions)), encoding='utf-8')
        # Use relative filenames in the filter to avoid platform drive/path escaping.
        video_filter = (
            'scale=900:900,pad=1080:1080:90:0:color=0x162e43,'
            "subtitles=02_Working_Files/corrected.srt:force_style='FontSize=17,MarginV=26,"
            "PrimaryColour=&HFFFFFF,OutlineColour=&H162E43,BorderStyle=1,Outline=2'"
        )
        subprocess.run([
            'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-loop', '1',
            '-i', '03_Exports/Riverside_Reading_Circle_Visual_v1.png',
            '-i', '02_Working_Files/Narration_v1.wav', '-vf', video_filter,
            '-r', '25', '-t', str(offset), '-c:v', 'libx264', '-threads', '2',
            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-movflags', '+faststart',
            '03_Exports/Riverside_Reading_Circle_Checked_v1.mp4',
        ], cwd=ROOT, check=True, timeout=240)
        run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i',
             str(exports / 'Riverside_Reading_Circle_Checked_v1.mp4'), '-f', 'null', '-'])
        print(json.dumps({'durationSeconds': offset, 'decodeExitCode': 0,
                          'humanListening': 'REQUIRED; not performed by this build',
                          'release': 'PRACTICE ONLY; NOT PUBLISHED'}))

if __name__ == '__main__':
    main()
