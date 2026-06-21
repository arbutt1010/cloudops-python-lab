# ==========================================================
#  PYTHON LISTS — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise where it says "# YOUR CODE HERE".
# Then run this file to test yourself:
#
#       python practice.py
#
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Make a list
# ----------------------------------------------------------
# Create a list called 'hobbies' with 3 hobbies you enjoy.
# Print the whole list, then print how many hobbies it has
# using len().

# YOUR CODE HERE
hobbies = ["Traveling", "Snooker", "Coding"]
print(hobbies)
print(len(hobbies))


# ----------------------------------------------------------
# EXERCISE 2: First and last
# ----------------------------------------------------------
# Given the list below, print ONLY the first city and
# ONLY the last city (use indexing).
cities = ["Lahore", "Karachi", "Islamabad", "Rawalpindi"]

# YOUR CODE HERE
print(cities[0], cities[-1])


# ----------------------------------------------------------
# EXERCISE 3: Update the list
# ----------------------------------------------------------
# In the list below, change "green" to "purple",
# then print the updated list.
colors = ["red", "green", "blue"]

# YOUR CODE HERE
colors[1] = "purple"
print(colors)


# ----------------------------------------------------------
# EXERCISE 4: Build a to-do list
# ----------------------------------------------------------
# Start with the list below.
#  - Add "exercise" to the END (append)
#  - Remove "email" from the list (remove)
#  - Print the final list
tasks = ["email", "meeting", "lunch"]

# YOUR CODE HERE
tasks.append("exercise")
tasks.remove("email")
print(tasks)


# ----------------------------------------------------------
# EXERCISE 5: Loop and print
# ----------------------------------------------------------
# Use a for-loop to print each fruit with the word "I like"
# in front of it. Example:  I like apple
fruits = ["apple", "mango", "grapes"]

# YOUR CODE HERE
for fruit in fruits:
    print("I like", fruit)


# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Stats from a list
# ----------------------------------------------------------
# Given the numbers below, print:
#   - the highest number
#   - the lowest number
#   - the total (sum)
#   - the list sorted from low to high
nums = [42, 7, 19, 88, 3, 55]

# YOUR CODE HERE
print(max(nums))
print(min(nums))
print(sum(nums))
nums.sort()
print(nums)



# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# hobbies = ["reading", "cricket", "coding"]
# print(hobbies)
# print(len(hobbies))
#
# --- Exercise 2 ---
# print(cities[0])
# print(cities[-1])
#
# --- Exercise 3 ---
# colors[1] = "purple"
# print(colors)
#
# --- Exercise 4 ---
# tasks.append("exercise")
# tasks.remove("email")
# print(tasks)
#
# --- Exercise 5 ---
# for fruit in fruits:
#     print("I like", fruit)
#
# --- Exercise 6 ---
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# nums.sort()
# print(nums)
# ==========================================================
