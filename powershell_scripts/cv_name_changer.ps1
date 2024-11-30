#its name when dowloaded
$name_1 = 'cv_pruebas.pdf'

#its wished name
$name_2 = Read-Host "Ingrese el nuevo nombre del archivo"

#where it comes from:
$path_1 = 'C:\Users\sgast\downloads'

#where it goes to
$path_2 = 'C:\Users\sgast\documents_personal\important_cv\cvs_made'

move-item -path $path_1\$name_1 -destination $path_2

rename-item -path $path_2\$name_1 -newname $path_2\$name_2

# Start-Process 'C:\Users\sgast\Documents\important_cv' 

# Start-Process 'https://pdfjoiner.com/'

scb $path_2\$name_2