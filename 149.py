import pandas as pd
import numpy as np
import sqlite3
db='database.sqlite'
conn=sqlite3.connect(db)
print("Opened data successfully")
df=pd.read_sql("""SELECT * FROM sqlite_master
               WHERE type='table';""",conn)
print(df)
p_m=pd.read_sql("""SELECT * FROM Player_Match""",conn)
p_m.head()
null_pm=pd.read_sql("""SELECT * FROM Player_Match
               WHERE Team_Id IS NULL""",conn)
print(null_pm)
toss_dec=pd.read_sql("""SELECT * FROM Match""",conn)
toss_dec.head()
n_m=pd.read_sql("""SELECT * FROM Match
               WHERE MATCH_Winner IS NULL""",conn)
print(n_m)