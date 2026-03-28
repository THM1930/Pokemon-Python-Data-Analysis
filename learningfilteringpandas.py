import pandas as pd

df = pd.read_csv("data.csv")

#Filtering = Keeping certains that meet your condition

#tall_pokemon = df[df["Height"] >= 2]
#heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"]]

print(legendary_pokemon)
