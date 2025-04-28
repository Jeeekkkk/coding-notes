# --------------------------------------------------------------------------------------------------------------------------------
#                                                      CONTROL FLOW
# --------------------------------------------------------------------------------------------------------------------------------

# Control Flow
    # Code that makes decisions based on conditions.

# Boolean Expressions
    # A statement that is either True or False.
example_true = 5 > 3
example_false = 3 == 7

# Boolean Variables
    # Variables that store True or False.
set_true = True
set_false = False

# Relational Operators
    # == Equal to
    # != Not equal to
    # <  Less than
    # >  Greater than
    # <= Less than or equal to
    # >= Greater than or equal to

# Boolean Operators
    # and: True if both are True
    # or: True if at least one is True
    # not: Reverses True/False

# If, Elif, Else
x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
else:
    print("Smaller")

# Match-Case
    # A cleaner alternative to lots of if-elif-else statements.
    # Matches a value against multiple possible cases.
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"
            # _ is the wildcard, meaning "catch everything else." Like else.

# Try-Except
    # A way to handle errors without crashing your program.
    # If Python hits an error (like dividing by zero, missing file, bad input), it usually stops the program.
    # try-except lets you catch that error and keep running.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Tricks and Tips
    # Use elif instead of multiple ifs for mutually exclusive logic.
    # Match-case is less flexible than if-elif-else but faster to read for simple matching.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         LOOPS
# --------------------------------------------------------------------------------------------------------------------------------

# For Loop
    # Iterate over items in a sequence.
for item in [1, 2, 3]:
    print(item)

# Range in Loops
for i in range(5):
    print(i)

# Break and Continue
for i in range(5):
    if i == 3:
        break    # Exits loop early
    if i == 1:
        continue # Skips current iteration
    print(i)

# While Loop
    # Loopes while the condition is true
x = 0
while x < 5:
    print(x)
    x += 1

# Nested Loops
for i in range(2):
    for j in range(2):
        print(i, j)

# List Comprehensions
squares = [x**2 for x in range(5)]

# Tricks and Tips
    # Use enumerate() to get index and item together:
        # for index, value in enumerate(['a', 'b', 'c']):
        #     print(index, value)
    # Print all loop outputs on the same line:
        # print(item, end=' ')

# --------------------------------------------------------------------------------------------------------------------------------
#                                                        FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------

# Defining Functions
def greet(name):
    return f"Hello, {name}!"

# Calling Functions
greeting = greet("Jake")

# Parameters and Arguments
    # Parameters: Variables in function definition.
        # Placeholder variables, can be reused in other functions
        # Not advised to be the same as your global variables
    # Arguments: Actual values passed to function.

# Default Arguments
def power(num, exponent=2):
    return num ** exponent

# Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with keywords
    # describe_pet(pet_name="Whiskers", animal_type="cat")

# *args and **kwargs
    # *args: Allows any number of positional arguments (tuple).
    # **kwargs: Allows any number of keyword arguments (dict).

def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

# Tricks and Tips
    # Use None as default when the default value would otherwise be a mutable object (like a list):
        # def func(data=None):
        #     if data is None:
        #         data = []
    # Functions can return multiple values as a tuple:
        # def min_and_max(numbers):
        #     return min(numbers), max(numbers)
