#!/bin/bash

echo "Previously find the path of the file you wanna add-commit-push"
echo "Filename:"
read filename

# Add the required file
git add $filename

# Commit the changes with a default commit message
git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M:%S')"

# Push changes to the remote repository
git push -u origin main
