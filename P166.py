import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
data_july={
    'Day':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    'New Births': [12,15,11,9,1,9,21]
}
df_july=pd.DataFrame(data_july)
plt.figure(figsize=(8,5))
plt.bar(df_july['Day'], df_july['New Births'], color='skyblue',width=0.6,edgecolor='navy')

plt.title('Birth Rate Data - July')
plt.xlabel("Day")
plt.ylabel("New Births")
plt.show()

x=list(range(1,51))
y=[random.randint(1,100) for _ in x]

plt.scatter(x,y,c="red")

plt.title("Scatter Plot with More Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
x=list(range(1,51))
y=[i+(i%5)*2 for i in x]
plt.scatter(x,y,c="blue")
plt.title("Scatter Plot with Pattern Data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()