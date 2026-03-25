import re

from flask import Blueprint, request, jsonify, render_template
from .database import db
from .models import Employee, Project

api = Blueprint('api', __name__)

EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


@api.route("/", methods=["GET"])
def index():
    return render_template("project_assignment.html")

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

def validate_profile(data):
    errors = {}

    if not data.get("full_name"):
        errors["full_name"] = "Full name is required."

    email = data.get("email")
    if not email:
        errors["email"] = "Email is required."
    elif not is_valid_email(email):
        errors["email"] = "Invalid email."

    if not data.get("experience_level"):
        errors["experience_level"] = "Experience level is required."

    if not data.get("tech_stack"):
        errors["tech_stack"] = "Tech stack is required."

    if not data.get("project_duration"):
        errors["project_duration"] = "Project duration is required."

    if not data.get("availability"):
        errors["availability"] = "Must confirm availability."

    if not data.get("projects"):
        errors["projects"] = "Select atleast one project."

    return errors


@api.route("/profile", methods=["POST"])
def save_profile():

    profile_data = {
        "full_name" : request.form.get("full_name", "").strip(),
        "email" : request.form.get("email", "").strip(),
        "experience_level" : request.form.get("experience_level", "").strip(),
        "tech_stack" : request.form.get("tech_stack", "").strip(),
        "project_duration" : request.form.get("project_duration", "").strip(),
        "additional_skills" : request.form.get("additional_skills", "").strip(),
        "availability" : request.form.get("availability", "").strip(),
        "projects" : request.form.getlist("projects"),
    }

    errors = validate_profile(profile_data)

    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    email = profile_data["email"].lower().strip()

    employee = Employee.query.filter_by(email=email).first()

    selected_projects = Project.query.filter(
        Project.id.in_(profile_data["projects"])
    ).all()

    if employee:
        employee.full_name = profile_data["full_name"]
        employee.experience_level = profile_data["experience_level"]
        employee.tech_stack = profile_data["tech_stack"]
        employee.project_duration = profile_data["project_duration"]
        employee.additional_skills = profile_data["additional_skills"]
        employee.availability = True
        employee.projects = selected_projects
        message = "Profile updated successfully."

    else:
        employee = Employee(
            full_name = profile_data["full_name"],
            email = email,
            experience_level = profile_data["experience_level"],
            tech_stack = profile_data["tech_stack"],
            project_duration = profile_data["project_duration"],
            additional_skills = profile_data["additional_skills"],
            availability = True
        )
        employee.projects = selected_projects
        db.session.add(employee)
        message = "Profile created successfully."

    db.session.commit()
    return jsonify({
        "success": True,
        "message": message,
        "employee": employee.to_json()
        }), 200


@api.route("/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()

    return jsonify([
        {"id": p.id, "name": p.name} for p in projects
    ])
