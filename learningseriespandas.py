import pandas as pd

#Series is a pandas 1 dimensional library that can hold any data type, its like a single column in a table

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series[series < 2000])



"""
data = [100,102,104, 200, 202]

series = pd.Series(data, index = ["a", "b", "c", "d", "e"])

print(series[series < 200])
"""