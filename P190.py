import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('Titanic Dataset.csv')
data.head(5)

num_data=data.drop(['Name','Ticket','Cabin','Embarked','Gender'],axis=1)
labels=['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']

for l in labels:
    plt.boxplot(num_data[l])
    print("Distribution of",l)
    plt.show()

from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
num_data=scalar.fit_transform(num_data)