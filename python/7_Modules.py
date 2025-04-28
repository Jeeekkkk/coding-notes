# --------------------------------------------------------------------------------------------------------------------------------
#                                                         MODULES
# --------------------------------------------------------------------------------------------------------------------------------

# Modules
    # Files containing Python code that can be imported and used elsewhere.
    # Allows organization, reuse, and separation of code.

# Importing Modules
import math
result = math.sqrt(16)

# Import Specific Object from Module
from math import sqrt
result = sqrt(16)

# Aliasing Modules or Objects
import math as m
result = m.sqrt(16)

from math import sqrt as square_root
result = square_root(16)

# Tricks and Tips
    # Use aliasing to shorten long module names.
    # Only import what you need to avoid clutter.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                    STANDARD LIBRARIES
# --------------------------------------------------------------------------------------------------------------------------------

# Common Built-in Modules
    # math - Mathematical functions
    # random - Random number generation
    # datetime - Work with dates and times
    # os - Interact with operating system
    # sys - Access system-specific parameters
    # json - Handle JSON data

# Example: random module
import random
random_number = random.randint(1, 100)
random_choice = random.choice(["apple", "banana", "cherry"])

# Example: datetime module
import datetime
now = datetime.datetime.now()

# Tricks and Tips
    # The Python Standard Library has documentation online.
    # Learn common modules to avoid reinventing the wheel.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                     THIRD-PARTY MODULES
# --------------------------------------------------------------------------------------------------------------------------------

# Installing Third-Party Modules
    # Use pip to install external libraries.
    # Example: pip install requests

# Example Usage
import requests
response = requests.get("https://api.example.com")

# Tricks and Tips
    # Always install modules inside a virtual environment for project isolation.
        # Reference note "Virtual_Environments.md"

# --------------------------------------------------------------------------------------------------------------------------------
#                                                        CUSTOM MODULES
# --------------------------------------------------------------------------------------------------------------------------------

# Importing Your Own Files as Modules
    # Any .py file can be imported if it's in the same directory or Python path.

# Example
    # File structure:
        # main.py
        # helpers.py

# Inside helpers.py
def greet(name):
    return f"Hello, {name}!"

# Inside main.py
from helpers import greet
message = greet("Jake")
print(message)

# Tricks and Tips
    # Keep custom modules clean and organized by topic.
    # Avoid circular imports (files trying to import each other).