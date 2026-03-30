Set-Location $PSScriptRoot
if (-not (Test-Path .venv\Scripts\Activate.ps1)) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1
Write-Host "Installing dependencies..."
pip install -e . -q
python main.py
