import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/Users/chrishaellia/HTML-Practice/HTML-Practice/Python/Penguins.csv")

df=sns.load_dataset('penguins')
print(df.head(10))
print(sns.get_dataset_names())
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe().T)
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))
#print(df.corr())
#sns.heatmap(df, cmap='Wistia', annot=True)
df.hist(figsize=(12,8))
plt.show()
df.plot(kind='box', subplots=True, layout=(3,2),sharex=False,sharey=False,figsize=(0,12))
plt.show()
sns.countplot(data=df,x='sex',palette='summer')
plt.show()