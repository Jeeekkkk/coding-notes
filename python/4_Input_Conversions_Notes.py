# --------------------------------------------------------------------------------------------------------------------------------
#                                                          INPUT
# --------------------------------------------------------------------------------------------------------------------------------

# Input
    # Allows user to provide input.
    # Always returns a string.

# Gathering Input
user_input = input("Give us your input: ")

# Cleaning Input
    # Convert to lower case
    user_input_lower = user_input.lower()

    # Convert to upper case
    user_input_upper = user_input.upper()

    # Convert to title case
    user_input_title = user_input.title()

# Tricks and Tips
    # Combine input and cleaning:
        # user_input = input("Enter something: ").strip().lower()
    # Always remember input() returns a string, even if the user types numbers.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                       CONVERSIONS
# --------------------------------------------------------------------------------------------------------------------------------

# Conversions
    # Changing data types.

# String to Integer
num = int("5")    # 5

# String to Float
decimal = float("5.5")    # 5.5

# Integer to String
num_str = str(5)    # "5"

# Float to String
float_str = str(5.5)    # "5.5"

# Tricks and Tips
    # Useful when processing numbers from user input:
        # user_age = int(input("Enter your age: "))
    # Use str() to safely print numbers with text:
        # print("You are " + str(age) + " years old.")
