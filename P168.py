import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=iris.target
df['species']=df['species'].map({0:'setosa',1:'versicolor',2:'virginica'})
print(df.head())
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Iris Features")
plt.show()
plt.figure()
sns.scatterplot(x='sepal length(cm)',y='petal length (cm)',hue='species',data=df)
plt.title("Scatter Plot")
plt.show()