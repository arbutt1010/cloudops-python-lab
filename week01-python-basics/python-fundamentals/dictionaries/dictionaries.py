# ==========================================================
#  PYTHON DICTIONARIES — A Beginner's Tutorial
# ==========================================================
# A "dictionary" stores data as KEY -> VALUE pairs.
# Instead of a position number (like a list), you look
# things up by a LABEL (the key).
#
#       student = {"name": "Abdul", "age": 25}
#                    ^key    ^value
#
# Think of a real dictionary: you look up a WORD (key) to
# get its MEANING (value). Created with curly braces { }.
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: Creating a dictionary
# ----------------------------------------------------------
student = {
    "name": "Abdul",
    "age": 25,
    "grade": "A"
}

print("Example 1: Creating a dictionary")
print(student)
print("Number of pairs:", len(student))   # len() counts the pairs
print()


# ----------------------------------------------------------
# EXAMPLE 2: Accessing values by key
# ----------------------------------------------------------
# Use square brackets with the KEY (not a number!).
print("Example 2: Accessing values")
print(student["name"])     # Abdul
print(student["age"])      # 25

# .get() is a safer way — it returns None instead of crashing
# if the key doesn't exist:
print(student.get("grade"))      # A
print(student.get("height"))     # None (no crash!)
print()


# ----------------------------------------------------------
# EXAMPLE 3: Adding and changing values
# ----------------------------------------------------------
# Dictionaries are mutable (like lists). Assign to a key:
print("Example 3: Adding and changing")
student["age"] = 26              # change an existing value
student["city"] = "Rawalpindi"   # add a brand-new pair
print(student)
print()


# ----------------------------------------------------------
# EXAMPLE 4: Removing pairs and checking keys
# ----------------------------------------------------------
print("Example 4: Removing and checking")
del student["grade"]             # remove the "grade" pair
print(student)

# Check if a key exists with 'in':
print("name" in student)         # True
print("grade" in student)        # False
print()


# ----------------------------------------------------------
# EXAMPLE 5: Looping through a dictionary
# ----------------------------------------------------------
prices = {"apple": 50, "banana": 20, "cherry": 80}

print("Example 5: Looping")

print("-- keys --")
for key in prices:               # looping gives you the KEYS
    print(key)

print("-- keys and values together --")
for fruit, price in prices.items():   # .items() gives both
    print(f"{fruit} costs {price}")
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): keys(), values(), and a real use-case
# ----------------------------------------------------------
print("Example 6: keys(), values(), totals")
print("All keys:  ", list(prices.keys()))     # ['apple', 'banana', 'cherry']
print("All values:", list(prices.values()))   # [50, 20, 80]
print("Total price:", sum(prices.values()))    # 150

# A very common real use: COUNTING things with a dictionary.
votes = ["cat", "dog", "cat", "cat", "dog"]
counts = {}
for animal in votes:
    if animal in counts:
        counts[animal] = counts[animal] + 1   # seen before: add 1
    else:
        counts[animal] = 1                     # first time: start at 1
print("Vote counts:", counts)   # {'cat': 3, 'dog': 2}
