import requests
import sys
import pandas

# json_url = 'https://run.mocky.io/v3/403681b2-00ca-489a-8b47-b54abf8e2283'

# def fetch_data(api_url):
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         print(f"Error: {e}")
#         sys.exit()

# def filter_data(json_data):
#     filtered_data = []
#     for dicts in json_data:
#         if dicts["status"] == 'active' and dicts['score'] >= 80:
#             filtered_data.append(dicts)
#     if not filter_data:
#         print("error: No data to filter")
#         sys.exit()
#     return filtered_data

# def save_to_csv(filtered_json,file_name):
#     normalized_filtered_json = pandas.json_normalize(filtered_json)
#     try:
#         normalized_filtered_json.to_csv(file_name,index=False)
#         print("Success writing file")
#     except Exception as e:
#         print(f"Error: {e}")
#         sys.exit()
    

# if __name__ == "__main__":
#     api_data = fetch_data(json_url)
#     data_filtered = filter_data(api_data)
#     save_to_csv(data_filtered,'testing_script.csv')



data = [
    {
        "user": {"id": "u1", "name": "Alice"},
        "activity": {"type": "login", "success": True}
    },
    {
        "user": {"id": "u2", "name": "Bob"},
        "activity": {"type": "login", "success": False}
    }
]

# Flatten this into a DataFrame using pandas.json_normalize
# Filter for rows where the login success is True
# Print just the user IDs from those rows

def json_normalize(json_data):
    return pandas.json_normalize(data)

def filter_data(normalized_data):
    filtered_data = []
    for dicts in normalized_data:
        if dicts["activity"]["success"] == True:
            print(dicts["user"]["id"])

if __name__ == "__main__":
    normalized_data = json_normalize(data)
    print(normalized_data)
    # filter_data(normalized_data)