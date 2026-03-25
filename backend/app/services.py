from .models import Employee, Project
from .database import db

def save_or_update_employee(data):

    email = data["email"].lower().strip()

    employee = Employee.query.filter_by(email=email).first()

    selected_projects = Project.query.filter(
        Project.id.in_(data["projects"])
    ).all()

    if employee:
        employee.full_name = data["full_name"]
        employee.experience_level = data["experience_level"]
        employee.tech_stack = data["tech_stack"]
        employee.project_duration = data["project_duration"]
        employee.additional_skills = data["additional_skills"]
        employee.availability = True
        employee.projects = selected_projects
        message = "Profile updated successfully."
    else:
        employee = Employee(
            full_name=data["full_name"],
            email=email,
            experience_level=data["experience_level"],
            tech_stack=data["tech_stack"],
            project_duration=data["project_duration"],
            additional_skills=data["additional_skills"],
            availability=True
        )
        employee.projects = selected_projects
        db.session.add(employee)
        message = "Profile created successfully."

    db.session.commit()

    return employee, message