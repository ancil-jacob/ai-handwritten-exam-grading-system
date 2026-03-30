"""Entry point - runs the GradeAI server."""

if __name__ == "__main__":
    try:
        import uvicorn
    except ModuleNotFoundError:
        import subprocess
        import sys

        print("uvicorn not found. Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
        import uvicorn
    uvicorn.run(
        "gradeai.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
