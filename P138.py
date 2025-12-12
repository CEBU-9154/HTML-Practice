import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Example.csv")
print("\nFIRST 5 ROWS OF DATA:")
print(data.head())

print("\nDATA INFO: ")
print(data.info())
numeric_cols=data.select_dtypes(include=['int64', 'float64']).columns
categorical_cols=data.select_dtypes(include=['object']).columns

sns.pairplot(data)
plt.suptitle("Pairplot of Weatjer Dataset", y=1.02)
plt.show()

sns.jointplot(x='humidity', y='temperature',data=data,kind='scatter')
sns.jointplot(x='humidity', y='temperature',data=data,kind='hex')
sns.jointplot(x='humidity', y='temperature',data=data,kind='kde')
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=data[numeric_cols])
plt.title("Boxplot of Numeric Variables")
plt.show()