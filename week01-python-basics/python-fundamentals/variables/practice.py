# ==========================================================
#  PYTHON VARIABLES — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise by writing your code where it says
# "# YOUR CODE HERE". Then run this file to test yourself:
#
#       python practice.py
#
# Tip: Do them one at a time. Uncomment a print to check
#      your answer, then move to the next one.
#
# (Solutions are at the very bottom of this file — try first!)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Create your profile
# ----------------------------------------------------------
# Create 3 variables:
#   - your_name  -> your name as a string
#   - your_age   -> your age as an integer
#   - your_city  -> your city as a string
# Then print all three on one line.

# YOUR CODE HERE
your_name = "Abdul"
your_age = 32
your_city = "Rawalpindi"

print(your_name, your_age, your_city)

# ----------------------------------------------------------
# EXERCISE 2: Rectangle area
# ----------------------------------------------------------
# A rectangle has a width of 8 and a height of 5.
# Store them in variables, calculate the area (width * height),
# store it in a variable called 'area', and print it.
# Expected answer: 40

# YOUR CODE HERE
width = 8
height = 5
area = width * height
print(area)


# ----------------------------------------------------------
# EXERCISE 3: Swap the values
# ----------------------------------------------------------
# These two variables are given. Swap them so that
# 'first' becomes "banana" and 'second' becomes "apple".
first = "apple"
second = "banana"

# YOUR CODE HERE
first = "banana"
second = "apple"
# print(first, second)   # should print: banana apple
print(first, second)


# ----------------------------------------------------------
# EXERCISE 4: Build a sentence with an f-string
# ----------------------------------------------------------
# Given the variables below, use an f-string to print:
#   "I have 3 cats and 2 dogs."
cats = 3
dogs = 2

# YOUR CODE HERE
print(f"I have {cats} cats and {dogs} dogs.")


# ----------------------------------------------------------
# EXERCISE 5: Shopping total
# ----------------------------------------------------------
# You buy 4 notebooks at 25 each and 2 pens at 10 each.
# Use variables to calculate the total cost and print it.
# Expected answer: 120

# YOUR CODE HERE
notebooks = 25
pens = 10
note_qnty = 4
pen_qnty = 2

total_cost_notebooks = notebooks * note_qnty
total_cost_pens = pens * pen_qnty

total = total_cost_pens + total_cost_notebooks

print("The total cost of both object is", total)


# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Check the type
# ----------------------------------------------------------
# Create a variable 'temperature' equal to 36.6
# Print its value AND its type using type().
# What type is it? (int or float?)

# YOUR CODE HERE

temperature = 36.6
type = type(temperature)
print(f"The temperature is {temperature} and it's type is {type}")


# ==========================================================
#  SOLUTIONS  (scroll up and try first! No peeking 😄)
# ==========================================================
# To check a solution, remove the # at the start of each line.
#
# --- Exercise 1 ---
# your_name = "Abdul"
# your_age = 25
# your_city = "Lahore"
# print(your_name, your_age, your_city)
#
# --- Exercise 2 ---
# width = 8
# height = 5
# area = width * height
# print(area)
#
# --- Exercise 3 ---
# first, second = second, first
# print(first, second)
#
# --- Exercise 4 ---
# print(f"I have {cats} cats and {dogs} dogs.")
#
# --- Exercise 5 ---
# notebooks = 4 * 25
# pens = 2 * 10
# total = notebooks + pens
# print(total)
#
# --- Exercise 6 ---
# temperature = 36.6
# print(temperature, type(temperature))   # it's a float
# ==========================================================
