import sqlite3


def execute_query(sql: str):
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def five_students_GPA(): #1
    sql = """
    SELECT s.student, AVG(g.grades) AS GPA
    FROM grades g
    JOIN students s ON s.id = g.student_id
    GROUP BY s.student
    ORDER BY GPA DESC
    LIMIT 5
    """
    return execute_query(sql)

def best_student_GPA(): #2
    sql = """
    SELECT c.cours_name, s.student, AVG(g.grades)
    FROM grades g
    JOIN students s ON s.id = g.student_id
    JOIN courses c ON c.id = g.cours_id
    GROUP BY c.cours_name
    """
    return execute_query(sql)

def GPA_from_group(): #3
    sql = """
    SELECT cours_name, AVG(grades)
    FROM grades g 
    LEFT JOIN students s ON s.id = g.student_id 
    LEFT JOIN courses c ON c.id = g.cours_id 
    LEFT JOIN groups g2 ON g.id = s.group_id 
    WHERE s.group_id = 1
    GROUP  BY c.cours_name
    """
    return execute_query(sql)



def all_groups_GPA(): #4
    sql = """
    SELECT AVG(grades) AS GPA
    FROM grades g
    """
    return execute_query(sql)

def teacher_courses(): #5
    sql = """
    SELECT cours_name, teacher_name  
    FROM courses c
    GROUP BY teacher_name    
    """
    return execute_query(sql)

def students_by_group(): #6
    sql = """
    SELECT student
    FROM students s 
    WHERE group_id = 1
    ORDER BY student
    """
    return execute_query(sql)

def students_grades_by_cours(): #7
    sql = """
    SELECT student, cours_name, grades
    FROM grades g 
    LEFT JOIN students s ON s.id = g.student_id 
    LEFT JOIN courses c ON c.id = g.cours_id 
    LEFT JOIN groups g2 ON g.id = s.group_id
    WHERE s.group_id = 2
    ORDER BY cours_id 
    """
    return execute_query(sql)

def student_last_lesson(): #8
    sql = """
    SELECT cours_name, student, grades, MAX(created_at)
    FROM students s 
    LEFT JOIN grades g ON g.student_id = s.id 
    LEFT JOIN courses c ON c.id = g.cours_id
    WHERE g.cours_id = 1 AND s.group_id = 1
    GROUP BY s.student 
    ORDER BY g.created_at DESC 
	"""
    return execute_query(sql)

def courses_by_student(): #9
    sql = """
    SELECT DISTINCT cours_name
    FROM courses c JOIN grades g ON g.cours_id = c.id
    WHERE student_id = 5
	"""
    return execute_query(sql)

def teacher_by_courses(): #10
    sql = """
    SELECT DISTINCT cours_name, teacher_name 
    FROM courses c JOIN grades g ON g.cours_id = c.id 
    WHERE g.student_id =3 AND c.id = 2
	"""
    return execute_query(sql)

def GPA_teacher_to_student(): #11
    sql = """
    SELECT student, cours_name, teacher_name, AVG(grades)
    FROM grades g 
    LEFT JOIN courses c ON c.id = g.cours_id
    LEFT JOIN students s ON s.id = g.student_id 
    WHERE g.student_id = 1
    GROUP BY g.student_id 
    """
    return execute_query(sql)

def GPA_by_teacher(): #12
    sql = """
    SELECT AVG(grades), cours_name, teacher_name
    FROM grades g
    LEFT JOIN courses c ON c.id = g.cours_id 
    GROUP BY cours_id 
    """
    return execute_query(sql)



if __name__ == '__main__':
    print(five_students_GPA())
    print(best_student_GPA())
    print(GPA_from_group())
    print( all_groups_GPA())
    print(teacher_courses())
    print(students_by_group())
    print(students_grades_by_cours())
    print(student_last_lesson())
    print(courses_by_student())
    print(teacher_by_courses())
    print(GPA_teacher_to_student())
    print(GPA_by_teacher())

