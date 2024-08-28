import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
print(df.to_string())

#plotting data set before cleaning
df.plot()
df.plot(kind='scatter',x='Duration',y='Calories')
df.plot(kind='hist',x='Duration',y='Calories')
plt.show()


#Removing duplicates
print(df.duplicated())
df.drop_duplicates(inplace=True)

#replace empty cells with mean,median,mode
x=df['Calories'].median()
df['Calories'].fillna(x,inplace=True)
print(df.to_string())

#fixing wrong data
for x in df.index:
    if df.loc[x,'Duration']>60:
        df.loc[x,'Duration']=60
print(df)

#fixing wrong format data
df.loc[27,'Date']="'2020/12/26'"
print(df)
df.dropna(subset=['Date'],inplace=True)
df['Date']=pd.to_datetime(df['Date'])
print(df.to_string())

#plotting data set after cleaning
df.plot()
plt.show()
df.plot(kind='scatter',x='Duration',y='Calories')
df.plot(kind='hist',x='Duration',y='Calories')
plt.show()