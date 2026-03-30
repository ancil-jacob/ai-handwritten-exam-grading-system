# GradeAI

**Open-source AI-based subjective answer evaluation.** Runs locally: evaluate typed or handwritten student answers using semantic similarity, concept coverage, and optional grammar scoring. No paid APIs.

---

## Prerequisites

- **Python 3.10+** — [python.org](https://www.python.org/downloads/)
- **Node.js 18+** and **npm** — [nodejs.org](https://nodejs.org/)

---

## Quick start (new machine)

**1. Open project folder**
```bash
cd grade
```

**2. Create and activate virtual environment**

Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate
```
Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
pip install -e .
```

**4. Seed data (once)**
```bash
python scripts/seed_dev.py
```
Creates admin user `admin@gradeai.local` / `admin123`, Physics subject, and a sample exam.

**5. Run**
```bash
python run_all.py
```
- **Frontend:** http://localhost:5173  
- **Backend API:** http://localhost:8000  
- **API docs:** http://localhost:8000/docs  

Log in with `admin@gradeai.local` / `admin123`.

---

## Run options

| Action        | Command / URL |
|---------------|----------------|
| Start all     | `python run_all.py` or double-click `run-all.bat` (Windows) |
| Backend only  | `python main.py` or `run.bat` |
| Frontend only | `cd frontend` → `npm install` → `npm run dev` |

---

## Project structure

```
grade/
├── gradeai/          # Backend (FastAPI, SQLAlchemy, embeddings, OCR)
├── frontend/         # React + TypeScript + Vite + Tailwind
├── scripts/          # seed_dev.py
├── tests/
├── alembic/          # DB migrations
├── main.py           # Backend entry
├── run_all.py        # Start backend + frontend
├── requirements.txt # Python dependencies
└── pyproject.toml
```

---

## Configuration

- Copy `.env.example` to `.env` to override settings (debug, log level, database, etc.).
- **Optional:** OCR for handwritten answers: `pip install paddlepaddle paddleocr`
- **Optional:** Grammar scoring: included in `requirements.txt` (LanguageTool).

First evaluation downloads the embedding model (~400MB) once.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `No module named 'gradeai'` | From project root: `pip install -e .` |
| Subject dropdown empty | Run `python scripts/seed_dev.py` |
| "Cannot reach backend" | Start backend: `python main.py` or `python run_all.py` |
| Frontend won’t start | In `frontend`: `npm install` then `npm run dev` |

---

## Tests

```bash
pytest
```

---

## License & credits

Open-source. No paid APIs; runs fully locally.
