<#
.SYNOPSIS
    Finds knowledge-base gaps: high-volume support drivers with no KB article.

.DESCRIPTION
    Reads a case export (CSV) and reports drivers that generate volume but have
    no published KB article. These are the fastest self-service / deflection wins.

    Cost-saving lever: every deflected case is a case you never pay to handle.

.PARAMETER Path
    Path to the cases CSV. Defaults to the bundled sample data.

.EXAMPLE
    pwsh ./Get-KBGapReport.ps1
    pwsh ./Get-KBGapReport.ps1 -Path .\my-cases.csv
#>
param(
    [string]$Path = "$PSScriptRoot/../python/sample_data/cases.csv"
)

if (-not (Test-Path $Path)) {
    Write-Error "Case file not found: $Path"
    exit 1
}

$cases = Import-Csv -Path $Path

$report = $cases |
    Group-Object driver |
    ForEach-Object {
        $hasKb = ($_.Group | Where-Object { $_.has_kb_article -eq 'yes' }).Count -gt 0
        [pscustomobject]@{
            Driver   = $_.Name
            Cases    = $_.Count
            HasKB    = $hasKb
            KBGap    = -not $hasKb
        }
    } |
    Where-Object { $_.KBGap } |
    Sort-Object Cases -Descending

Write-Host ""
Write-Host "Knowledge-base gaps (high-volume drivers with no article):" -ForegroundColor Cyan
if ($report) {
    $report | Format-Table Driver, Cases -AutoSize
    $deflectable = ($report | Measure-Object Cases -Sum).Sum
    Write-Host "Potentially deflectable cases if these gaps are closed: $deflectable" -ForegroundColor Green
} else {
    Write-Host "No KB gaps found. Every driver has coverage." -ForegroundColor Green
}
Write-Host ""
