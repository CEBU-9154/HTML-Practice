import pandas
import pandas as pd
mydataset={
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3,7,2]
}

myvar= pandas.DataFrame(mydataset)
print(myvar,"\n")

a=[1,7,2]
myVar=pd.Series(a,index=['x','y','z'])
Myvar=pd.Series(a)
print(Myvar, myVar,"\n")

cals={'day1':420, 'day2': 380, 'day3':390}
MyVar=pd.Series(cals)
print(MyVar,"\n")

data={
    "calories": [420,380,390],
    "duration": [50,40,45]
}
my_var=pd.DataFrame(data)
print(my_var)
print(my_var.loc[0])
df=pd.DataFrame(data, index=["day1","day2","day3"])
print(df)

