from .database import db

employee_projects = db.Table(
    "employee_projects",
    db.Column("employee_id", db.Integer, db.ForeignKey("employees.id"), primary_key=True),
    db.Column("project_id", db.Integer, db.ForeignKey("projects.id"), primary_key=True)
)

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    tech_stack = db.Column(db.String(100), nullable=False)
    project_duration = db.Column(db.String(50), nullable=False)
    additional_skills = db.Column(db.String(255), nullable=True)
    availability = db.Column(db.Boolean, nullable=False, default=True)

    projects = db.relationship(
        "Project",
        secondary=employee_projects,
        back_populates="employees"
    )

    def to_json(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "experience_level": self.experience_level,
            "tech_stack": self.tech_stack,
            "project_duration": self.project_duration,
            "additional_skills": self.additional_skills,
            "availability": self.availability,
            "projects": [
                {"id": project.id, "name": project.name}
                for project in self.projects
            ]
        }

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    employees = db.relationship(
        "Employee",
        secondary=employee_projects,
        back_populates="projects"
    )