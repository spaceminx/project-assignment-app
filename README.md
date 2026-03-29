# Project Assignment App

A full-stack web application built with Flask (backend) and React (frontend) for managing internal project assignments.

Employees can register their profile, select projects they are interested in, and update their information.

## Features

- Create and update employee profiles
- Select multiple projects
- Dynamic project list from database
- Form validation (frontend + backend)
- Email-based identification (update existing users)
- Automatic database initialization on first run

---

## Database Design

Tables:

- **employees**: stores employee profile information (name, email, experience, etc.)
- **projects**: stores available projects imported from HTML
- **employee_projects**: many-to-many relationship between employees and projects

SQLite was chosen because it is simple to use and does not require any additional setup.

---

## Database Initialization

On startup, the application:

- creates database tables if they do not exist
- imports project data from HTML if the projects table is empty

This ensures the database is initialized only once.

---

## Running the Application with Docker

> **Note:** Make sure Docker is installed and running.


**Default ports**

The application uses the following default ports:
- Frontend: http://localhost:5173
- Backend API: http://localhost:5001/api

**Changing ports**

If you want to change ports, navigate to docker-compose.yml file:

```yaml
services:
  backend:
    ports:
      - "5001:5000"   # change 5001 to your preferred port

  frontend:
    ports:
      - "5173:5173"   # change 5173 (left one) to your preferred port
```

### 1. Clone the repository
```
git clone https://github.com/spaceminx/project-assignment-app.git
```
```
cd project-assignment-app
```

### 2. Build and run the application

```
docker compose up --build
```

### 3. Open the application

Open in browser:
- http://localhost:5173/

---

## Viewing the Database

The SQLite database file is created automatically at:

/backend/database/project_assignment.db


Can be opened by using any SQLite client or IDE

- SQLite CLI:
  ```
  sqlite3 backend/database/project_assignment.db
  ```
