import pandas as pd

# DataFrame is a tabular data structure with rows and column thats 2 dimensional like a excel spreadsheet

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
    }

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

#add a news column
df["Job"] = ["Cook", "N/A", "Cashier"]

#add a new row
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index=["Employee 4", "Employee 5"])
df =pd.concat([df, new_rows])

#print(df.iloc[1])
#print(df.loc["Employee 1"])

print(df)
