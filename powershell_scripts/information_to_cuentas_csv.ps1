#   Getting the date
do {
    $day = Read-Host "`nThe day of the Date Object"
    $isValid = [int]::TryParse($day, [ref]$null)
    if (-not $isValid) {
        Write-Host "`nInvalid input. The date must be a positive integer." -ForegroundColor Red
    } elseif ($day -gt 31 ) {
        Write-Host "`nToo big. Please parse the number properly." -ForegroundColor Red
    }
} while ((-not $isValid) -or ($day -gt 31))
Write-Host "`nValid! Please move onto the next step" -ForegroundColor Green
$day = "{0:D2}" -f $day
$period = (Get-Date -Format 'MM-yyyy')
$date = "$day-$period"

#   Register the amount spent
do {
    $monto = Read-Host "`nEnter the amount spent"
    $isValid = [double]::TryParse($monto, [ref]$null)
    if (-not $isValid) {
        Write-Host "Invalid input. The amount spent must be a positive real." -ForegroundColor Red
    }
} while (-not $isValid)
$monto = [double]$monto

Write-Host "`nValid! Please move onto the next step`n" -ForegroundColor Green

# Loading dictionary
$categoryDict = @{
    bl      =   'BLIND'
    cas     =   'CASA'
    cel     =   'CELULAR'
    cvar    =   'COM_VAR'
    ing     =   'INGRESO'
    men     =   'MENU'
    pas     =   'PASAJE'
    per     =   'PERSONAL'
    rec     =   'RECIBO'
    usd     =   'USD_INC'
    var     =   'var'
}

# Printing category list for reference
$categoryDict | ConvertTo-Json -Depth 2

do {
    $key = Read-Host "`nSelect a key from the dictionary above"
    if ($categoryDict.ContainsKey($key)) {
        $category = $categoryDict[$key]
        break
    } else {
        Write-Host "`nInvalid key, please try again." -ForegroundColor Red
    }
} while ($true)
Write-Host "`nValid! Please move onto the next step" -ForegroundColor Green

# Amount spent description
do {
    $description = Read-Host "`nType description. No commas, and no 'enhe'"
    if ($description -notmatch '[ñ,]') {
        # At this moment, we can't prevent ñ from being prompted here.
        # We trust on our user.
        break
    }
    Write-Host "`nDescription must not include 'enhe' or comma (,)" -ForegroundColor Red
} while ($true)
Write-Host "`nValid! Please move onto the next step" -ForegroundColor Green

#   The path of the csv file
$paths = 'C:\Users\sgast\documents_personal\excel\cuentas.csv'

# What happens if the amount spent is greater than 200
if (($monto -gt 200) -and (($category -ne "INGRESO") -and ($category -ne "USD_INC"))) {
    
    $numMonths  =   Read-Host "`nPlease add how many months you want to split your data."
    $newMonto   =   ($monto)/([int]$numMonths)
    $temp       =   [int](($date -split '-')[1])
    
    for ($i = 0; $i -lt $numMonths; $i++) {
        $newDay            =   "{0:D2}" -f ($temp + $i) 
        $newDate           =   [string]($date -replace '-\d{2}-', "-$newDay-")        
        $newDescription    =   "$description tag: cuota $i"
        
        #   The row to be append on the csv file
        $value = "$newDate,$newMonto,$newDescription,$category"
        add-content -path $paths -value "$value"
    }
} else {
    $value = "$date,$monto,$description,$category"
    add-content -path $paths -value "$value"
}