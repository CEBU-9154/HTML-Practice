import numpy
import pandas as pd
import sqlite3

db='database.sqlite'
conn=sqlite3.connect(db)
conn.execute("DROP TABLE students;")
conn.execute("""CREATE TABLE students (
student_id INTEGER PRIMARY KEY,
name TEXT,
class_id INTEGER
);""")
students_data = [
(1, 'Asha', 101),
(2, 'Rahul', 102),
(3, 'Meera', 101),
(4, 'Rohan', 103)
]
conn.execute("DROP TABLE classes;")
conn.execute("""
CREATE TABLE classes (
class_id INTEGER PRIMARY KEY,
class_name TEXT
);""")
conn.executemany("INSERT INTO students VALUES (?, ?, ?);", students_data)
classes_data = [
(101, 'Math'),
(102, 'Science'),
(104, 'English')
]
conn.executemany("INSERT INTO classes VALUES (?, ?);", classes_data)
inner_join = pd.read_sql("""
SELECT s.student_id, s.name, s.class_id, c.class_name
FROM students s
INNER JOIN classes c
ON s.class_id = c.class_id;""", conn)
print("INNER JOIN Result:\n", inner_join)