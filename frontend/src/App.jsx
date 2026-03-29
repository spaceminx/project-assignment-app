import { useEffect, useState } from "react";
import "./App.css"

function App() {
  const [projects, setProjects] = useState([]);
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    experience_level: "",
    tech_stack: "",
    project_duration: "",
    additional_skills: "",
    availability: false,
    projects: []
  });

  // fetch projects
useEffect(() => {
  fetch("/api/projects")
    .then(async (res) => {
      console.log("response status:", res.status);

      if (!res.ok) {
        const text = await res.text();
        console.log("response text:", text);
        throw new Error(`Failed with status ${res.status}`);
      }

      return res.json();
    })
    .then((data) => {
      console.log("projects from backend:", data);
      setProjects(data);
    })
    .catch((err) => {
      console.error("fetch error:", err);
    });
}, []);

  // handle input change
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setForm(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  // handle multi-select
  const handleProjectsChange = (e) => {
    const selected = Array.from(e.target.selectedOptions).map(
      option => option.value
    );

    setForm(prev => ({
      ...prev,
      projects: selected
    }));
  };

  // submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (form.projects.length === 0) {
      alert("Please select at least one project.");
      return;
    }

    const formData = new FormData();

    Object.keys(form).forEach(key => {
      if (key === "projects") {
        form.projects.forEach(p => formData.append("projects", p));
      }else if(key === "availability"){
        if(form.availability){
          formData.append("availability", "true");
        }
      } else {
        formData.append(key, form[key]);
      }
    });

    const res = await fetch("/api/profile", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    if (!res.ok) {
      alert(Object.values(data.errors).join("\n"));
      return;
    }

    setForm({
      ...data.employee,
      projects: data.employee.projects.map(p => String(p.id))
    });

    alert(data.message);
  };

  return (
  <div className="page">
    <div className="card">
      <h2>Project Assignment Form</h2>
      <p className="subtitle">
        Complete your profile to get assigned to internal projects.
      </p>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Full Name</label>
          <input
            type="text"
            name="full_name"
            value={form.full_name}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Email Address</label>
          <input
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Experience Level</label>
          <select
            name="experience_level"
            value={form.experience_level}
            onChange={handleChange}
            required
          >
            <option value="">Select your level</option>
            <option value="junior">Junior</option>
            <option value="mid">Mid-level</option>
            <option value="senior">Senior</option>
          </select>
        </div>

        <div className="form-group">
          <label>Primary Tech Stack</label>
          <select
            name="tech_stack"
            value={form.tech_stack}
            onChange={handleChange}
            required
          >
            <option value="">Choose one</option>
            <option value="backend">Backend</option>
            <option value="frontend">Frontend</option>
            <option value="fullstack">Fullstack</option>
            <option value="data">Data</option>
            <option value="devops">DevOps</option>
            <option value="mobile">Mobile</option>
          </select>
        </div>

        <div className="form-group">
          <label>Available Projects</label>
          <select
            name="projects"
            multiple
            value={form.projects}
            onChange={handleProjectsChange}
          >
            {projects.map((p) => (
              <option key={p.id} value={String(p.id)}>
                {p.name}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Preferred Project Duration</label>
          <div className="radio-group">
            <label>
              <input
                type="radio"
                name="project_duration"
                value="short"
                checked={form.project_duration === "short"}
                onChange={handleChange}
              />
              Short-term (1-3 months)
            </label>

            <label>
              <input
                type="radio"
                name="project_duration"
                value="medium"
                checked={form.project_duration === "medium"}
                onChange={handleChange}
              />
              Medium-term (3-6 months)
            </label>

            <label>
              <input
                type="radio"
                name="project_duration"
                value="long"
                checked={form.project_duration === "long"}
                onChange={handleChange}
              />
              Long-term (6+ months)
            </label>
          </div>
        </div>

        <div className="form-group">
          <label>Additional Skills</label>
          <input
            name="additional_skills"
            value={form.additional_skills}
            onChange={handleChange}
          />
        </div>

        <div className="form-group checkbox-group">
          <label>
            <input
              type="checkbox"
              name="availability"
              checked={form.availability}
              onChange={handleChange}
            />
            I confirm availability for the selected projects
          </label>
        </div>

        <div className="actions">
          <button type="submit">Save Profile</button>
          <button
            type="button"
            onClick={() =>
              setForm({
                full_name: "",
                email: "",
                experience_level: "",
                tech_stack: "",
                project_duration: "",
                additional_skills: "",
                availability: false,
                projects: []
              })
            }
          >
            Clear Form
          </button>
        </div>
      </form>
    </div>
  </div>
);
}

export default App;

