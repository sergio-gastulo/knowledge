function Edit-EnvironmentalVariable() {
    [alias("edit_env")]
        param()
	cmd /c "sysdm.cpl"
}

function Open-Zoom {
    [alias("zoom")]
    param()
    $zoom = "C:\Users\sgast\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom Workplace.lnk"
    Start-Process $zoom
}

function Open-Wolfram {
    [alias("wolfram")]
    param (
        [string]$v
    )
    $versionTuple = $v.Split(".")
    
    if (
        ($versionTuple[0] -lt 14) -or
        ($versionTuple[0] -eq 14 -and $versionTuple[1] -eq 0)
    ) {
        $path = (Join-Path -Path "C:\Program Files\Wolfram Research\Mathematica" -ChildPath "$v\Mathematica.exe")
    } else
    {
        $path = (Join-Path -Path "C:\Program Files\Wolfram Research\Wolfram" -ChildPath "$v\WolframNB.exe")
     }

    Write-Host "Starting: $path" 
    Start-Process $path
}

function Save-ClipboardImage {
    [alias("ss")]
    param(
        [string]$dir = (Get-Location).Path,
        [string]$setPathToClipboard = $true
    )

    $origLoc = (Get-Location).Path

    # Function to get image from clipboard
    function Get-ClipboardImage {
        Add-Type -AssemblyName System.Windows.Forms
        if ([System.Windows.Forms.Clipboard]::ContainsImage()) {
            $img = [System.Windows.Forms.Clipboard]::GetImage()
            return $img
        }
        else {
            Write-Error "No image found in clipboard."
            return $null
        }
    }

    # Prompt user for a file name
    $FileName = Read-Host "Enter the file name (without extension)"
    $FileName = (Split-Path . -leaf) + (Get-Date -Format "_MM_dd_yyyy_") + $FileName

    # Write-Host $FileName

    # Check if the file name is empty
    if (-not [string]::IsNullOrEmpty($FileName)) {
        Set-Location $dir        
        $FilePath = Join-Path -Path (Get-Location).Path -ChildPath "$FileName.png"
        # Write-Host $FilePath 
        (Get-ClipboardImage).Save($FilePath, [System.Drawing.Imaging.ImageFormat]::Png)
        Write-Output "Image saved to $FilePath"

    }
    else {
        Write-Error "File name cannot be empty."
    }

    if ($setPathToClipboard) {
        Set-Clipboard $FilePath
        Write-Host "`nPath copied, ready to paste as path`n" -ForegroundColor Green
    } else {
        Write-Host "You can always copy the path by selecting the path above."
    }

    Set-Location $origLoc

}


function browse{ Start-Process "msedge.exe" -ArgumentList (Resolve-Path .) }

function Add-AccountingInformation {
    [alias("acc")]
    param()

    $i = 1
    while($true){
        c:\Users\sgast\CODING\powershell_scripts\information_to_cuentas_csv.ps1     
        $i++;
        Write-Host "`nPress 'x' to end this command." -ForegroundColor Blue
        $continue = Read-Host
        if ($continue -eq 'x') {
            break
    }}
    # Printing after finishing the execution
    $file_path = "C:\Users\sgast\documents_personal\excel\cuentas.csv"
    Get-Content $file_path -Tail ($i+10)
    
 }

 
function Set-PowershellTheme {
    [alias("setPowTheme")]
    param (
        [string]$theme
    )
    $json_path = 'C:\Users\sgast\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json'
    $json = Get-Content $json_path | ConvertFrom-Json
    $json.profiles.list[0].colorScheme = $theme
    $json | ConvertTo-Json -depth 100 | Set-Content $json_path
}

function Set-Workspace {
    [alias("workspace")]
    param(
        [string]$val
    )

    $wall_path = "C:\Users\sgast\images\wallpapers"
    $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

    function IsDarkModeEnabled {
        ((Get-ItemPropertyValue -Path $registryPath -Name AppsUseLightTheme) -eq 0) -and ((Get-ItemPropertyValue -Path $registryPath -Name SystemUsesLightTheme) -eq 0)
    }

    if ($val -in @('w', 'wolfram','light-mode') ){
        $pict = Join-Path -Path $wall_path -ChildPath "working.jpg"

        if (IsDarkModeEnabled){
            Write-Host "Setting light mode"
            Start-Process ms-settings:colors
            Write-Host "Setting light mode on pow"
            Set-PowershellTheme 'One Half Light (Copy)'
            Write-Host "Moving... "
            Set-Location 'C:\users\sgast\wolfram'
            Write-Host "Loading kernel... "
            . "C:\Users\sgast\wolfram\scripts\kernel.ps1" 
        } else {
            Write-Host "Computer is already set on light mode."
        }
        
    } elseif ($val -in @('out','dark','darkmode','dark-mode')) {
        $wallpapers = Get-ChildItem (Join-Path -Path $wall_path -ChildPath "real_wallpapers")
        $rand = Get-Random -Maximum ($wallpapers).count
        $pict = $wallpapers[$rand].FullName
        
        if (-not (IsDarkModeEnabled)){
            Write-Host "Setting dark mode"
            Start-Process ms-settings:colors
            Write-Host "Setting dark mode on pow"
            setPowTheme 'One Half Dark'
            Set-Location '~'
            Write-Host "Cleaning functions"
            try {
                cleaner
            }
            catch {
                Write-Host "Ups! It looks like .\scrips\kernel.ps1 hasn't been defined!" -ForegroundColor Blue
            }
        } else {
            Write-Host "Computer is already set on dark mode. Changing desktop wallpaper accordingly." -ForegroundColor Blue
        }

    } else {
        Write-Host "`nWrong Flag. Run Again`n" -ForegroundColor Red
    }

    Set-AllDesktopWallpapers $pict

}

function Show-Screenshot {
    [alias("showss")]
    param(
        [int]$int
    )

    $screenshots = (Get-ChildItem "C:\Users\sgast\OneDrive\" | Select-Object -Index 3).FullName + "\Capturas de pantalla\"

    $screen_on_edge = "c:\Users\sgast\images\screenshots\"

    Get-ChildItem $screenshots | ForEach-Object {
        $newname = ($_.Name -replace ' ','_')
        Move-Item $_.FullName -Destination ( Join-Path $screen_on_edge $newname)
        
    }

    $files = Get-ChildItem $screen_on_edge | Select-Object -Last $int

    foreach ($file in $files) { Start-Process "msedge.exe" -ArgumentList $file.FullName } 

}

function Copy-Path {
    [alias("cpa")] 
    param(
        [string]$path
    ) 

    Set-Clipboard (Resolve-Path $path).ToString() 
} 

function Get-YouTube {
    [alias("yt")]
    param(
        [string]$flag #YouTube id-link or flag
    )

    if ($flag.Contains("https://")) {
        $match = "https://www.youtube.com/watch?v=q1fsBWLpYW4/sfdsfsd/sdfsdf/sdf/sdf/fsd/".Replace("(.*v=)","").Replace("/.*","")
        $url = -join ("https://www.youtube.com/embed/", $match)
        Start-Process $url  

    } elseif ( $flag -eq 'h') {
        $url = 'https://www.youtube.com/feed/history'
        Start-Process $url 
        break

    } elseif ($flag -eq 'wl'){
        $url = 'https://www.youtube.com/playlist?list=WL'
        Start-Process $url 
        break
    }

}

function log {
    python 'C:\Users\sgast\CODING\python_files\audio\kernel.py' $args[0]
}

function powAdmin{
    Start-Process powershell -Verb RunAs
}

function office {
	param(
		[string]$val
	)
    $officePath = 'C:\Program Files\Microsoft Office\root\Office16' 
	
    switch($val){
		'word'	{& Join-Path $officePath -ChildPath 'WINWORD.exe'}
		'excel'	{& Join-Path $officePath -ChildPath 'EXCEL.exe'}
		'point'	{& Join-Path $officePath -ChildPath 'POWERPNT.exe'}
		'onote'	{& Join-Path $officePath -ChildPath 'ONENOTE.exe'}
	}
	
}
