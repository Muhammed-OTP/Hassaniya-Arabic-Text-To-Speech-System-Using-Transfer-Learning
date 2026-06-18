# Hassaniya TTS — Windows environment setup
# Fixes WinError 206 (path too long) by using drive letter T: for this project folder.

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$DriveLetter = "T:"

Write-Host "=== Hassaniya TTS — Setup ===" -ForegroundColor Green
Write-Host "Project: $ProjectRoot"

# Map short drive letter (avoids Windows 260-char path limit during pip install)
if (-not (Test-Path $DriveLetter)) {
    subst $DriveLetter $ProjectRoot
    Write-Host "Mapped $DriveLetter -> project folder" -ForegroundColor Cyan
} else {
    Write-Host "Drive $DriveLetter already mapped" -ForegroundColor Yellow
}

Set-Location $DriveLetter

# Create venv if missing
if (-not (Test-Path ".venv\Scripts\python.exe")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
}

$python = ".\.venv\Scripts\python.exe"
$pip = ".\.venv\Scripts\pip.exe"

& $python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing requirements (this may take a few minutes)..." -ForegroundColor Cyan
& $pip install -r requirements.txt

Write-Host ""
Write-Host "=== Setup complete ===" -ForegroundColor Green
Write-Host "Activate with:"
Write-Host "  subst T: `"$ProjectRoot`"   # if not already mapped"
Write-Host "  T:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  jupyter notebook"
Write-Host ""
Write-Host "Run smoke test:"
Write-Host "  python scripts\smoke_test.py"
