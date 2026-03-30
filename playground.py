import pandas as pd

# Load the website leads data from a CSV file into a DataFrame
df = pd.read_csv("website_leads.csv")

# Fill missing Age values with a default value of 25
df["Age"] = df["Age"].fillna(25)

# Fill missing Email values with a placeholder string
df["Email"] = df["Email"].fillna("pending verification")

# Remove rows where Device_Type is null and store in a new DataFrame
df2 = df.dropna(subset=["Device_Type"])

# Remove duplicate rows and store in a new DataFrame
df3 = df.drop_duplicates()

# Display the cleaned DataFrame
print(df)
