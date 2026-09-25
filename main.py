
import pandas as pd

df= pd.read_csv("data_test.csv",dtype={"Phone Number": str})
df["Name"]= df["Name"].str.strip().str.title()
df["Email"]= df["Email"].str.strip().str.lower()

df_clean=df.dropna(how="all")
df_duplicate= df_clean.drop_duplicates()
print(df_duplicate.head())
