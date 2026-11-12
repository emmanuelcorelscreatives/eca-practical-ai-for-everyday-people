# Check What the Tool Actually Received

Emmanuel Corels Academy · Practical AI for Everyday People · Lesson 33

All event data are fictional and self-authored. No private files are required. The image-based notice is a digitally authored, skewed raster practice fixture; it is not evidence of a real notice or a real photographed event. Its text is deliberately excluded from PDF text extraction. This fixture tests the same source-readability issue discussed in the lecture without claiming a measured OCR response. No assistant replies are supplied as observed results.

## Before upload

Copy the four named practice files into a new folder. Keep this worksheet and all answer files outside that folder so the attachment selection remains exactly four files. Open the originals first: the PDF has four pages, the workbook has Overview, Schedule and Contacts, and the map labels are East Entrance, Main Hall and Registration. Page three is image-only; manually read its heading and time. Schedule is A1:D6, including its header row.

## Deliberate omission

Select only Inspection-Pack.pdf, Event-Workbook.xlsx and Attachment-Checklist.txt. Leave Entrance-Map.png unselected. Use an account and tool that supports these file types; interfaces and processing capabilities change. Do not assume a successful upload proves that a tool can read each file. Never upload private account documents.

Ask: “Report only what you can directly access: filenames, PDF pages, worksheet names, visible images, and anything unreadable or missing. Do not infer content.” Save the real response separately. Compare it with your folder, checklist and opened originals. Do not paste the answer key into the first prompt. Record uncertainty, unsupported files and absent evidence without converting them into a confident answer.

## Verify known markers

1. Confirm the four page thumbnails in the original PDF. Check page three directly for Setup Notice and 08:30.
2. Ask what the tool can read on page three, explicitly requesting uncertainty. A tool might read the time correctly or fail. Neither behavior is predetermined.
3. Open the workbook in Calc. Select Schedule; inspect A1:D6 and the other two sheet tabs. Ask the tool which range is populated, then compare the real answer with the original.
4. Compare the attachment list with the intended four files. Ask if Entrance-Map.png is directly accessible. If uncertain, investigate rather than asserting a fabricated answer.
5. Upload the missing map. Ask only for visible labels; compare the actual response with the opened PNG.
6. If page three remains unreadable, provide: “Source: Inspection-Pack.pdf, page 3. Verified heading: Setup Notice. Verified time: 08:30.” Label this as your manual observation, not successful OCR. Exporting a clearer page image is another possible fallback.
7. Begin the substantive task only after the required source inventory is reconciled. Still independently check important dates, numbers, names, meaning and permissions.

## Your evidence table

| Expected | Tool reported | Opened original | Repair / unresolved |
| --- | --- | --- | --- |
| Four files | Record actual reply | Compare names and attachment list | Add missing map |
| PDF pages 1–4 | Record actual coverage | Four thumbnails | Record readability separately |
| Setup Notice, 08:30 | Record actual reading and uncertainty | Open page 3 | Label manual excerpt if needed |
| Three named sheets | Record actual names | Open workbook tabs | Supply unsupported content separately |
| Schedule A1:D6 | Record actual range | Inspect filled cells | Explain mismatch without guessing |
| Three map labels | Record actual labels | Open PNG | Upload the separate image |

Expected, reported, opened and repaired are distinct evidence categories. A generated inventory cannot prove its own claims. “Attached” never means “fully available.”

## Reproducible fixture checks

Run `python3 verify_fixture.py` with Python 3. It uses only the standard library, validates all four file hashes against the included manifest and checks workbook sheet names, Schedule cell references, and the four PDF page objects. It verifies the supplied fixture structure, not an assistant's actual access, OCR quality or screenshot appearance. Use the opened originals for those checks. Expected result: `PASS: four-file fixture hashes and structural markers verified`. A change to any file is detected; retain the originals and record your changes in a separate copy.
