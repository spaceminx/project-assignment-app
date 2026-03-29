PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE employees (
	id INTEGER NOT NULL, 
	full_name VARCHAR(100) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	experience_level VARCHAR(50) NOT NULL, 
	tech_stack VARCHAR(100) NOT NULL, 
	project_duration VARCHAR(50) NOT NULL, 
	additional_skills VARCHAR(255), 
	availability BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
CREATE TABLE projects (
	id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO projects VALUES(1,'Customer Portal Redesign');
INSERT INTO projects VALUES(2,'Data Pipeline Migration');
INSERT INTO projects VALUES(3,'Mobile App Enhancement');
INSERT INTO projects VALUES(4,'Internal Analytics Dashboard');
INSERT INTO projects VALUES(5,'API Gateway Implementation');
INSERT INTO projects VALUES(6,'Cloud Infrastructure Setup');
INSERT INTO projects VALUES(7,'E-commerce Platform Update');
INSERT INTO projects VALUES(8,'Reporting System Automation');
INSERT INTO projects VALUES(9,'Microservices Architecture Transition');
INSERT INTO projects VALUES(10,'Customer Data Platform Integration');
CREATE TABLE employee_projects (
	employee_id INTEGER NOT NULL, 
	project_id INTEGER NOT NULL, 
	PRIMARY KEY (employee_id, project_id), 
	FOREIGN KEY(employee_id) REFERENCES employees (id), 
	FOREIGN KEY(project_id) REFERENCES projects (id)
);
COMMIT;
