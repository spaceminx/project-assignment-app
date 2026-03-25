from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / "database" / "project_assignment.db"

SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False