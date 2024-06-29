#In order to open it via egde (faster than photos) the namefiles has to be joint with "_"

#All whatsapp downloads files

$download_path = "C:\Users\sgast\Downloads\"

#every png file name is replaced with no spaces
ls $download_path | % { rni $_.Fullname -newname ($_.Name -replace ' ', '_') }

#the month we are currently paying
$path = "C:\Users\sgast\Documents_personal\excel\casa_accounting\" + (Read-Host "give the name of the month youre paying") + "\"

if (-not (test-path -Path $path)){
	mkdir $path
}

#moving each wsp png file to the desired carpet 
ls $download_path -Filter 'Wha*'| % {mv $_.FullName -Destination $path}

#it opens each file and then asks for its coresponding name with png already
ls $path -Filter 'Wha*' | % {
	saps -FilePath "msedge.exe" -ArgumentList $_.FullName; 
	rni $_.FullName -NewName ((Read-Host "Name of the payment") + ".png")
}




