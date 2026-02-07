import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE Employees(
               EMPLOYEEID INTEGER PRIMARY KEY,
               EMPLOYEENAME TEXT,
               DEPARTMENT TEXT,
               SALARY INTEGER
)
''')
employees=[
    (1,'SANJAY','IT',35000),
    (2,'RAHUL','HR',50000),
    (3,'KARAN','FINANCE',45000),
    (4,'WASIM','IT',40000),
    (5,'RAMUSH','HR',25000),
    (6,'AJAY','FINANCE',42000),
    (7,'PRIYA','IT',48000)
]

cursor.executemany('INSERT INTO EMPLOYEES VALUES (?,?,?,?)', employees)
conn.commit()

print("All Employees:")
cursor.execute("SELECT * FROM Employees")
for row in cursor.fetchall():
    print(row)
cursor.execute('SELECT MIN(Salary) AS MinSalary, MAX(Salary) AS MaxSalary FROM Employees')
result=cursor.fetchone()
print("\nMin Salary:", result[0])
print("Max Salary:", result[1])

print("\nEmployees in IT Department:")
cursor.execute("SELECT * FROM Employees WHERE DEPARTMENT='IT'")
for row in cursor.fetchall():
    print(row)
conn.close()
