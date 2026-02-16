<#
.SYNOPSIS
    DOBer - Date of Birth list generator.

.DESCRIPTION
    Generates date-of-birth strings in statistically likely order, based on the
    assumption that user ages in a target application follow a roughly normal
    distribution around a given average age.

    Dates radiate outward from the average age, alternating older and younger,
    so the most statistically likely dates appear first.

.PARAMETER Format
    .NET date format string (default: dd-MM-yy).

.PARAMETER Output
    Output file path. If omitted, prints to stdout.

.PARAMETER Min
    Minimum age (default: 18).

.PARAMETER Max
    Maximum age (default: 65).

.PARAMETER Average
    Average age (default: 40).

.EXAMPLE
    .\dober.ps1 -Format "ddMMyy"

.EXAMPLE
    .\dober.ps1 -Min 21 -Max 26 -Average 23 -Format "MMM-dd-yyyy" -Output dobs.txt

.EXAMPLE
    .\dober.ps1 -Format "yyyyMMdd" | Select-Object -First 1000
#>

param(
    [string]$Format = "dd-MM-yy",
    [string]$Output,
    [int]$Min = 18,
    [int]$Max = 65,
    [int]$Average = 40
)

if ($Min -ge $Average -or $Average -ge $Max) {
    Write-Error "Must satisfy: Min < Average < Max"
    exit 1
}

$today = Get-Date
$base = $today.AddDays(-$Average * 365)

$olderDays = ($Max - $Average) * 365
$youngerDays = ($Average - $Min) * 365

# Indices for alternating between older and younger
$olderIdx = 1
$youngerIdx = 0

$lines = [System.Collections.Generic.List[string]]::new()

while ($olderIdx -lt $olderDays -or $youngerIdx -lt $youngerDays) {
    # Older date
    if ($olderIdx -lt $olderDays) {
        $lines.Add($base.AddDays(-$olderIdx).ToString($Format))
        $olderIdx++
    }
    # Younger date
    if ($youngerIdx -lt $youngerDays) {
        $lines.Add($base.AddDays($youngerIdx).ToString($Format))
        $youngerIdx++
    }
}

if ($Output) {
    $lines | Set-Content -Path $Output -Encoding UTF8
    Write-Host "Written to $Output" -ForegroundColor Green
} else {
    $lines | ForEach-Object { Write-Output $_ }
}
