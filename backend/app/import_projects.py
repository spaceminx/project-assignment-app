from bs4 import BeautifulSoup
from pathlib import Path

from . import create_app
from .database import db
from .models import Project

HTML_FILE = Path(__file__).resolve().parent.parent / "data" / "project_assignment.html"

def extract_projects():
    with open(HTML_FILE, "r", encoding="UTF-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    select = soup.find("select", {"multiple": True})

    if not select:
        return []

    projects = []
    seen = set()

    for row in select.find_all("option"):
        name = row.get_text().strip()

        if name and name not in seen:
            projects.append(name)
            seen.add(name)

    return projects

def import_projects():
    projects = extract_projects()

    project_count = 0
    for project in projects:
        existing = Project.query.filter_by(name=project).first()
        if not existing:
            db.session.add(Project(name=project))
            project_count += 1

    db.session.commit()
    return project_count

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        added = import_projects()
        print(F"Imported {added} projects.")