import pandas as pd

#Data cleaning helps with just fixing data that is not good 

df = pd.read_csv("data.csv")

#1. drop missing columns
#  df = df.drop(columns=["Legendary", "No"])

#2. handle missing data
#  df = df.dropna(subset=["Type2"])
#  df = df.fillna({"Type2": "None"})

#3. Fix inconsistant values

"""
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire" : "FIRE",
                                   "Water" : "WATER"
                                   })
"""

#4. Standarize text 
# df["Name"] = df["Name"].str.lower()      

#5. Fix Data Types
# df["Legendary"] = df["Legendary"].astype(bool)

#6. Drop Dups
df = df.drop_duplicates()


print(df.to_string())

