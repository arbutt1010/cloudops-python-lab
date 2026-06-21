# ==========================================================
#  PYTHON CONDITIONS — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise where it says "# YOUR CODE HERE".
# Then run this file to test yourself:
#
#       python practice.py
#
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Pass or fail
# ----------------------------------------------------------
# If marks are 50 or more, print "Pass". Otherwise "Fail".
marks = 63

# YOUR CODE HERE
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# ----------------------------------------------------------
# EXERCISE 2: Positive, negative, or zero
# ----------------------------------------------------------
# Use if / elif / else to print whether the number is
# "Positive", "Negative", or "Zero".
number = 1

# YOUR CODE HERE
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ----------------------------------------------------------
# EXERCISE 3: Grade calculator
# ----------------------------------------------------------
# Print a grade based on the score:
#   90+  -> "A"      80-89 -> "B"
#   70-79 -> "C"     below 70 -> "F"
score = 90

# YOUR CODE HERE
if score >= 90:
    print("A")
elif score >= 80 and score <= 90:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
else:
    print("Your are Fail: F")

# ----------------------------------------------------------
# EXERCISE 4: Can they vote AND drive?
# ----------------------------------------------------------
# A person can vote if age >= 18.
# Use 'and' to print "Can vote and drive" only if age >= 18
# AND has_license is True. Otherwise print "Not yet".
age = 18
has_license = True

# YOUR CODE HERE
if age >= 18:
    print("Can vote and drive")
else:
    print("Not yet")


# ----------------------------------------------------------
# EXERCISE 5: Weekend check
# ----------------------------------------------------------
# Using 'or', print "It's the weekend!" if the day is
# "Saturday" OR "Sunday". Otherwise print "It's a weekday".
day = "Monday"

# YOUR CODE HERE
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else :
    print("It's a weekday")



# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): FizzBuzz
# ----------------------------------------------------------
# Loop through numbers 1 to 15. For each number:
#   - if divisible by BOTH 3 and 5 -> print "FizzBuzz"
#   - else if divisible by 3       -> print "Fizz"
#   - else if divisible by 5       -> print "Buzz"
#   - otherwise                    -> print the number
# Hint: check the "both" case FIRST! Order matters.
# (This is a famous classic interview question.)

# YOUR CODE HERE
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("##################3")
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# if marks >= 50:
#     print("Pass")
# else:
#     print("Fail")
#
# --- Exercise 2 ---
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")
#
# --- Exercise 3 ---
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")
#
# --- Exercise 4 ---
# if age >= 18 and has_license:
#     print("Can vote and drive")
# else:
#     print("Not yet")
#
# --- Exercise 5 ---
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday")
#
# --- Exercise 6 ---
# for n in range(1, 16):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)
# ==========================================================
