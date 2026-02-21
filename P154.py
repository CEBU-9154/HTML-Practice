import pandas as pd
import sqlite3

db='database.sqlite'
conn=sqlite3.connect(db)

tables=pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""",conn)
print(tables)
team=pd.read_sql("""SELECT * FROM Team;""",conn)
print(team)
seasons=pd.read_sql("""SELECT * FROM Season;""",conn)
print(seasons)
matches_25=pd.read_sql("""SELECT Match_Id, Team_2 as Away_Team, Toss_Winner, Match_Winner FROM Match WHERE Team_1=(SELECT Team_1 FROM Match WHERE Team_1==3 AND Season_Id==8);""",conn)
print("Matches played: ",matches_25)
csk_wins=pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 3 AND Season_Id == 8""",conn)
print("Matches won by CSK as Home Team in Year 2015", csk_wins)

match_runs=pd.read_sql("""SELECT SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No FROM Batsman_Scored WHERE Total_Runs > 5 AND Match_Id IN (SELECT Match_Id FROM Match WHERE Season_Id == 8);""",conn)
print(match_runs)

avg=pd.read_sql("""SELECT Match_Id, Runs_Scored as Total_Runs, Innings_No 
                FROM Batsman_Scored
                WHERE Innings_No==1 AND Runs_Scored
>
                (SELECT AVG(Runs_Scored) FROM Batsman_Scored);""",conn)
print("Matches with Scored Runs Greater Than Avg Scored Runs: ", avg)