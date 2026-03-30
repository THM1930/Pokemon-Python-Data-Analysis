import pandas as pd


#Read the csv file
df = pd.read_csv("ad_performance_raw.csv")


#remove dups
df2 = df.drop_duplicates()


#remove empty values for Clicks and replace it with 0
df3 = df.dropna(subset=["Clicks"])
df4 = df.fillna(0)


#show results where the impressions are over 7500
impressions = df[df["Impressions"] > 7500]

print(impressions)
