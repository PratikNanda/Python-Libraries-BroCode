import pandas as pd

# df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col = "Name") # specifying the Index

# print(df)

# SELECTION BY COLUMN
# print(df["Name"])
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())

# print(df[["Name", "Height", "Weight"]])
# print(df[["Name", "Height", "Weight"]].to_string())

# SELECTION BY ROW/S

# print(df.loc[5])
# print(df.loc["Pikachu",["Height", "Weight"]])
# range of rows
# print(df.loc["Charizard":"Blastoise",["Height", "Weight"]])
# print(df.iloc[0:11:2, 0:3])


# User input version

pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} is not found")
