# ==========================================================
#  PYTHON NUMBERS — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise where it says "# YOUR CODE HERE".
# Then run this file to test yourself:
#
#       python practice.py
#
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Simple calculator
# ----------------------------------------------------------
# Two numbers are given. Print their sum, difference,
# product, and division (one per line).
a = 20
b = 6

# YOUR CODE HERE
print("Sum: ", a + b)
print("Difference: ", a - b)
print("Product: ", a * b)
print("Division: ", a / b)
print("Floor: ", a // b)
print("Exponent: ", a ** b)
print("Modulus: ", a % b)


# ----------------------------------------------------------
# EXERCISE 2: Odd or even?
# ----------------------------------------------------------
# Use the % (remainder) operator to print True if the
# number is even, and False if it is odd.
# Hint:  number % 2 == 0
number = 17

# YOUR CODE HERE
print(number % 2 == 0)

# ----------------------------------------------------------
# EXERCISE 3: Area of a circle
# ----------------------------------------------------------
# Area = pi * radius ** 2   (use 3.14159 for pi)
# Calculate the area for the radius below and print it,
# rounded to 2 decimal places using round().
radius = 7

# YOUR CODE HERE
cal = 3.14159 * radius ** 2
print(round(cal, 2))


# ----------------------------------------------------------
# EXERCISE 4: Fix the type
# ----------------------------------------------------------
# This price arrived as TEXT (a string). Convert it to a
# number, add 10 to it, and print the result.
price_text = "50"

# YOUR CODE HERE
type_convert = int(price_text) + 10
print(type_convert)


# ----------------------------------------------------------
# EXERCISE 5: Split the bill
# ----------------------------------------------------------
# A bill of 1000 is split between 3 friends.
#  - Print how much each pays using normal division (/).
#  - Then use // and % to print the whole amount each pays
#    and how much is left over.
bill = 1000
people = 3

# YOUR CODE HERE
print(bill / people)
print(bill // people)
print(bill % people)

# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Highest, lowest, average
# ----------------------------------------------------------
# Given the test scores below, print the highest score,
# the lowest score, and the average.
# Hint: max(), min(), sum(), and len() all work on a list.
scores = [88, 72, 95, 60, 79]

# YOUR CODE HERE
print(max(scores))
print(min(scores))
print("Sum Score: ",sum(scores))
print("Length Score: ",len(scores))
average_score = sum(scores) / len(scores)
print("Average Scores: ", average_score)
print()



# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
#
# --- Exercise 2 ---
# print(number % 2 == 0)
#
# --- Exercise 3 ---
# area = 3.14159 * radius ** 2
# print(round(area, 2))
#
# --- Exercise 4 ---
# print(int(price_text) + 10)
#
# --- Exercise 5 ---
# print(bill / people)        # 333.333...
# print(bill // people)       # 333  (whole amount each)
# print(bill % people)        # 1    (left over)
#
# --- Exercise 6 ---
# print("Highest:", max(scores))
# print("Lowest: ", min(scores))
# print("Average:", sum(scores) / len(scores))
# ==========================================================
