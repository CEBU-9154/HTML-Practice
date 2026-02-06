import sqlite3

connect=sqlite3.connect("company.db")
cursor=connect.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS EMPLOYEE (
               EMP_ID INTEGER PRIMARY KEY,
               EMP_NAME TEXT NOT NULL,
               DEPARTMENT TEXT,
               SALARY REAL);
               """)
print("Employee table created successfully.")
cursor.execute("INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME,"
"DEPARTMENT,SALARY) VALUES (101, 'AMIT','HR',25000)")
cursor.execute("INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME,"
"DEPARTMENT,SALARY) VALUES (102, 'PRIYA','IT',41000)")
cursor.execute("INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME,"
"DEPARTMENT,SALARY) VALUES (103, 'RAJ','FINANCE',50000)")

connect.commit()
print("Sample employee data inserted. \n")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])
print("\nEmployee Records:")
cursor.execute("SELECT * FROM EMPLOYEE;")
rows=cursor.fetchall()
for row in rows:
    print(row)
connect.close()