
#Moving to the path of the python.exe file
$script_path = 'C:\Program Files\Python312'
cd $script_path

#Upgrading pip
python -m pip install --upgrade pip

#Reading the library to be installed
$library = Read-Host 'Lib to install'

#installing such library
pip install $library

#returning to python environment
$vscode_path = "C:\Users\sgast\python_files"
cd $vscode_path

#openning vscode
code .


