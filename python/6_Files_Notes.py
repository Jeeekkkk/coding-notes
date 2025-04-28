# --------------------------------------------------------------------------------------------------------------------------------
#                                                          FILES
# --------------------------------------------------------------------------------------------------------------------------------

# Files
    # Python allows you to read from and write to file types such as .txt, .csv, .json.
    # Always use context manager (with open) to handle files safely.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      READING TXTs
# --------------------------------------------------------------------------------------------------------------------------------

# Read Entire File
with open("file.txt", "r") as file:
    content = file.read()

# Read Lines Into List
with open("file.txt", "r") as file:
    lines = file.readlines()

# Read Line by Line
with open("file.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

# Tricks and Tips
    # Always close files automatically using with open().
    # read() returns one big string.
    # readlines() returns a list where each line is a separate string.
    # readline() reads only the next line.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                     WRITING TXTs
# --------------------------------------------------------------------------------------------------------------------------------

# Write to File (Overwrites)
with open("file.txt", "w") as file:
    file.write("Hello, world!\n")

# Append to File (Adds to End)
with open("file.txt", "a") as file:
    file.write("Another line.\n")

# Tricks and Tips
    # 'w' mode overwrites existing file contents.
    # 'a' mode adds to the end without deleting current contents.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      READING CSVs
# --------------------------------------------------------------------------------------------------------------------------------

import csv

# Read CSV into Dictionary
with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# Tricks and Tips
    # csv.DictReader turns each row into a dictionary where column names are the keys.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      WRITING CSVs
# --------------------------------------------------------------------------------------------------------------------------------

# Write Dictionary Data to CSV
fieldnames = ["name", "age"]
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

with open("output.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Tricks and Tips
    # Always write header row first with writer.writeheader().
    # newline='' avoids blank lines appearing in Windows.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      READING JSONs
# --------------------------------------------------------------------------------------------------------------------------------

import json

# Load JSON File
with open("data.json", "r") as file:
    data = json.load(file)

# Tricks and Tips
    # JSON format is very similar to Python dictionaries.
    # json.load() parses JSON text into Python objects automatically.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                     WRITING JSONs
# --------------------------------------------------------------------------------------------------------------------------------

# Save Dictionary to JSON File
data = {"name": "Jake", "age": 27}

with open("output.json", "w") as file:
    json.dump(data, file)

# Tricks and Tips
    # json.dump() converts Python dictionaries into JSON format and writes it to a file.
    # Useful for saving data that needs to be reloaded later.
