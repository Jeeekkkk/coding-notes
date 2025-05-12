# JSON
import json
with open("json_scratch.json,"w") as f:
    json.dump(data,f,indent=2)

# # Starts with raw API response and normalizes data
    # Normalize data
def normalize_data(api_response):
    dataframe = pandas.json_normalize(data)
    # test
    if dataframe.empty:
        print("Error: No data to write")
        sys.exit()

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