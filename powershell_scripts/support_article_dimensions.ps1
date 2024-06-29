
$path = "c:\Users\sgast\Wolfram\Support_Articles\System_Modeler"

$link = Read-Host "link"

$support_article_num = (($link -split "post=" )[-1] -split "\&")[0] + "\"

$fullPath = Join-Path -Path $path -ChildPath $support_article_num #works well

Start-Process $fullPath

Get-ChildItem $fullPath | ForEach-Object { 
    $obj = ([System.Drawing.Image]::FromFile($_.FullName)); 
    Write-Host (($_.Name -split '_')[-1] -replace '.png', ''), "-> $($obj.Width), $($obj.Height)" 
}

