from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
GRADES = 20
GROUPS = [('A-22',), ('B-22',), ('C-22',)]
COURSE = ['Mathematics', 'Physics', 'Jurisprudence', 'History', 'English']
for_grades = []
fake_data = faker.Faker('ru-RU')
for _ in range(1000):
    for_grades.append(
        (randint(1, 30), randint(1, 5), randint(1, 5), fake_data.date_between_dates(date_start=datetime(2022, 1, 1))))

def add_fake_name(number_students, number_teachers):
    fake_students = []
    fake_teachers = []
    
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
    
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    return fake_students, fake_teachers

def add_data(students, teachers) -> tuple():
    for_students = []
    for_courses = []
    for student in students:
        for_students.append((student, randint(1, 3)))
    
    course_counter = 0
    teacher_counter = 0
    for _ in range(len(COURSE) + 1):
        if course_counter > len(COURSE) + 1:
            break
        if teacher_counter == len(teachers):
            teacher_counter = 0
        else:
            for_courses.append((COURSE[course_counter], teachers[teacher_counter]))
            course_counter += 1
            teacher_counter += 1
    return for_students, for_courses

def insert_in_db(students, groups, course, grades) -> None:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        
        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        
        cur.executemany(sql_to_groups, groups)
        
        sql_to_students = """INSERT INTO students(student, group_id)
                               VALUES (?, ?)"""
        
        cur.executemany(sql_to_students, students)
        
        sql_to_courses = """INSERT INTO courses(cours_name, teacher_name)
                               VALUES (?, ?)"""
        
        cur.executemany(sql_to_courses, course)
        
        sql_to_grades = """INSERT INTO grades(student_id, cours_id, grades, created_at)
                                       VALUES (?, ?, ?, ?)"""
        
        cur.executemany(sql_to_grades, grades)
        
        con.commit()


if __name__ == "__main__":
    students, course = add_fake_name(NUMBER_STUDENTS, NUMBER_TEACHERS)
    students, course = add_data(students, course)
    insert_in_db(students, GROUPS, course, for_grades)