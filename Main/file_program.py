import pandas as pd
import sys
from pathlib import Path

def get_file():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    search_count = 3
    while True:
        csv_file_name=input("Please enter the name of the CSV file (i.e. filename.csv): ").lower().strip()
        try:
            df= pd.read_csv(f"{csv_file_name}", dtype={"Phone Number": str})
            return df
        except FileNotFoundError:
            print("\n❌ File not found! Please make sure your CSV file is in the correct location.")
            search_count-=1
            if search_count <=3:
                print(f"You have {search_count} attempts left! Please try again.")
            elif search_count == 0:
                print(f"You have {search_count} attempts left! Please try again later.")
                sys.exit()

def create_file_path(df_remove_duplicate):
    output_folder=Path("../cleaned_data_exports")
    output_folder.mkdir(parents=True, exist_ok=True)
    df_remove_duplicate.to_csv(output_folder/"cleaned_leads.csv",index=False)
    csv_file_path=output_folder/"cleaned_leads.csv"
    return csv_file_path