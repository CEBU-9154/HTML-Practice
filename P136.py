import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("USA_Housing.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)
#print(sns.heatmap(df.corr(), annot=True))