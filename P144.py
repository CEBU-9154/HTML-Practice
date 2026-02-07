import sqlite3
database='database.sqlite'
conn=sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables=pd.read_sql("""SELECT * 
                   FROM sqlite_master
                   WHERE type='table';""",conn)
print(tables)
teams=pd.read_sql("""SELECT *
                    FROM Team;""",conn)
print(teams)
MI_wins=pd.read_sql("""SELECT *
                    FROM Match
                    WHERE Match_Winner==7;""",conn)
print(MI_wins)
MI_S8_S9=pd.read_sql("""SELECT *
                     FROM Match
                     WHERE Match_Winner==7 and Season_Id IN (8,9);""",conn)
print(MI_S8_S9)
nt=pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""",conn)
print(nt)

mmm=pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin)
                FROM Match;""",conn)
print(mmm)