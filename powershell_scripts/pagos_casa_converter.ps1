#In order to open it via egde (faster than photos) the namefiles has to be joint with "_"

#All whatsapp downloads files

$download_path = "C:\Users\sgast\Downloads\"

#every png file name is replaced with no spaces
Get-ChildItem $download_path | ForEach-Object { 
	Rename-Item $_.Fullname -newname ($_.Name -replace ' ', '_') 
}

#the month we are currently paying
$path = "C:\Users\sgast\Documents_personal\excel\casa_accounting\" + (Read-Host "give the name of the month youre paying") + "\"

if (-not (test-path -Path $path)){
	mkdir $path
}

#moving each wsp png file to the desired carpet 
Get-ChildItem $download_path -Filter 'Wha*'| ForEach-Object {Move-Item $_.FullName -Destination $path}

#it opens each file and then asks for its coresponding name with png already
Get-ChildItem $path -Filter 'Wha*' | ForEach-Object {
	Start-Process -FilePath "msedge.exe" -ArgumentList $_.FullName; 
	Rename-Item $_.FullName -NewName ((Read-Host "Name of the payment") + ".png")
}




