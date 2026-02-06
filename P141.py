import pandas as pd
import sqlite3

db="database.sqlite"

conn=sqlite3.connect(db)
cursor=conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Students(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT NOT NULL,
               AGE INTEGER);
               """)
cursor.execute('INSERT INTO Students (NAME, AGE) VALUES (?,?)', ('ALICE',14))
cursor.execute('INSERT INTO Students (NAME, AGE) VALUES (?,?)', ('BOB',15))

conn.commit()
cursor.execute("SELECT * FROM Students")
rows=cursor.fetchall()
print("Using cursor.fetchall();",rows)
df=pd.read_sql("SELECT * FROM Students", conn)
print("\n Using pandas DataFrame:")
print(df)
conn.close()