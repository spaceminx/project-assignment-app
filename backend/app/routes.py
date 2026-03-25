from flask import Blueprint, request, jsonify, render_template
from .models import Project
from .services import save_or_update_employee
from .validators import validate_profile


api = Blueprint('api', __name__)

@api.route("/", methods=["GET"])
def index():
    return render_template("project_assignment.html")


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

    employee, message = save_or_update_employee(profile_data)

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
