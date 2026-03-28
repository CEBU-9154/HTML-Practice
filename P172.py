import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"]=(10,6)

np.random.seed(42)
data={
    "Age": np.random.randint(18,60,100),
    "StudyHours": np.random.randint(1,10,100),
    "SleepHours": np.random.randint(4,9,100)
}
df=pd.DataFrame(data)

print(df.head())
corr_matrix=df.corr()
print(corr_matrix)

plt.figure(figsize=(10,7))
sns.heatmap(corr_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()