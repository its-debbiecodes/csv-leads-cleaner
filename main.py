
import pandas as pd

df= pd.read_csv("data_test.csv",dtype={"Phone Number": str})
df["Name"]= df["Name"].str.strip().str.title()
df["Email"]= df["Email"].str.strip().str.lower()

def valid_email(email):
    if pd.isna(email) == True:
        return "\033[30mInvalid!\033[0m"
    else:
        email_pattern = r"^[\w\._-]+@[\w\._-]+\.\w+$"
        if re.fullmatch(email_pattern,email):
            return "\033[32mValid\033[0m"
        else:
            return "\033[30mInvalid!\033[0m"

df["Email_Status"]= df["Email"].apply(valid_email)

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

output_folder=Path("cleaned_data_exports")
output_folder.mkdir(parents=True, exist_ok=True)
save_csv_file=df_remove_duplicate.to_csv(output_folder/"cleaned_leads.csv",index=False)
print(f""" 
====== CLEANED UP LEADS ======
\n{df_remove_duplicate.head()}
==========================================
""")

print(f"""
====== LEAD LIST CLEANING REPORT ======
\n\033[32mOriginal Rows:\033[0m {original_rows}
\n\033[32mEmpty rows removed:\033[0m {no_empty_rows}
\n\033[32mBlank emails removed:\033[0m {no_blank_emails}
\n\033[32mDuplicates removed:\033[0m {no_duplicates_rows}
\n\033[32mInvalid Emails:\033[0m {df_invalid_emails}
\n\033[32mClean Leads:\033[0m {current_rows}
=====================================================================
""")