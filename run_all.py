"""
GradeAI unified runner - starts backend and frontend together.

Usage: python run_all.py

- Backend starts in a new window (Windows) or background (Unix)
- Frontend runs in this terminal; Ctrl+C stops frontend
- Close the Backend window to stop the backend (Windows)
"""
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

ROOT = Path(__file__).resolve().parent

BACKEND_URL = "http://localhost:8000"
HEALTH_PATH = "/health"
POLL_INTERVAL = 2
HEALTH_TIMEOUT = 60


def wait_for_backend() -> bool:
    """Poll backend /health until ok or timeout. Returns True if ready."""
    deadline = time.monotonic() + HEALTH_TIMEOUT
    while time.monotonic() < deadline:
        try:
            with urlopen(f"{BACKEND_URL}{HEALTH_PATH}", timeout=5) as r:
                if r.status == 200:
                    return True
        except (URLError, OSError):
            pass
        time.sleep(POLL_INTERVAL)
    return False


def main():
    os.chdir(ROOT)

    print("=" * 50)
    print("  GradeAI - Starting Backend + Frontend")
    print("=" * 50)
    print("  Backend:  http://localhost:8000")
    print("  Frontend: http://localhost:5173")
    print("  Press Ctrl+C to stop frontend")
    print("=" * 50)

    # Ensure venv
    venv_activate = ROOT / ".venv" / "Scripts" / "activate.bat"
    if not venv_activate.exists():
        venv_activate = ROOT / ".venv" / "bin" / "activate"
    if not ROOT.joinpath(".venv").exists():
        print("\nCreating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", ".venv"])

    venv_python = ROOT / ".venv" / "Scripts" / "python.exe"
    if not venv_python.exists():
        venv_python = ROOT / ".venv" / "bin" / "python"
    python_exe = str(venv_python) if venv_python.exists() else sys.executable

    # Install backend deps
    print("\n[1/3] Installing backend dependencies...")
    subprocess.run([python_exe, "-m", "pip", "install", "-e", ".", "-q"], cwd=ROOT)

    if sys.platform == "win32":
        # Windows: start backend in new cmd window
        print("[2/3] Starting backend (new window)...")
        backend_bat = ROOT / "_run_backend.bat"
        subprocess.Popen(
            f'start "GradeAI Backend" cmd /k call "{backend_bat}"',
            cwd=ROOT,
            shell=True,
        )
    else:
        # Unix: start backend in background
        print("[2/3] Starting backend...")
        backend = subprocess.Popen(
            [python_exe, "main.py"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

    print("    Waiting for backend to be ready...")
    if not wait_for_backend():
        print("    Warning: Backend did not become ready in time. Starting frontend anyway.")
    else:
        print("    Backend is ready.")

    # Frontend
    frontend_dir = ROOT / "frontend"
    if not frontend_dir.exists():
        print("Error: frontend folder not found")
        sys.exit(1)

    if not (frontend_dir / "node_modules").exists():
        print("Installing frontend dependencies...")
        subprocess.run(["npm", "install"], cwd=frontend_dir, shell=(sys.platform == "win32"))

    print("[3/3] Starting frontend...")
    print("")
    subprocess.run(
        ["npm", "run", "dev"],
        cwd=frontend_dir,
        
        shell=(sys.platform == "win32"),
    )


if __name__ == "__main__":
    main()
