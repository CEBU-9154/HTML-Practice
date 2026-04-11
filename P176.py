import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("FuelConsumption.csv")
data.head()
data.isnull().any()
data.info()

sns.set_style('white')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('dark')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('ticks')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('white')
sns.countplot(x=data['FUELTYPE'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['FUELTYPE'],palette='winter',legend=False)
plt.show()

sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['FUELTYPE'],color='Purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['FUELTYPE'],color='Red')
plt.show()

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['FUELTYPE'],color='Cyan')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['FUELTYPE'],color='Orange')
plt.xticks(rotation=45)
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['FUELTYPE'],color='Green')
plt.xticks(rotation=45)
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster",font_scale=0.8)
sns.countplot(x=data['FUELTYPE'],color='Blue')
plt.xticks(rotation=45)
plt.show()