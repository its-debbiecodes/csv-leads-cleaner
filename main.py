
import pandas as pd

df= pd.read_csv("data_test.csv",dtype={"Phone Number": str})
df["Name"]= df["Name"].str.strip().str.title()
df["Email"]= df["Email"].str.strip().str.lower()

print("Total number of rows in this file:",df.shape[0])

df_clean=df.dropna(how="all")
after_empty_rows=df_clean.shape[0]

df_email=df_clean.dropna(subset=["Email"])
after_blank_emails=df_email.shape[0]

df_duplicate= df_email.drop_duplicates()
after_duplicates_clean=df_duplicate.shape[0]

print(df_duplicate.head())

print(f"Original number of Rows:{original_rows}")
print(f"Rows after empty rows removed: {after_empty_rows}")
print(f"Rows after blank emails removed: {after_blank_emails}")
print(f"Rows after duplicates removed:{after_duplicates_clean}")