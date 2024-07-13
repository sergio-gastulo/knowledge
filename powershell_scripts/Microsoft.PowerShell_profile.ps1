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

    $file_path = "C:\Users\sgast\Documents_personal\excel\cuentas.csv"
    
    Get-Content $file_path | Select-Object -Last ($i+10)
    
 }


# Add-Type to import user32.dll functions
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class MouseActions
{
    [DllImport("user32.dll", CharSet = CharSet.Auto, CallingConvention = CallingConvention.StdCall)]
    public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);

    [DllImport("user32.dll")]
    public static extern bool SetCursorPos(int X, int Y);

    public const int MOUSEEVENTF_LEFTDOWN = 0x02;
    public const int MOUSEEVENTF_LEFTUP = 0x04;
}
"@

function Set-MousePositionAndClick {
    param (
        [int]$x,
        [int]$y
    )

    # Set mouse position
    [MouseActions]::SetCursorPos($x, $y)
    
    # Perform left click
    [MouseActions]::mouse_event([MouseActions]::MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    Start-Sleep -Milliseconds 100
    [MouseActions]::mouse_event([MouseActions]::MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
}

function DarkLightMode { 

    $wall_path = "C:\Users\sgast\Documents_personal\images\wallpapers"
    
    $val = Read-Host "is this Personal hours or (W)orking hours"

    $registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

    function IsDarkModeEnabled {
        ((Get-ItemPropertyValue -Path $registryPath -Name AppsUseLightTheme) -eq 0) -and ((Get-ItemPropertyValue -Path $registryPath -Name SystemUsesLightTheme) -eq 0)
    }

    if ($val -eq "W" ){

        #by default my working hours theme is light mode
        $pict = Join-Path -Path $wall_path -ChildPath "working.jpg"

        if (IsDarkModeEnabled){
            Start-Process ms-settings:colors
        }
    
    } else {
        
        #if I'm not working I use darkmode
        $wallpapers = Get-ChildItem (Join-Path -Path $wall_path -ChildPath "real_wallpapers")
        $rand = Get-Random -Maximum ($wallpapers).count

        $pict = $wallpapers[$rand].FullName

        if (-not (IsDarkModeEnabled)){
            Start-Process ms-settings:colors
        }
        
    }

    Set-AllDesktopWallpapers $pict

}

function Screenshot-ToEdge {

    $screenshots = (Get-ChildItem "C:\Users\sgast\OneDrive\" | Select-Object -Index 3).FullName + "\Capturas de pantalla\"

    $screen_on_edge = "c:\Users\sgast\Documents_personal\images\screenshots\"

    Get-ChildItem $screenshots | ForEach-Object {
        $newname = ($_.Name -replace ' ','_')
        Move-Item $_.FullName -Destination ( Join-Path $screen_on_edge $newname)
        
    }

    $int = Read-Host "Last n pictures to open on edge"

    $files = Get-ChildItem $screen_on_edge | Select-Object -Last $int

    foreach ($file in $files) { Start-Process "msedge.exe" -ArgumentList $file.FullName } 

}


