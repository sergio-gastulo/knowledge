
function zoom {
    $zoom = "C:\Users\sgast\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom Workplace.lnk"
    Start-Process $zoom
}

function wolfram {
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

function Get-ClipIm {
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
    $FileName = (split-path . -leaf) + (Get-Date -Format "_MM_dd_yyyy_") + $FileName

    # Check if the file name is empty
    if (-not [string]::IsNullOrEmpty($FileName)) {
        $FilePath = Join-Path -Path (Get-Location) -ChildPath "$FileName.png"
        $ClipboardImage = Get-ClipboardImage
        if ($ClipboardImage -ne $null) {
            # Save image to the specified path
            $ClipboardImage.Save($FilePath, [System.Drawing.Imaging.ImageFormat]::Png)
            Write-Output "Image saved to $FilePath"
        }
    }
    else {
        Write-Error "File name cannot be empty."
    }
}


function Edge-Browsing-File{ Start-Process "msedge.exe" -ArgumentList (Resolve-Path .) }


function Support-Article{ C:\Users\sgast\CODING\powershell_scripts\support_article_dimensions.ps1 }


function Accounting-Info { 

    $i = 1
    
    while($true){
        
        c:\Users\sgast\CODING\powershell_scripts\information_to_cuentas_csv.ps1
        
        $i++;
        Write-Host " "
        $continue = Read-Host "press x to exit"
        Write-Host " "
        
        if ($continue -eq 'x') {
            break
    }}

    $file_path = "C:\Users\sgast\documents_personal\excel\cuentas.csv"
    
    Get-Content $file_path | Select-Object -Last ($i+10)
    
 }


# Add-Type to import user32.dll functions
# Add-Type @"
# using System;
# using System.Runtime.InteropServices;
# public class MouseActions
# {
#     [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
#     public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);

#     [DllImport("user32.dll")]
#     public static extern bool SetCursorPos(int X, int Y);

#     public const int MOUSEEVENTF_LEFTDOWN = 0x02;
#     public const int MOUSEEVENTF_LEFTUP = 0x04;
# }
# "@
# failed autoclicker, worthless by now 
# function Set-MousePositionAndClick {
#     param (
#         [int]$x,
#         [int]$y
#     )

#     # Set mouse position
#     [MouseActions]::SetCursorPos($x, $y)
    
#     # Perform left click
#     [MouseActions]::mouse_event([MouseActions]::MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     Start-Sleep -Milliseconds 100
#     [MouseActions]::mouse_event([MouseActions]::MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
# }

function setPowTheme {
    param (
        [string]$theme
    )
    $json_path = 'C:\Users\sgast\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json'
    $json = Get-Content $json_path | ConvertFrom-Json
    $json.profiles.list[0].colorScheme = $theme
    $json | ConvertTo-Json -depth 100 | Set-Content $json_path
}

function workspace { 
    $wall_path = "C:\Users\sgast\images\wallpapers"
    $val = $args[0]
    $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

    function IsDarkModeEnabled {
        ((Get-ItemPropertyValue -Path $registryPath -Name AppsUseLightTheme) -eq 0) -and ((Get-ItemPropertyValue -Path $registryPath -Name SystemUsesLightTheme) -eq 0)
    }

    if ($val -eq 'w' ){
        $pict = Join-Path -Path $wall_path -ChildPath "working.jpg"

        if (IsDarkModeEnabled){
            Write-Host "Setting light mode"
            Start-Process ms-settings:colors
            Write-Host "Setting light mode on pow"
            setPowTheme 'Tango Light (modified)'
            Write-Host "Moving... "
            Set-Location '~\wolfram'
            Write-Host "Loading kernel... "
            . '.\scripts\kernel.ps1' 
        } else {
            Write-Host "Computer is already set on light mode."
        }
        
    } elseif ($val -eq 'out') {
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
            cleaner
        } else {
            Write-Host "Computer is already set on dark mode. Changing desktop wallpaper accordingly."
        }

    } else {
        Write-Host "Wrong Flag. Run Again"
    }

    Set-AllDesktopWallpapers $pict

}

function Show-Screenshot {

    $screenshots = (Get-ChildItem "C:\Users\sgast\OneDrive\" | Select-Object -Index 3).FullName + "\Capturas de pantalla\"

    $screen_on_edge = "c:\Users\sgast\images\screenshots\"

    Get-ChildItem $screenshots | ForEach-Object {
        $newname = ($_.Name -replace ' ','_')
        Move-Item $_.FullName -Destination ( Join-Path $screen_on_edge $newname)
        
    }

    $int = Read-Host "Last n pictures to open on edge"

    $files = Get-ChildItem $screen_on_edge | Select-Object -Last $int

    foreach ($file in $files) { Start-Process "msedge.exe" -ArgumentList $file.FullName } 

}

function copy-path { 
    param(
        [string]$path
    ) 

    Set-Clipboard (Resolve-Path $path).ToString() 
} 

function yt {
    param(
        [string]$id #YouTube id-link or flag
    )

    if ($id.Contains("https://")) {
        $id = $id.Split("v=")[-1]
        $url = -join ("https://www.youtube.com/embed/", $id)
        Start-Process $url  
    } elseif ( $id -eq 'h') {
        $url = 'https://www.youtube.com/feed/history'
        Start-Process $url 
        break
    } elseif ($id -eq 'wl'){
        $url = 'https://www.youtube.com/playlist?list=WL'
        Start-Process $url 
        break
    }

}
