import pandas as pd
import sqlite3
db='database.sqlite'
conn=sqlite3.connect(db)
print('Opened data successfully.')
tables=pd.read_sql("""SELECT * FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)
matches=pd.read_sql("""SELECT * FROM Match;""", conn)
print(matches.head())
"""**Conclusion-**
-12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
-3 columns with null values
"""

result1=pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner 
                    FROM Match
                    WHERE Season_Id=9
                    GROUP BY Match_Winner
                    ORDER BY AVG(Win_Margin);""", conn)
print(result1)

result2=pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id) 
                    FROM Match
                    WHERE Season_Id=9;""", conn)
print(result2)

result3=pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match)) 
                    FROM Match
                    WHERE Season_Id=9;""", conn)
print(result3)

result4=pd.read_sql("""SELECT SUM(Win_Margin) 
                    FROM Match
                    WHERE Season_Id=9;""", conn)
print(result4)