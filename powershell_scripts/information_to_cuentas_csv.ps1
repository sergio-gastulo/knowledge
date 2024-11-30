<#
    Excel takes a while to start on my computer, i wanted to save time, so i created a ps1
    file to help me on the automatization process:
    It's a form which files the information into a certain csv, where my accounting information is saved
#>

<# 
    Getting the day, only the day is necessary because i do this daily, so its literally impossible to fill
    this form from month to month 
#>


#   Getting the date
Write-Host " "
$day = Read-Host 'Fecha (solo el dia)'
$month = (Get-Date).Month.ToString("00")
$year = (Get-Date).Year
$date = "$day-$month-$year"

#   Register the amount spent
Write-Host " "
$monto = READ-host 'Registre el monto ingresado'

#category list
$wordList = @("BLIND", "CASA", "CELULAR", "COM_VAR", "INGRESO", "MENU", "PASAJE", "PERSONAL", "RECIBO", "USD_INC", "VARIOS")

Write-Host " "
"*"*100
Write-Host " "
#   Displaying the categories with numbers
Write-Host "Seleccione la categoria correspondiente:"
for ($i = 0; $i -lt $wordList.Length; $i++) {
    Write-Host "$($i + 1) -> $($wordList[$i])"
}
Write-Host " "
"*"*100
Write-Host " "

#   Selecting the kind of spending the amount was
$selectedNumber = Read-Host "Type category number"

#   Validating the input
while (-not ($selectedNumber -match '^\d+$') -or [int]$selectedNumber -le 0 -or [int]$selectedNumber -gt $wordList.Length) {
    $selectedNumber = Read-Host "Type valid category number"
}

#   Getting the selected word
$selectedWord = $wordList[[int]$selectedNumber - 1].Trim()

# Solicitar una breve descripción al usuario
Write-Host " "
$descripcion = Read-Host "type descripcion -- no commas no ENHE "
Write-Host " "


#   The path of the csv file
$paths = 'C:\Users\sgast\documents_personal\excel\cuentas.csv'

if (([int]$monto -gt 200) -and (($selectedWord -ne "INGRESO") -and ($selectedWord -ne "USD_INC"))) {
    
    <# Action to perform if the condition is true #>
    $numMonths = Read-Host "How many months do you want to your value into your csv"
    
    $newMonto = ([int]$monto)/([int]$numMonths)
    
    for ($i = 0; $i -lt $numMonths; $i++) {
        
        $newMonth = ([int]$Month+$i).ToString("00")
        $newDate = "$day-$newMonth-$year"        
        $newDesc = "$descripcion tag: cuota $i"
        #   The row to be append on the csv file
        $value = "$newDate,$newMonto,$newDesc,$selectedWord"
        

        add-content -path $paths -value "$value"
    }
} else {
    <# Action when all if and elseif conditions are false #>
    
    $value = "$date,$monto,$descripcion,$selectedWord"

    <# 
    Just appending the row to the csv file, withouth anything changed 
    #>
    add-content -path $paths -value "$value"
}