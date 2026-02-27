import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("country_vaccinations.csv")
df.head(10)
df.isnull().any()

ss=df.iloc[:5200, :]
plt.figure(figsize=(12,8))
sns.heatmap(ss.isnull(), cbar=False, cmap="viridis")
plt.show()

print(df.head(10))
print(df.dropna(how="all"))
print(df.fillna(method="bfill"))
print(df.interpolate)

df_dropped=df.dropna
print(df_dropped)