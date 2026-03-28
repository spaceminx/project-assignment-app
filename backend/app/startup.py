from .database import db
from .models import Project
from .import_projects import import_projects


def initialize_database():
    db.create_all()

    project_count = Project.query.count()

    if project_count < 10:
        added_count = import_projects()
        print(f"Imported {added_count} projects during startup.")
    else:
        print(f"Projects already initialized ({project_count} found). Skipping import.")