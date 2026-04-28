import pandas as pd

data = {"Name": ["Marco", "Lockie", "Arshdeep"],
        "Age": [29 , 28, 33],
        "Job": ["Left Arm Bowler", "Right Arm Bowler", "Left Arm Bowler"]}


df = pd.DataFrame(data, index = [74, 37,2])


df["Nationality"] = ["SA", "NZ", "IND"]

#new row

new_row = pd.DataFrame([{"Name": "Stoinis",
                         "Age": 34,
                         "Job": "Allrounder"}],
                         index = [38])


df = pd.concat([df,new_row])
print(df)