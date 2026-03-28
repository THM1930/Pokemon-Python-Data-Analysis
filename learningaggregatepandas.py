import pandas as pd

#Aggregate functions helps summarize and analyze data

df = pd.read_csv("data.csv")

# Whole Dataframe

"""
mean function = print(df.mean(numeric_only=True))
sum function = print(df.sum(numeric_only=True))
minimum function = print(df.min(numeric_only=True))
maximum function = print(df.max(numeric_only=True))
count function = print(df.count())
"""

# Single Column 

"""

print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())

"""

# Groupby Functions

"""
group = df.groupby("Type1")


print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())
"""
