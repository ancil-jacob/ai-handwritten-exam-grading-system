# GradeAI - Start Backend + Frontend
Set-Location $PSScriptRoot
if (-not (Test-Path .venv\Scripts\Activate.ps1)) {
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1
pip install -e . -q
python run_all.py
