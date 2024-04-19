#its name when dowloaded
$name_1 = 'cv_pruebas.pdf'

#its wished name
$name_2 = Read-Host "Ingrese el nuevo nombre del archivo"

#where it comes from:
$path_1 = 'C:\Users\sgast\OneDrive\Documentos\Downloads'

#where it goes to
$path_2 = 'C:\Users\sgast\Documents\important_cv'

move-item -path $path_1\$name_1 -destination $path_2

rename-item -path $path_2\$name_1 -newname $path_2\$name_2

start 'C:\Users\sgast\Documents\important_cv' 

start 'https://pdfjoiner.com/'