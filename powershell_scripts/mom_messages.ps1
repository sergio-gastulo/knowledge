
while ($True) {
    $cond4 = "El yape es a este numero al nombre de Betty Cespedes"
    $cond5 = "El plin es al 924182134 al nombre de Sergio Gastulo"
    "*"*100
    Write-Host "1 -> Recordar el precio del menu"
    Write-Host "2 -> Muchas gracias veci"
    Write-Host "3 -> Pagar pedido"
    Write-Host "4 -> El yape es a este numero al nombre de Betty Cespedes"
    Write-Host "5 -> El plin es al 924182134 al nombre de Sergio Gastulo"
    Write-Host "6 -> Mensaje para las cuentas"
    "*"*100
    " "
    $selection = Read-Host "Seleccione su mensaje:"
    switch ($selection) {
        1 { "Veci buenas, queremos recordarle que los sabados, domingos y feriados, el plato tiene un precio especial de 13 soles. Esperamos que lo tenga en cuenta para sus siguientes pedidos! (;" | Set-Clipboard }
        2 { "Muchas gracias veci" | Set-Clipboard }
        3 { 
            $int = read-host "--"; "Veci buenas no se olvide de yapear por favor, en total es " +$int+" soles" | Set-Clipboard
        }
        4 { $cond4 | Set-Clipboard }
        5 { $cond5 | Set-Clipboard }
        6 { 
            $int = read-host "--"; "Veci buenas noches le enviamos su cuenta hasta la fecha, en total es S/" +$int+".00 (: " | Set-Clipboard
        }
    }
}