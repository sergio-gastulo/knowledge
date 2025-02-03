$OutputEncoding = [System.Text.Encoding]::UTF8
Write-Host ('ññ' -notmatch '[ñ,]') # This should return False
Write-Host (',,' -notmatch '[ñ,]') # This should return False
Write-Host (',ñ' -notmatch '[ñ,]') # This should return False
$val = Read-Host "Type ññ"

if ($val -notmatch '[ñ,]') {
    # This shouldn't even be evaluated
    Write-Host "$val is not interpreted as enhe"
}