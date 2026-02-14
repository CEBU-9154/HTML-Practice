import sqlite3
import pandas as pd
conn=sqlite3.connect('database.sqlite')
print("opened data successfully")
conn.execute("""DROP TABLE CLASS_10;""")
conn.execute('''CREATE TABLE CLASS_10
             (SNO INT PRIMARY KEY NOT NULL,
             ROLL_NO INT NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT DEFAULT (15),
             GENDER TEXT NOT NULL,
             EMAIL_ID TEXT NOT NULL,
             CONTACT_NO REAL NOT NULL);''')
print("Table created successfully")
conn.execute("INSERT INTO CLASS_10 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
             VALUES (1,1, 'ALLEN', 14, 'MALE','alen@gmail.com', 8080900)")
conn.execute("INSERT INTO CLASS_10 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
             VALUES (2,2, 'AISHA', 14, 'FEMALE','aish@gmail.com', 9080900)")
conn.execute("INSERT INTO CLASS_10 (SNO,ROLL_NO,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
             VALUES (3,3, 'JEFF', 15, 'MALE','jeff@gmail.com', 9900900)");
conn.commit()
print("Records created successfully")
tables=pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""",conn)
print(tables)
class_10d=pd.read_sql("""SELECT * FROM CLASS_10;""",conn)
class_10d.head()