import pandas as pd
data={"calories":[420,380,390],"duration":[50,45,45]}
#data frame
df=pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df['calories'][0])




