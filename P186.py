import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    'Age': [22, 25, 47, 35, 46, 28, 30, 19, 40, 50],
    'Salary': [20000, 25000, 50000, 40000, 52000, 30000, 32000, 18000, 45000, 60000],
    'Fare': [7.25, 71.83, 8.05, 53.1, 8.05, 13.0, 7.75, 21.0, 26.0, 30.0]
})

data.hist(bins=5)
plt.show()
sns.boxplot(data=data)
plt.show()