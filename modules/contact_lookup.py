# import pandas as pd

# def get_email(name):
#     df = pd.read_excel("contacts.xlsx")
#     df.columns = df.columns.str.strip()
#     email = df[df['Name'].str.lower() == name.lower()]['Email'].values
#     if len(email):
#         return email[0]
#     else:
#         raise ValueError("Email not found for the name: " + name)


# import pandas as pd

# def get_email(name):
#     df = pd.read_excel("contacts.xlsx")  # Make sure the path is correct
#     df.columns = df.columns.str.strip()  # Remove any extra whitespace from headers
#     email = df[df['Person Name'].str.lower() == name.lower()]['Email Address'].values
#     if len(email):
#         return email[0]
#     else:
#         raise ValueError("Email not found for the name: " + name)



# import pandas as pd

# def get_email(name):
#     df = pd.read_excel("contacts.xlsx")
    
#     # Normalize column names: strip spaces and lowercase
#     df.columns = df.columns.str.strip().str.lower()
    
#     # Now match against cleaned column names
#     email = df[df['name'].str.lower() == name.lower()]['email'].values

#     if len(email):
#         return email[0]
#     else:
#         raise ValueError("Email not found for the name: " + name)


# modules/contact_lookup.py
import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

SHEET_ID = "1Tv6vTnF9xCh7gQQGwb-XSGzULnV_ejgv60KTa6G5Kps"
SHEET_RANGE = "Sheet1!A:B"  # Adjust this if your sheet has a different name or range

def get_email(name):
    print("name is ",name)
    creds = service_account.Credentials.from_service_account_file(
        "/Users/kaushalgadhiya/Projects/Email_Agent/modules/credentials.json",  # Make sure your service account JSON is placed in your project root
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
    values = result.get("values", [])

    if not values:
        raise ValueError("No data found in the Google Sheet")

    df = pd.DataFrame(values[1:], columns=values[0])  # First row as header
    df.columns = df.columns.str.strip()
    print(df)

    if "Name" not in df.columns or "Email" not in df.columns:
        raise KeyError("Make sure your sheet has 'Name' and 'Email' columns")

    # email = df[df["Name"].str.lower() == name.lower()]["Email"].values
    email = df[df["Name"].str.strip().str.lower() == name.strip().lower()]["Email"].values
    
    if len(email):
        return email[0]
    else:
        raise ValueError("Email not found for the name: " + name)
