# --------------------------------------------------------------------------------------------------------------------------------
#                                                          LISTS
# --------------------------------------------------------------------------------------------------------------------------------

# Lists
    # Ordered collection of items.
    # Can contain multiple data types, including other lists (nested lists).
    # Lists are mutable (can be changed after creation).

# Creating Lists
empty_list = []
mixed_list = [1, "text", True, 3.14]
nested_list = [[1, 2], [3, 4]]

# Accessing Items
first_item = mixed_list[0]    # 1
last_item = mixed_list[-1]    # 3.14

# Editing Lists
    # Append: Add one item to the end
        mixed_list.append("new")
    # += operator: Add multiple items
        mixed_list += ["another", 99]
    # Insert: Add an item at a specific index
        mixed_list.insert(2, "inserted")
    # Remove: Remove specific value
        mixed_list.remove("text")
    # del: Remove item by index
        del mixed_list[0]
    # Pop: Remove item by index and return it
        popped_item = mixed_list.pop(2)

# Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

# Sorting Lists
numbers = [3, 1, 4, 2]
numbers.sort()               # Ascending order
numbers.sort(reverse=True)    # Descending order

# Slicing Lists
    # Access a range of items
slice_of_list = numbers[1:3]

# Range
range_list = list(range(5))   # [0, 1, 2, 3, 4]
range_list_custom = list(range(2, 6))  # [2, 3, 4, 5]
range_with_step = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]

# Tricks and Tips
    # Reverse a list quickly:
        # reversed_list = list1[::-1]
    # Copy a list safely:
        # list_copy = list1[:]

# --------------------------------------------------------------------------------------------------------------------------------
#                                                        SUBLISTS
# --------------------------------------------------------------------------------------------------------------------------------

# Accessing Nested Lists
first_sublist = nested_list[0]
first_item_in_sublist = nested_list[0][0]

# Modifying Nested Lists
    # When modifying, loop through each level and append accordingly.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                          TUPLES
# --------------------------------------------------------------------------------------------------------------------------------

# Tuples
    # Ordered, immutable collection of items.
    # Use when you want to ensure data cannot be changed.

# Creating Tuples
tuple_example = (1, 2, 3)
single_element_tuple = (4,)

# Accessing Tuples
first_element = tuple_example[0]

# Unpacking Tuples
me = ("Jake", 27, "Male")
name, age, gender = me

# Tricks and Tips
    # Useful for quick swapping:
    # a, b = b, a
