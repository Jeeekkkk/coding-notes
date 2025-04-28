# --------------------------------------------------------------------------------------------------------------------------------
#                                                         CLASSES
# --------------------------------------------------------------------------------------------------------------------------------

# Object-Oriented Programming (OOP)
    # A way to structure code around real-world objects.
    # Classes are templates for creating objects.

# Defining a Class
class Dog:
    pass

# Tricks and Tips
    # Use capitalized names for classes (PascalCase).
    # Use 'pass' when you need an empty class temporarily.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      INSTANTIATION
# --------------------------------------------------------------------------------------------------------------------------------

# Creating an Instance
my_dog = Dog()

# Tricks and Tips
    # Each instance is independent but shares the class structure.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      ATTRIBUTES
# --------------------------------------------------------------------------------------------------------------------------------

# Attributes
    # Variables that belong to an object.

# Adding Attributes During Instantiation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create Instance with Attributes
my_dog = Dog("Buddy", 5)

# Accessing Attributes
print(my_dog.name)
print(my_dog.age)

# Tricks and Tips
    # self refers to the specific instance.
    # Attributes are defined in __init__ and accessed through instances.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                       METHODS
# --------------------------------------------------------------------------------------------------------------------------------

# Methods
    # Functions that belong to an object.

# Defining a Method
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Calling a Method
my_dog = Dog("Buddy")
print(my_dog.bark())

# Tricks and Tips
    # Always include 'self' as the first parameter in methods.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                  CLASS VS INSTANCE ATTRIBUTES
# --------------------------------------------------------------------------------------------------------------------------------

# Class Attribute (Shared Across All Instances)
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name          # Instance attribute

# Accessing Class Attribute
print(Dog.species)
print(my_dog.species)

# Tricks and Tips
    # Changing a class attribute affects all instances.
    # Changing an instance attribute affects only that instance.

# --------------------------------------------------------------------------------------------------------------------------------
#                                                      SPECIAL METHODS
# --------------------------------------------------------------------------------------------------------------------------------

# Special (Dunder) Methods
    # __init__, __str__, __repr__, etc.

# Example: __str__ Method
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog named {self.name}"

# Now print(my_dog) will print a friendly message instead of an object location.

# Tricks and Tips
    # __str__ should return a readable description.
    # __repr__ should return a more detailed, developer-focused string.