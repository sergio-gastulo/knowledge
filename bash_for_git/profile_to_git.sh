#!/bin/bash

profile_path="/c/Users/sgast/OneDrive/Documentos/WindowsPowerShell/Microsoft.PowerShell_profile.ps1"
destination_path="/c/Users/sgast/CODING/powershell_scripts/"

cp "$profile_path" "$destination_path"

git add "/powershell_scripts/Microsoft.PowerShell_profile.ps1"

git commit -m "Auto-commit: $(date '+%Y-%m-%d')"

git push -u origin main