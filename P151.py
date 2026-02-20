import numpy
import pandas as pd
import sqlite3

db='database.sqlite'
conn=sqlite3.connect(db)
tables=pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table'""", conn)
print(tables)
joined_city=pd.read_sql("""SELECT c.Country_Id, c.Country_Name,ci.City_Name
                        FROM country c
                        INNER JOIN city ci
                        ON c.Country_ID == ci.Country_id""",conn)
print(joined_city)
left_city=pd.read_sql("""SELECT * FROM player LEFT JOIN season ON player.Player_ID==season.Man_of_the_Series""",conn)
print(left_city)
union=pd.read_sql("""SELECT Player_Name FROM player UNION SELECT Team_Name FROM team""",conn)
print(union)