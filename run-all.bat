@echo off
cd /d "%~dp0"
title GradeAI Runner
if not exist .venv\Scripts\activate.bat (
    echo Creating virtual environment...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
pip install -e . -q
python run_all.py
