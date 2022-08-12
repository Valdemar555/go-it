import sqlite3

query1 = """
        SELECT * FROM person p         
        """

query2 = """
        SELECT * FROM record r 
        """

query3 = """
        SELECT person.first_name, person.last_name, record.first_phone, record.second_phone
        FROM record
        JOIN person ON record.person_id = person.id        
        """

query4 = """
        SELECT person.first_name, person.last_name, record.first_phone, record.second_phone, record.email, record.birthday, record.address
        FROM record
        JOIN person ON record.person_id = person.id        
        """


def get_person():
    with sqlite3.connect("contact_book.db") as con:
        cur = con.cursor()
        result = cur.execute(query1)
    for rec in result:
        print(rec)
    print("********************")
        


def get_record():
    with sqlite3.connect("contact_book.db") as con:
        cur = con.cursor()
        result = cur.execute(query2)
    for rec in result:
        print(rec)
    print("********************")
    

def get_phone():
    with sqlite3.connect("contact_book.db") as con:
        cur = con.cursor()
        result = cur.execute(query3)

    for rec in result:
        print(rec)
    print("********************")


def get_all_info():
    with sqlite3.connect("contact_book.db") as con:
        cur = con.cursor()
        result = cur.execute(query4)

    for rec in result:
        print(rec)
    print("********************")
    
if __name__ == '__main__':
    get_person()
    get_record()
    get_phone()
    get_all_info()
