from .database import db

employee_projects = db.Table(
    "employee_projects",
    db.Column("employee_id", db.Integer, db.ForeignKey("employees.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("projects.id"))
)

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    experience = db.Column(db.String(50), nullable=False)
    primary_technology = db.Column(db.String(100), nullable=False)
    preferred_project_duration = db.Column(db.String(50), nullable=False)
    additional_skills = db.Column(db.String(255), nullable=True)
    is_available = db.Column(db.Boolean, nullable=False, default=True)

    projects = db.relationship(
        "Project",
        secondary=employee_projects,
        back_populates="employees"
    )

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    employees = db.relationship(
        "Employee",
        secondary=employee_projects,
        back_populates="projects"
    )