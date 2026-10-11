import re
from file_program import pd
def valid_email(email):
    if pd.isna(email) == True:
        return f"\033[31mInvalid!\033[0m"
    else:
        email_pattern = r"^[\w\._-]+@[\w\._-]+\.\w+$"
        if re.fullmatch(email_pattern,email):
            return f"\033[32mValid\033[0m"
        else:
            return f"\033[31mInvalid!\033[0m"

def data_clean_up(df):
    df["Name"] = df["Name"].astype("string").str.strip().str.title()
    df["Email"] = df["Email"].astype("string").str.strip().str.lower()

    df["Email_Status"] = df["Email"].apply(valid_email)
    original_rows = df.shape[0]
    current_rows = df.shape[0]

    df_no_empty = df.dropna(subset=["Name", "Email"], how="all")
    no_empty_rows = current_rows - df_no_empty.shape[0]
    current_rows = df_no_empty.shape[0]

    df_blank_email = df_no_empty.dropna(subset=["Email"])
    no_blank_emails = current_rows - df_blank_email.shape[0]
    current_rows = df_blank_email.shape[0]

    df_remove_duplicate = df_blank_email.drop_duplicates()
    no_duplicates_rows = current_rows - df_remove_duplicate.shape[0]
    current_rows = df_remove_duplicate.shape[0]


    df_invalid_emails = (df_remove_duplicate["Email_Status"] == f"\033[31mInvalid!\033[0m").sum()
    df_valid_emails = (df_remove_duplicate["Email_Status"] == f"\033[32mValid\033[0m").sum()
    total_rows_removed=no_empty_rows+no_blank_emails+no_duplicates_rows

    percentage_of_valid_leads=0
    if current_rows == 0:
        print(f"\033[31mCan't calculate email percentage: no leads remain.\033[0m")
    else:
        percentage_of_valid_leads = df_valid_emails / current_rows * 100
    return current_rows,original_rows, no_empty_rows, no_blank_emails, no_duplicates_rows,df_invalid_emails,df_valid_emails,percentage_of_valid_leads, total_rows_removed,df_remove_duplicate