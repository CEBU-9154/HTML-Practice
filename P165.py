import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HouseDF=pd.read_csv('USA_Housing.csv')
HouseDF.head()
HouseDF.info()
sns.pairplot(HouseDF)
plt.figure(figsize=(10,6))
sns.heatmap(HouseDF.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()