# Accessing Keys
ex_dict["example key"]
    # If key is not found, exception KeyError is returned
ex_dict.get("example key")
    # This is another way that will not produce an exception
    # Returns "N/A" if key not found
# Accessing Nested Keys
ex_dict["example key"]["example nested key"]

    # Accessing Keys: Working with potential missing keys or values
    ex_dict.get("key")
        # If "key" exists → returns its value
        # If "key" is missing → returns None
        ex_dict.get("key", {}))
            # Default value will return if key is missing, in this cas an empty dict
    # Chaining for nested dictionaries
    ex_dict.get("user", {}).get("age")
        # If "user" exists, tries to get "age"
        # If "user" is missing, .get("user", {}) returns an empty dict — so no crash 

# Looping Through Keys and Values
for key in ex_dict:
    print(key)
    # Prints the keys
for value in ex_dict.values():
    print(ex_dict[value])
    # prints the values
for key,value in ex_dict.items():
    print(key,value)
    # prints keys and values

# Store dictionary values in lists
keys = person.keys()
    # prints dict_keys(['name', 'age', 'city'])
values = person.values()
    # prints dict_values(['Alice', 30, 'New York'])
keys_and_values = person.items()
    # prints dict_items([('name', 'Alice'), ...])

# Dictionary Methods
    # Get all keys
keys = customer.keys()
    # Get all values
values = customer.values()
    # Get all key-value pairs
items = customer.items()

# --------------------------------------------------------------------------------------------------------------------------------

#                                       MODIFYING DICTIONARIES
# Adding or Changing Values
person["age"] = 31
    # Cahnges existing value
    # If this key is not present, it will make a new k:v pair

# Deleting key-value pairs
del person["city"]

# Add or overwrite multiple key-value pairs
my_dict.update({"new_key": 42, "another_key": 99})

# Merge two or more dictionaries
dict_1.update(dict_2)

# Remove a key and return its value
my_dict.pop("key")


# --------------------------------------------------------------------------------------------------------------------------------
# Filtering Flat Dictionaries
flat_dict = {"a": 10, "b": 60, "c": 25}
# TASK: Create a new dictionary with only values greater than 50
new_flat_dict = {}
for key,value in flat_dict.items():
    if value > 50:
        new_flat_dict[key] = value
    
# -------------------------------------------------
# Filtering Dictionaries of Dictionaries
nested_dict = {
    "u1": {"active": True},
    "u2": {"active": False}
}
# TASK: Create a new dictionary with only entries where 'active' is True
new_nested_dict = {}
for key in nested_dict:
    if nested_dict[key]['active'] == True:
        new_nested_dict[key] = nested_dict[key]
        
# -------------------------------------------------
# Filtering a List of Dictionaries
list_of_dicts = [
    {"name": "A", "stars": 50, "fork": False},
    {"name": "B", "stars": 5, "fork": True},
    {"name": "C", "stars": 100, "fork": False}
]
# TASK: Create a new list with only repos that have more than 25 stars and are not forks
new_list_of_dicts = []
for dicts in list_of_dicts:
    if dicts["stars"] > 25 and dicts["fork"] == False:
        new_list_of_dicts.append(dicts)
print(new_list_of_dicts)

# -------------------------------------------------
# Working with JSON Objects
import json

json_str = '''
[
    {"id": "x", "archived": false},
    {"id": "y", "archived": true},
    {"id": "z", "archived": false}
]
'''
# TASK: Load this JSON and create a list of items where 'archived' is False
loaded_json_str = json.loads(json_str)
json_str = []
for dicts in loaded_json_str:
    if dicts["archived"] == False:
        json_str.append(dicts)
print(json_str)
