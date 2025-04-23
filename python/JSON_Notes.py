# Load JSON via URL
import requests

url = "https://api.example.com/data"
response = requests.get(url)
json_data = response.json()  # Automatically parses the JSON into a Python object

print(type(json_data))  # Could be a dict or a list, depending on the structure
# --------------------------------------------------------------------------------------------------------------------------------

# Load JSON via String
import json

json_str = '''
[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]
'''
loaded_json_str = json.loads(json_str)  # Converts JSON string to Python object
# --------------------------------------------------------------------------------------------------------------------------------

# Load JSON via File
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Converts file contents to Python object
