# ==========================================================
#  PYTHON VARIABLES — A Beginner's Tutorial
# ==========================================================
# A "variable" is a name that stores a value.
# Think of it as a labeled box: the label is the name,
# and the value is what you put inside the box.
#
# Syntax:   variable_name = value
#           (the single "=" means "assign", not "equals")
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: Creating your first variables
# ----------------------------------------------------------
name = "Abdul"          # text   -> called a "string" (str)
age = 25                # whole number -> "integer" (int)
height = 5.9            # decimal number -> "float"
is_student = True       # yes/no value -> "boolean" (bool)

print("Example 1: Basic variables")
print(name, age, height, is_student)
print()  # prints a blank line


# ----------------------------------------------------------
# EXAMPLE 2: Variables can change (they are "variable"!)
# ----------------------------------------------------------
score = 10
print("Example 2: Changing a variable")
print("Start score:", score)

score = 50              # we overwrite the old value
print("New score:  ", score)

score = score + 25      # use the current value to make a new one
print("After bonus:", score)
print()


# ----------------------------------------------------------
# EXAMPLE 3: Using variables in calculations
# ----------------------------------------------------------
price = 100
quantity = 3
total = price * quantity

print("Example 3: Doing math with variables")
print("Total cost:", total)
print()


# ----------------------------------------------------------
# EXAMPLE 4: Combining text variables (string concatenation)
# ----------------------------------------------------------
first_name = "Abdul"
last_name = "Rehman"
full_name = first_name + " " + last_name   # join with a space

print("Example 4: Joining text")
print("Full name:", full_name)

# A cleaner way using an "f-string" (formatted string):
print(f"Hello, {full_name}! You are {age} years old.")
print()


# ----------------------------------------------------------
# EXAMPLE 5: Checking a variable's type
# ----------------------------------------------------------
# Python figures out the type automatically based on the value.
print("Example 5: Checking types with type()")
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Assigning multiple variables at once
# ----------------------------------------------------------
x, y, z = 1, 2, 3        # three variables in one line
a = b = c = 0            # give the same value to several names

print("Example 6: Multiple assignment")
print("x, y, z =", x, y, z)
print("a, b, c =", a, b, c)
