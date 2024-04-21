# Prompt the user to enter the file name
$filename = Read-Host "Enter the file name"

$carpet = Read-Host "ps1 or bloc"

$ps1_path = $('C:\Users\sgast\Documents_personal\powershell_scripts\'+$filename+'.ps1')
$bloc_path = $('C:\Users\sgast\Documents_personal\bloc_notas\'+$filename+'.txt')

if ($carpet -eq 'ps1') {

	ni $ps1_path
	notepad $ps1_path

} elseif ($carpet -eq 'bloc') {

	# Create the file in the Bloc notas folder and open it in Notepad
	ni $bloc_path
	notepad $bloc_path

} else {

	Write-Host "Invalid input. Please enter 'ps1' or 'bloc'."

}
