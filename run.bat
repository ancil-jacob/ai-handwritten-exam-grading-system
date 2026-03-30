@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\activate.bat (
    echo Creating virtual environment...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
echo Installing dependencies...
pip install -e . -q
python main.py
