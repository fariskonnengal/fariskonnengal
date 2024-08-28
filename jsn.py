import pandas as pd
df = pd.read_json('dwsample2-json.json')
print(df.to_string())
print(df.head(10))
print(df.tail(10))
print(df.info())
print(pd.options.display.max_rows)
