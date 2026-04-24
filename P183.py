import pandas as pd
data = {
"Name": ["Asha", "Rahul", "Meena", "Arjun", "Divya", "Kiran", "Sneha", "Vijay"],

"Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],

"Age": [20, 22, 21, 23, 20, 24, 22, 23],

"Marks": [85, 78, 92, 88, 76, 95, 89, 84],

"Department": ["CS", "IT", "CS", "EC", "IT", "CS", "EC", "IT"]
}

df=pd.DataFrame(data)
print(df)
print("Mean Age:",df['Age'].mean())
print('Mean Marks:',df["Marks"].mean())
print("Median Age:",df['Age'].median())
print('Median Marks:',df["Marks"].median())