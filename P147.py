import sqlite3
conn=sqlite3.connect("school.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
               ID INTEGER PRIMARY KEY,
               NAME TEXT,
               CLASS TEXT,
               MARKS INTEGER,
               CITY TEXT)""")
students_data=[
    (1,"Anu","10A",85,"Chennai"),
    (2,"Bala","10A",78,"Chennai"),
    (3,"Cathy","10B",92,"Madurai"),
]

cursor.executemany("INSERT OR REPLACE INTO STUDENTS VALUES(?,?,?,?,?)", students_data)
print(students_data)
print("Distinct city from students")
cursor.execute("SELECT DISTINCT CITY FROM STUDENTS")
print(cursor.fetchall())
print("Display students ordered by marks (highest first)")
cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC")
print(cursor.fetchall())
print("Find total students in each class")
cursor.execute("SELECT class, COUNT(*) FROM students GROUP BY class")
print(cursor.fetchall())
print("Average marks of students")
cursor.execute("SELECT AVG(MARKS) FROM STUDENTS")
print(cursor.fetchone())
conn.commit()