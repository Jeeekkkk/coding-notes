# --------------------------------------------------------------------------------------------------------------------------------
#                                                          BASICS
# --------------------------------------------------------------------------------------------------------------------------------

# Commenting
# - Single line comment: Use # before the comment.
# - Multi-line comment: Use triple quotes (''' or """).

# Common Errors
# - SyntaxError: Incorrect structure or syntax.
# - NameError: Variable or function name not found.
# - TypeError: Wrong data type used in an operation.
# - AttributeError: Object has no such attribute.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         STRINGS
# --------------------------------------------------------------------------------------------------------------------------------

# Creating Strings
# - Single quotes ('') and double quotes ("") are functionally the same.
#   Use whichever helps avoid escaping characters inside the string.
single_quote_string = 'Hello'
double_quote_string = "Hello"

# Multiline Strings
# - Use triple quotes to span text across multiple lines.
multiline_string = '''This is a
multiline string.'''

# Escape Characters
# - Use \ to include special characters inside a string.
string_with_apostrophe = 'I can\'t'
string_with_quote = "She said, \"Hello\""
new_line = "First line\nSecond line"
tabbed_text = "Column1\tColumn2"

# Combining Strings and Variables
name = "Jake"
welcome_message = "Hello, " + name

# String Methods
text = " hello world! "
uppercase = text.upper()          # Converts to uppercase
lowercase = text.lower()          # Converts to lowercase
titlecase = text.title()          # Converts to title case
split_text = text.split()         # Splits on spaces
split_custom = text.split('o')    # Splits at every 'o'
joined_text = '-'.join(['Hello', 'World']) # Joins with '-'
stripped_text = text.strip()       # Removes spaces at start/end
replaced_text = text.replace("world", "there")
found_index = text.find("world")  # Returns index of substring

# String Formatting
formatted_text = "Hello, {}!".format(name)
formatted_text_named = "Hello, {user}!".format(user=name)

# --------------------------------------------------------------------------------------------------------------------------------
#                                                          NUMBERS
# --------------------------------------------------------------------------------------------------------------------------------

# Types of Numbers
# - int: Whole numbers
# - float: Numbers with decimals
integer_num = 5
float_num = 5.0
negative_float = -2.75

# Special Floats
infinite_num = float("inf")
negative_infinite_num = float("-inf")

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         INDEXING
# --------------------------------------------------------------------------------------------------------------------------------

# Standard Indexing (left to right)
# - Index starts at 0.
text = "Python"
first_letter = text[0]    # 'P'
third_letter = text[2]    # 't'

# Reverse Indexing (right to left)
# - Index starts at -1.
last_letter = text[-1]    # 'n'
second_last = text[-2]    # 'o'

# Slicing
slice_text = text[1:4]    # 'yth'

# Slice Syntax
# - [start:stop:step]
# - start: where slice begins (inclusive)
# - stop: where slice ends (exclusive)
# - step: interval between indices

# Examples
skip_letters = text[::2]  # 'Pto' (every second letter)
reverse_text = text[::-1] # 'nohtyP' (reverses the string)