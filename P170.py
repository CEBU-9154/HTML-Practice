import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
sns.set(style="whitegrid")
plt.rcParams['figure.figsize']=(10,6)
np.random.seed(42)
data={
    "Age": np.random.randint(18,60,100),
    "Study Hours": np.random.randint(1,10,100),
    "Sleep Hours": np.random.randint(4,9,100),
    "Attendance": np.random.randint(60,100,100),
    }
df=pd.DataFrame(data)
df["Marks"]=(df["Study Hours"]*5+df["Attendance"]*0.5+np.random.randint(-10,10,100))
print(df.head())
corr_matrix=df.corr()
print(corr_matrix)

sns.scatterplot(x="Study Hours",y="Marks",data=df)
plt.title("Stidy Hours vs Marks")
plt.show()

sns.pairplot(df)
plt.show()