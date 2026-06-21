# ==========================================================
#  PYTHON STRINGS — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise by writing your code where it says
# "# YOUR CODE HERE". Then run this file to test yourself:
#
#       python practice.py
#
# Tip: Do them one at a time. Run the file after each one.
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Make a greeting
# ----------------------------------------------------------
# Create a variable 'city' with your city name.
# Use an f-string to print: "Welcome to <city>!"
# Example output: Welcome to Rawalpindi!

# YOUR CODE HERE
city = "Rawalpindi"
print(f"Welcome to {city}!")


# ----------------------------------------------------------
# EXERCISE 2: Shout it out
# ----------------------------------------------------------
# Given the word below, print it in ALL CAPITAL letters.
word = "python"

# YOUR CODE HERE
print(word.upper())


# ----------------------------------------------------------
# EXERCISE 3: First and last character
# ----------------------------------------------------------
# Given the name below, print ONLY the first character,
# then ONLY the last character (use indexing).
name = "Abdul"
# Hint: name[0]  and  name[-1]

# YOUR CODE HERE
print(name[0] + " and " + name[-1])


# ----------------------------------------------------------
# EXERCISE 4: Clean up the text
# ----------------------------------------------------------
# This string has extra spaces around it.
# Use .strip() to remove them, then print the clean text.
messy = "   hello there   "

# YOUR CODE HERE
cleaned = messy.strip()

print(cleaned)


# ----------------------------------------------------------
# EXERCISE 5: Count the letters
# ----------------------------------------------------------
# Print how many characters are in the sentence below
# (use len()), and how many times the letter "a" appears
# (use .count()).
sentence = "banana milkshake"

# YOUR CODE HERE
print(len(sentence))
print(sentence.count("a"))

# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Build a username
# ----------------------------------------------------------
# Given a first and last name, create a username that is:
#   - all lowercase
#   - first name + "." + last name
# Example: "Abdul" + "Rehman"  ->  "abdul.rehman"
first = "Abdul"
last = "Rehman"

# YOUR CODE HERE
username_f = first.lower()
username_l = last.lower()
username = username_f + "." + username_l
print(username)



# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# city = "Rawalpindi"
# print(f"Welcome to {city}!")
#
# --- Exercise 2 ---
# print(word.upper())
#
# --- Exercise 3 ---
# print(name[0])
# print(name[-1])
#
# --- Exercise 4 ---
# print(messy.strip())
#
# --- Exercise 5 ---
# print(len(sentence))
# print(sentence.count("a"))
#
# --- Exercise 6 ---
# username = first.lower() + "." + last.lower()
# print(username)
# ==========================================================
