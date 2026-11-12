param([Parameter(Mandatory=$true)][string]$Destination)
$ErrorActionPreference='Stop'
if(-not [IO.Path]::IsPathRooted($Destination)){throw 'Use a new absolute destination'}
if(Test-Path -LiteralPath $Destination){throw 'Destination already exists; refusing overwrite'}
New-Item -ItemType Directory -Path $Destination | Out-Null
foreach($name in @('Awaiting Review','Approved Snapshot','Rejected','Needs Recheck')){New-Item -ItemType Directory -Path (Join-Path $Destination $name) | Out-Null}
$v2=Join-Path (Join-Path $Destination 'Needs Recheck') 'EVT-014-v2';New-Item -ItemType Directory -Path $v2 | Out-Null
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'action-package-v2.pdf') -Destination (Join-Path $v2 'action-package.pdf')
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'supporting-brief.pdf') -Destination $v2
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'review-status.txt') -Destination $v2
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'event-map-v1.pdf') -Destination $v2
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'action-package-v2.json') -Destination (Join-Path $v2 'action-package.json')
$cases=Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot 'packages.json') | ConvertFrom-Json
$cases[0].approved | ConvertTo-Json -Depth 10 | Set-Content -Encoding UTF8 -LiteralPath (Join-Path (Join-Path $Destination 'Approved Snapshot') 'EVT-014-v1.json')
'Created new fictional Academy queue. External action disabled.'
