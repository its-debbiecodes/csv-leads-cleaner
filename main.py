
import pandas as pd

df= pd.read_csv("data_test.csv",dtype={"Phone Number": str})
df["Name"]= df["Name"].str.strip().str.title()
df["Email"]= df["Email"].str.strip().str.lower()
original_rows=df.shape[0]
current_rows=df.shape[0]

df_no_empty=df.dropna(how="all")
no_empty_rows =current_rows-df_no_empty.shape[0]
current_rows=df_no_empty.shape[0]

df_clean=df.dropna(how="all")
after_empty_rows=df_clean.shape[0]

df_email=df_clean.dropna(subset=["Email"])
after_blank_emails=df_email.shape[0]

df_duplicate= df_email.drop_duplicates()
after_duplicates_clean=df_duplicate.shape[0]

print(f"\n\033[32mOriginal number of Rows:{original_rows}\033[0m")
print(f"\n\033[32mEmpty rows removed: {no_empty_rows}\033[0m")
print(f"\n\033[32mBlank emails removed: {no_blank_emails}\033[0m")
print(f"\n\033[32mDuplicates removed:{no_duplicates_rows}\033[0m")
print(f"\n\033[32mNumber of rows after cleanup:{current_rows}\033[0m")