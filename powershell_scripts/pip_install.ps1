<#
    Installing packages on python takes a while since "cd"ing to scripts at every step to install
    a library is really tedious.
    Thats why I created a ps1 file to automatize the labor
#>

#Moving to the path of the python.exe file
$script_path = 'C:\Program Files\Python312'
Set-Location $script_path

#Upgrading pip
python -m pip install --upgrade pip

#Reading the library to be installed
$library = Read-Host 'Lib to install'

#installing such library
pip install $library

#moving to my vscode path
$vscode = 'C:\Users\sgast\CODING'
Set-Location $vscode

