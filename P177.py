import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

labels = ['Math', 'Science', 'English', 'History']
sizes = [60, 43, 29, 17]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Subject Distribution')
plt.show()

data = {
    'Date': pd.date_range(start='2025-01-01', periods=5),
    'Sales': [100, 120, 90, 140, 160]
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

df.plot()
plt.title('Over Time Sales')
plt.show()

df=pd.read_csv('Weather Dataset.csv')
print(df.head())
df_group=df.groupby('month').mean(numeric_only=True)
df_group = df_group.reset_index()

plt.plot(df['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading Number over Time')