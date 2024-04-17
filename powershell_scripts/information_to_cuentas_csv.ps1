<#
    Excel takes a while to start on my computer, i wanted to save time, so i created a ps1
    file to help me on the automatization process:
    It's a form which files the information into a certain csv, where my accounting information is saved
#>

<# 
    Getting the day, only the day is necessary because i do this daily, so its literally impossible to fill
    this form from month to month 
#>
$day = Read-Host 'Fecha (solo el dia)'

#   Getting the date
$date = Get-Date -Format "dd-MM-yyyy"

#   Formatting the date
$date = $date -replace "^..", $day

#   Register the amount spent
$monto = READ-host 'Registre el monto ingresado'

#   What kind of spending the amount was?
$wordList = @("CELULAR", "CASA", "MENU", "PASAJE", "BLIND", "INGRESO","VARIOS", "COM_VAR","PERSONAL","RECIBO")

#   Selecting the kind of spending the amount was
$selectedWord = Read-Host "Seleccione la categoria correspondiente: $($wordList -join ', ')"

#   Validating the input
while ($selectedWord -notin $wordList) {
    Write-Host "Invalid input. Please select a word from the list."
    $selectedWord = Read-Host "Seleccione la categoria correspondiente: $($wordList -join ', ')"
}

#   The description of the amount spent, so everything is properly tracked
$descripcion = READ-HOST 'Poner breve descripcion'

#   The row to be append on the csv file
$value = "$date,$monto,$descripcion,$selectedWord"

#   The path of the csv file
$paths = 'C:\Users\sgast\Documents_personal\excel\cuentas.csv'

#   Appending the row to the csv file
add-content -path $paths -value "`n$value"







