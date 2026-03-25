import re

EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

def validate_email(email):
    return re.match(EMAIL_REGEX, email) is not None

def validate_profile(data):
    errors = {}

    if not data.get("full_name"):
        errors["full_name"] = "Full name is required."

    email = data.get("email")
    if not email:
        errors["email"] = "Email is required."
    elif not validate_email(email):
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