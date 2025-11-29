import pandas as pd
import numpy as np

exam_data={'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Micheal', 'Matthew', 'Laura', 'Jonas'],
           'score': [12.5, 9, 16.5, np.nan, 9, 20, 24.5, np.nan, 8],
           'attempts': [1,3,2,4,2,4,1,1,2],
           'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no']}
labels=['a','b','c','d','e','f','h','i', 'j']

df=pd.DataFrame(exam_data, index=labels)
print("Summary of the basic information about this DataFramw and its data: ")
print(df.info())