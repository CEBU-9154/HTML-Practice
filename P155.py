
import pandas as pd
import sqlite3

conn = sqlite3.connect("data.sqlite")
cursor = conn.cursor()
cursor.execute("""

CREATE TABLE IF NOT EXISTS Student (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Class_Id INTEGER,
Marks INTEGER
);
""")

students_data = [
('Asha', 101, 85),
('Rahul', 102, 78),
('Meera', 101, 92),
('Rohan', 103, 65),
('Sana', 102, 88)
]

cursor.executemany("INSERT INTO Student (Name, Class_Id, Marks) VALUES (?, ?, ?);", students_data)
conn.commit()
students = pd.read_sql("SELECT * FROM Student;", conn)
print("All Students:")
print(students)
high_scores = pd.read_sql("SELECT Name, Marks FROM Student WHERE Marks > 80;", conn)
print("\nStudents scoring above 80:")
print(high_scores)
topper = pd.read_sql("""
SELECT Name, Marks
FROM Student
WHERE Marks = (SELECT MAX(Marks) FROM Student);
""", conn)
print("\nTopper:")
print(topper)
conn.close()