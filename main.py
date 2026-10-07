
import pandas as pd

df= pd.read_csv("data_test.csv",dtype={"Phone Number": str})
df["Name"]= df["Name"].str.strip().str.title()
df["Email"]= df["Email"].str.strip().str.lower()

def valid_email():
    email_pattern = r"^[\w\._-]+@+[\w\._-]+\.\w+$"
    if re.fullmatch(email_pattern, df["Email"]):
        return df["Email"]

    else:
        return "\033[32mInvalid Email Format!\033[0m"

original_rows=df.shape[0]
current_rows=df.shape[0]

df_no_empty=df.dropna(how="all")
no_empty_rows =current_rows-df_no_empty.shape[0]
current_rows=df_no_empty.shape[0]

df_blank_email=df_no_empty.dropna(subset=["Email"])
no_blank_emails= current_rows-df_blank_email.shape[0]
current_rows=df_blank_email.shape[0]

df_remove_duplicate= df_blank_email.drop_duplicates()
no_duplicates_rows=current_rows-df_remove_duplicate.shape[0]
current_rows=df_remove_duplicate.shape[0]

print(f"\n{df_remove_duplicate.head()}")

print(f"\n\033[32mOriginal number of Rows:{original_rows}\033[0m")
print(f"\n\033[32mEmpty rows removed: {no_empty_rows}\033[0m")
print(f"\n\033[32mBlank emails removed: {no_blank_emails}\033[0m")
print(f"\n\033[32mDuplicates removed:{no_duplicates_rows}\033[0m")
print(f"\n\033[32mNumber of rows after cleanup:{current_rows}\033[0m")