import pandas as pd
data={"Cool Drinks":["Pepsi","7""up","Sprite"],"cost":[20,30,10]}
#data frame
df=pd.DataFrame(data)
print(df)
print(df.loc[2])
