import pandas as pd
import matplotlib.pyplot as plt
data = {
'Department': ['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales', 'IT'],

'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male'],

'Salary': [50000, 40000, 52000, 45000, 48000, 47000, 51000]
}
df=pd.DataFrame(data)
print(df)
grouped=df.groupby('Department')['Salary'].mean()
print(grouped)

grouped.plot(kind='bar')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

ax=grouped.plot(kind='bar')
for i,value in enumerate(grouped):
    ax.text(i,value + 500, str(round(value,2)),
            ha='center',fontsize=10)
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()   