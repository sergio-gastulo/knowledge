<#
    This is a code i developed for a quick spyder activation
    It was really tedious to press windows+anaconda prompt+conda activate env+spyder
    I looked for the anaconda prompt executable on my files 
    Then I learned how to activate it from powershell
    And the automatization came by itself 
#>

#The file where the anaconda prompt was
start 'C:\Users\sgast\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Prompt.lnk'

#Object to work with the keyboards directly
$wshell = New-Object -ComObject wscript.shell

#writing the command conda activate <env>
$wshell.SendKeys('conda activate secondo{ENTER}')

#activating spyder on <env>
$wshell.SendKeys('spyder{ENTER}')




