import pandas as pd

# Series = 1-Dimensional labelled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-Dimensional)


# data = [100, 102, 104]
# data = [100.1, 102.3, 104.5]
# data = ["A", "B", "C"]

    # ----------Outputs--------------------
    # ➜  Pandas git:(main) ✗ python3 02_Series_in_Pandas_are_easy.py                                                               
    # 0    100
    # 1    102
    # 2    104
    # dtype: int64

    # ➜  Pandas git:(main) ✗ python3 02_Series_in_Pandas_are_easy.py
    # 0    100.1
    # 1    102.3
    # 2    104.5
    # dtype: float64

    # ➜  Pandas git:(main) ✗ python3 02_Series_in_Pandas_are_easy.py
    # 0    A
    # 1    B
    # 2    C
    # dtype: str

# series = pd.Series(data) # defaut indexing
# print(series.loc[2])   # without indexing
# print(series.iloc[2]) # integer indexing


# series = pd.Series(data, index = ["a", "b", "c"])
# series.loc["c"] = 108
# print(series.loc["c"])
# print(series.iloc[2])


#------------Data Filtering ----------

# data = [100, 102, 104, 200, 204]
# series = pd.Series(data, index = ["a", "b", "c" ,"d", "e"])

# print(series)

    # output

    # a    100
    # b    102
    # c    104
    # d    200
    # e    204
    # dtype: int64

# print(series[series >= 200])

    # output
    # d    200
    # e    204
    # dtype: int64

# print(series[series < 200])

    # output
    # a    100
    # b    102
    # c    104
    # dtype: int64



#----------Using Dictionaries --------------------


calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories) # no indexing required because dictionaries does have keys /Labels

# print(series)
    # output
    # Day 1    1750
    # Day 2    2100
    # Day 3    1700
    # dtype: int64

# print(series.loc["Day 3"])

    # output is 1700

# series.loc["Day 3"] += 500 #update value
# print(series.loc["Day 3"])
    # output is 2000


# filtering

# print(series[series > 2000])
    # output 
    # Day 2    2100
    # dtype: int64

print(series[series <= 2000])
    # output
    # Day 1    1750
    # Day 3    1700
    # dtype: int64
