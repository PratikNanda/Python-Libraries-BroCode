import pandas as pd

# DataFrames = A tabular structure with rows and columns. (2 - Dimensional)
#              Similar to Excel sheet


data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
        }


# df = pd.DataFrame(data)

        # output with default indexes

        #         Name  Age
        # 0  Spongebob   30
        # 1    Patrick   35
        # 2  Squidward   50


df = pd.DataFrame(data, index = ["employee 1", "employee 2", "employee 3"])

        # output with

        #                 Name  Age
        # employee 1  Spongebob   30
        # employee 2    Patrick   35
        # employee 3  Squidward   50


#locating 

# print(df.loc["employee 2"])
# print(df.iloc[1])



#------------Adding a new column -----------

# number of rows must match with origin data
df["Job"] = ["Cook", "N/A", "Cashier"]


#------------Adding a new row -----------
# new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}])
# new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index = ["employee 4"])             # Indexing 
# df = pd.concat([df,new_row])

#------------Adding a new rows -----------
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index = ["employee 4", "employee 5"])

df = pd.concat([df,new_rows])

        # output

        #                 Name  Age       Job
        # employee 1  Spongebob   30      Cook
        # employee 2    Patrick   35       N/A
        # employee 3  Squidward   50   Cashier
        # employee 4      Sandy   28  Engineer


print(df)