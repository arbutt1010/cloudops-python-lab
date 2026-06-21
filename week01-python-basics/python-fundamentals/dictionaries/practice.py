# ==========================================================
#  PYTHON DICTIONARIES — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise where it says "# YOUR CODE HERE".
# Then run this file to test yourself:
#
#       python practice.py
#
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Make a dictionary
# ----------------------------------------------------------
# Create a dictionary called 'book' with these pairs:
#   title  -> "Python 101"
#   author -> "Abdul"
#   year   -> 2026
# Then print the whole dictionary.

# YOUR CODE HERE
book = {
    "title": "Python 101",
    "author": "Abdul",
    "year": "2026" 
}
print(book)

# ----------------------------------------------------------
# EXERCISE 2: Look up a value
# ----------------------------------------------------------
# Print just the capital of Pakistan from the dictionary
# (access it by its key).
capitals = {"Pakistan": "Islamabad", "Japan": "Tokyo", "Italy": "Rome"}

# YOUR CODE HERE
print(capitals["Pakistan"])


# ----------------------------------------------------------
# EXERCISE 3: Add and update
# ----------------------------------------------------------
# Start with the dictionary below.
#  - Change the price of "milk" to 60
#  - Add a new item "eggs" with price 120
#  - Print the final dictionary
groceries = {"milk": 50, "bread": 40}

# YOUR CODE HERE
groceries["milk"] = 60
groceries["eggs"] = 120
print(groceries)


# ----------------------------------------------------------
# EXERCISE 4: Check and remove
# ----------------------------------------------------------
# Using the dictionary below:
#  - Print True if "math" is a key (use 'in')
#  - Remove "history" from the dictionary (use del)
#  - Print the final dictionary
marks = {"math": 90, "science": 85, "history": 70}

# YOUR CODE HERE
print("math" in marks)
del marks["history"]
print(marks)


# ----------------------------------------------------------
# EXERCISE 5: Loop and print
# ----------------------------------------------------------
# Loop through the dictionary and print each pair like:
#   "apple costs 50"
# Hint: use .items()
prices = {"apple": 50, "banana": 20, "mango": 70}

# YOUR CODE HERE
for price, cost in prices.items():
    print(f"{price} cost {cost}")


# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Count the letters
# ----------------------------------------------------------
# Count how many times each letter appears in the word below
# and store the result in a dictionary, then print it.
# Example: "apple" -> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
# Hint: loop through each letter; if it's already a key add 1,
#       otherwise start it at 1.
word = "banana"

# YOUR CODE HERE
count = {}

for a in word:
    if a in count:
        count[a] = count[a] + 1
    else:
        count[a] = 1
print(count)

# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# book = {"title": "Python 101", "author": "Abdul", "year": 2026}
# print(book)
#
# --- Exercise 2 ---
# print(capitals["Pakistan"])
#
# --- Exercise 3 ---
# groceries["milk"] = 60
# groceries["eggs"] = 120
# print(groceries)
#
# --- Exercise 4 ---
# print("math" in marks)
# del marks["history"]
# print(marks)
#
# --- Exercise 5 ---
# for item, price in prices.items():
#     print(f"{item} costs {price}")
#
# --- Exercise 6 ---
# counts = {}
# for letter in word:
#     if letter in counts:
#         counts[letter] = counts[letter] + 1
#     else:
#         counts[letter] = 1
# print(counts)
# ==========================================================
