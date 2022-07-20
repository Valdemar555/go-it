-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(120) UNIQUE NOT NULL
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    student VARCHAR(120) UNIQUE NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: courses
DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cours_name VARCHAR(120) UNIQUE NOT NULL,
    teacher_name VARCHAR(120) NOT NULL
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    cours_id INTEGER NOT NULL,
    grades INTEGER NOT NULL,
    created_at DATE,
    FOREIGN KEY (cours_id) REFERENCES courses (id),
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);