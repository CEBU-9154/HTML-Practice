import pandas as pd
df=pd.read_csv("students_data.csv")

print("Null values in each column:",df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Marks"]=df["Marks"].fillna(df["Marks"].median())
df["City"]=df["City"].fillna(df["City"].mode()[0])

print("\nAfter handling null values:")
print(df.isnull().sum())