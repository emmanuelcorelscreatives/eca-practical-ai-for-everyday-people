from pathlib import Path
import csv,zipfile
p=Path(__file__).parent
with (p/"source-log-completed.csv").open(newline="") as f: rows=list(csv.DictReader(f))
assert len(rows)==3 and [r["Source ID"] for r in rows]==["S01","S02","S03"]
for row in rows: assert (p/"GardenOpenDay/01_Originals"/row["Original filename"]).is_file()
for f in [p/"GardenOpenDay/01_Originals/Volunteer_Planning_Notes_2026-10-02.docx",p/"GardenOpenDay/02_Working_Notes/Source_Log.xlsx"]:
 with zipfile.ZipFile(f) as z: assert z.testzip() is None
print("PASS: three exact source rows/files and DOCX/XLSX CRC. No cloud import or learner comprehension claimed.")
