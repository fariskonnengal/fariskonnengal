import pandas as pd
df = pd.read_csv('customers-100.csv')
print(df.to_string())
print(df.head(10))
print(df.tail(10))
print(pd.options.display.max_rows)
print(df.info())