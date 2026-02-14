import sqlite3
import pandas as pd
conn=sqlite3.connect('database.sqlite')
print("opened data successfully")
conn.execute("DROP TABLE ID;")
conn.execute('''CREATE TABLE ID
             (NUM TEXT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             GENDER TEXT NOT NULL,
             EMAIL_ID TEXT NOT NULL,
             CONTACT_NO REAL NOT NULL);''')
print("Table created successfully")
conn.execute("INSERT INTO ID (NUM,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) VALUES (1, 'AIZEN', 14, 'MALE','aizen@gmail.com', 8080900)")
conn.commit()
print("ID created successfully")
tables=pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""",conn)
print(tables)
class_10d=pd.read_sql("""SELECT * FROM ID""",conn)
class_10d.head()