param([string]$Destination = (Join-Path $PWD "Academy-Riverside-Reading-Day"))
$ErrorActionPreference = "Stop"
if (Test-Path -LiteralPath $Destination) { throw "Destination already exists; choose a NEW practice folder. No files changed." }
$root = New-Item -ItemType Directory -Path $Destination
foreach ($name in @("01 Pending Review","02 Approved","03 Rejected","04 Changes Requested","05 Simulated Action Log")) { New-Item -ItemType Directory -Path (Join-Path $root.FullName $name) | Out-Null }
@"
FICTIONAL TRAINING RECORD — NOT PUBLISHED
A-002 Riverside Reading Day v1
Rejected—start time missing.
Proposed date: 24 October 2026 (organizer-supplied, not independently verified).
No external action. Keep this reason with the rejected record.
"@ | Set-Content -LiteralPath (Join-Path $root.FullName "03 Rejected/A-002_Riverside-Reading-Day_v1.txt") -Encoding UTF8
@"
SIMULATED ACTION ONLY — NO REAL PUBLICATION
A-001 approved v1. Reviewed and current destination: Public events page.
Reviewed/current version match. Fixture demonstrates routing only.
Start time remains missing; this is not factual permission to publish.
"@ | Set-Content -LiteralPath (Join-Path $root.FullName "05 Simulated Action Log/A-001_approved_v1.txt") -Encoding UTF8
@"
record_id,reviewer_role,decision_time,decision,reason,reviewed_version,reviewed_destination,supporting_information_reference
A-001,Event communications reviewer,2026-10-20T09:00:00Z,Approved,Routing simulation only,v1,Public events page,organizer-form-v1
A-002,Event communications reviewer,2026-10-20T09:00:00Z,Rejected,Start time is missing,v1,Public events page,organizer-form-v1
"@ | Set-Content -LiteralPath (Join-Path $root.FullName "decision-log.csv") -Encoding UTF8
Write-Output $root.FullName
