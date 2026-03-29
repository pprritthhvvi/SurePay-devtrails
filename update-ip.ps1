# ============================================================
# update-ip.ps1 -- Auto-detect LAN IP and patch mobile api.js
# Run this whenever your IP changes: .\update-ip.ps1
# ============================================================

# Get current LAN IP (prefer 10.x or 192.168.x over 172.x)
$allIPs = (Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object { $_.IPAddress -notmatch '^127\.' -and $_.IPAddress -notmatch '^169\.' } |
    Select-Object -ExpandProperty IPAddress)

$ip = $allIPs | Where-Object { $_ -match '^10\.' -or $_ -match '^192\.168\.' } | Select-Object -First 1
if (-not $ip) { $ip = $allIPs | Select-Object -First 1 }

Write-Host "[OK] Detected LAN IP: $ip" -ForegroundColor Green

# Path to api.js
$apiFile = "$PSScriptRoot\mobile-app\src\services\api.js"

# Replace the API_BASE_URL line
$content = Get-Content $apiFile -Raw
$updated = $content -replace "const API_BASE_URL = 'http://[^']+';", "const API_BASE_URL = 'http://${ip}:8000/api/v1';"
Set-Content $apiFile $updated -NoNewline

Write-Host "[OK] Updated api.js --> http://${ip}:8000/api/v1" -ForegroundColor Green
Write-Host ""
Write-Host "Demo Login Credentials:" -ForegroundColor Cyan
Write-Host "   Phone   : 9876543210"
Write-Host "   Password: demo123"
Write-Host ""
Write-Host "[->] Now restart Expo: npm start (in mobile-app/)" -ForegroundColor Yellow
