while ($true) {
    try {
        $dayNumber = [int](Read-Host "`nWrite the day")
        Write-Host "`nParse successful." -ForegroundColor Green
        Write-Host $dayNumber
        if (($dayNumber -gt 31) -or ($dayNumber -lt 1)){
            Write-Host "`nHowever, it must be a positive integer < 31" -ForegroundColor Red
        } else {
            break
        }
    }
    catch {
        <#Do this if a terminating edayNumberception happens#>
        Write-Host "`nUps, something wrong happened while parsing. `nTry again`n" -ForegroundColor Red
    }
}