import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('iris')
categories=['setosa','viginica','versicolor']
data['flower_num']=pd.Categorical(data['species'],categories,ordered=True)
median_value=np.median(data['flower_num'].cat.codes)
median_text=categories[int(median_value)]
print("Median Value of Species -",median_text)

print("Frequency of each category of Species feature")
print(data['species'].value_counts())

sns.countplot(data['flower_num'],order=data['flower_num'].value_counts().index,palette='winter')