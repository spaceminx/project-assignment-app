document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("project-form");
    const projectsSelect = document.getElementById("projects");

    function fillForm(employee) {
        form.full_name.value = employee.full_name || "";
        form.email.value = employee.email || "";
        form.experience_level.value = employee.experience_level || "";
        form.tech_stack.value = employee.tech_stack || "";
        form.additional_skills.value = employee.additional_skills || "";
        form.availability.checked = !!employee.availability;

        document.querySelectorAll('input[name="project_duration"]').forEach(radio => {
            radio.checked = radio.value === employee.project_duration;
        });

        const selectedIds = employee.projects.map(p => String(p.id));

        Array.from(projectsSelect.options).forEach(option => {
            option.selected = selectedIds.includes(option.value);
        });
    }

    // load projects
    fetch("/projects")
        .then(res => res.json())
        .then(data => {
            data.forEach(project => {
                const option = document.createElement("option");
                option.value = project.id;
                option.textContent = project.name;
                projectsSelect.appendChild(option);
            });
        });

    // submit handler
    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const selected = Array.from(projectsSelect.options).filter(o => o.selected);

        if (selected.length === 0) {
            alert("Please select at least one project.");
            return;
        }

        const formData = new FormData(form);

        try {
            const response = await fetch("/profile", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                alert(Object.values(data.errors).join("\n"));
                return;
            }

            fillForm(data.employee);
            alert(data.message);

        } catch (err) {
            alert("Something went wrong.");
        }
    });
});