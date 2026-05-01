import pandas as pd

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work dne with Pandas is data cleaning


df = pd.read_csv("data.csv")


#------------------ 1. Drop irrelevant columns----------------
# df = df.drop(columns=["Legendary", "No"])

#------------------------ 2. Handle missing data-------------------
# df = df.dropna(subset = ["Type2"])
# df = df.fillna({"Type2": "None"})

#------------------------ 3. Fix inconsistent values-------------------
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                     "Water": "WATER",
#                                     "Fire": "FIRE"})

#------------------------ 4. Standardize text-------------------
# df["Name"] = df["Name"].str.lower()

#------------------------ 5. Fix DataTypes-------------------
# df["Legendary"] = df["Legendary"].astype(bool)

#------------------------ 6. Remove Duplicates-------------------
df = df.drop_duplicates()



print(df.to_string())