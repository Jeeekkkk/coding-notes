import os
import requests
import pandas
import sys

# Variables
base_url = "https://api.example.com/"
endpoint = "target/endpoint"
API_TOKEN = os.getenv("TOKEN_NAME")
headers = {
    "Authorization": f"token {API_TOKEN}" # Authentication
    ,"Accept": "api_version" # API Versioning
    ,"User-Agent": "app_name" # Client Identifier
}

# Test for token presence
if not API_TOKEN:
    print("Error: API token not found.")
    sys.exit()

# API Caller
def fetch_data(base_url, endpoint, headers):
    try:
        response = requests.get(base_url+endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit()

# Normalize data
def normalize_data(data):
    dataframe = pandas.json_normalize(data, sep="_")
    # test
    if dataframe.empty:
        print("Error: No data to write")
        sys.exit()
    return dataframe

# Save to CSV
def save_to_csv(df,filename="api_csv_export.csv"):
    # write
    return df.to_csv(filename,index=False)

# Save to Excel
def save_to_excel(df,filename="api_csv_export.xlsx"):
    # write
    return df.to_excel(filename, index=False)

# Write to DB
def save_to_db(df,filename="api_csv_export.db"):
    return df.to_db(filename, index=False)

# Execute
if __name__ == "__main__":
    raw_data = fetch_data(base_url, endpoint, headers)
    dataframe = normalize_data(raw_data)
    save_to_csv(dataframe, filename="example_filename.csv") # filename here overwrites the default defined in the function. Use var filename for default
    #save_to_csv(data, "example_filename.xlsx") # filename here overwrites the default defined in the function. Use var filename for default
    #save_to_db((data, filename="example_filename.db") # filename here overwrites the default defined in the function. Use var filename for default)
    print(f"Data written successfully")

