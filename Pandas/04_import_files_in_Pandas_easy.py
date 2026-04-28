import pandas as pd

df = pd.read_csv("data.csv")

# df = pd.read_json("data.json")

# print(df) # truncating display only top 5 and bottom 5

print(df.to_string()) # reads full data