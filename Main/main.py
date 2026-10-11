
from clean_process import data_clean_up
from file_program import create_file_path,get_file
def main():
    df=get_file()
    current_rows,original_rows, no_empty_rows, no_blank_emails, no_duplicates_rows,df_invalid_emails,df_valid_emails,percentage_of_valid_leads, total_rows_removed,df_remove_duplicate=data_clean_up(df)
    csv_file_path= create_file_path(df_remove_duplicate)


    print(f""" 
    \n====== CLEANED UP LEADS ===================================================
    \n✓ Cleaning complete!                                                       
    \n\033[32mClean Leads:\033[0m {current_rows}                               
    \nSaved to: {csv_file_path}                                                  
    \n===========================================================================
    \n{df_remove_duplicate.head(10)}                                           
    \n===========================================================================
    """)

    print(f"""
    ====== LEAD LIST CLEANING REPORT ======
    \033[32mOriginal Rows:\033[0m {original_rows}
    \033[32mEmpty rows removed:\033[0m {no_empty_rows}
    \033[32mBlank emails removed:\033[0m {no_blank_emails}
    \033[32mDuplicates removed:\033[0m {no_duplicates_rows}
    \033[32mInvalid Emails:\033[0m {df_invalid_emails}
    \033[32mValid Emails:\033[0m {df_valid_emails}
    \033[32mPercentage of valid leads:\033[0m {percentage_of_valid_leads:.2f}%
    \033[32mTotal rows removed:\033[0m {total_rows_removed}
    \033[32mClean Leads:\033[0m {current_rows}
    =====================================================================
    """)

if __name__ == "__main__":
    main()