do {
    $description = Read-Host "`nType description. No commas, and no 'enhe'"
    if ($description -notmatch ',') {
        # At this moment, we can't prevent ñ from being prompted here.
        # We trust on our user.
        # bug known at enhe_is_not_detected_from_console....ps1
        break
    }
    Write-Host "`nDescription must not include 'enhe' or comma (,)" -ForegroundColor Red
} while ($true)