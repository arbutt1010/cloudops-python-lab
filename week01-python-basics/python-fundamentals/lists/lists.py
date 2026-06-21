# ==========================================================
#  PYTHON LISTS — A Beginner's Tutorial
# ==========================================================
# A "list" stores MANY values in one variable, in order.
# You create one with square brackets [ ] and commas:
#
#       fruits = ["apple", "banana", "cherry"]
#
# Lists can hold any type, and they can grow or shrink.
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: Creating lists
# ----------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["Abdul", 25, True, 5.9]   # a list can mix types
empty = []                         # a list with nothing in it (yet)

print("Example 1: Creating lists")
print(fruits)
print(numbers)
print(mixed)
print("Length of fruits:", len(fruits))   # len() counts the items
print()


# ----------------------------------------------------------
# EXAMPLE 2: Accessing items (indexing & slicing)
# ----------------------------------------------------------
# Just like strings, positions start at 0:
#
#     fruits =  apple  banana  cherry
#     index      0       1       2
#     (also     -3      -2      -1   from the end)
print("Example 2: Accessing items")
print(fruits[0])     # 'apple'  -> first item
print(fruits[-1])    # 'cherry' -> last item
print(fruits[0:2])   # ['apple', 'banana'] -> a slice (2 is NOT included)
print()


# ----------------------------------------------------------
# EXAMPLE 3: Changing a list (lists are "mutable")
# ----------------------------------------------------------
# Unlike strings, you CAN change a list in place.
colors = ["red", "green", "blue"]
print("Example 3: Changing items")
print("Before:", colors)

colors[1] = "yellow"     # replace the item at index 1
print("After: ", colors) # ['red', 'yellow', 'blue']
print()


# ----------------------------------------------------------
# EXAMPLE 4: Adding and removing items
# ----------------------------------------------------------
animals = ["cat", "dog"]
print("Example 4: Adding and removing")

animals.append("rabbit")     # add to the END
print("After append:", animals)

animals.insert(0, "horse")   # add at a specific position (index 0)
print("After insert:", animals)

animals.remove("dog")        # remove by VALUE
print("After remove:", animals)

last = animals.pop()         # remove & return the LAST item
print("Popped:", last, "-> now:", animals)
print()


# ----------------------------------------------------------
# EXAMPLE 5: Looping through a list
# ----------------------------------------------------------
# A "for" loop visits each item one at a time.
shopping = ["milk", "eggs", "bread"]
print("Example 5: Looping through a list")
for item in shopping:
    print("Buy:", item)
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Handy list tools
# ----------------------------------------------------------
scores = [88, 72, 95, 60, 79]
print("Example 6: Handy list tools")
print("Highest:", max(scores))     # 95
print("Lowest: ", min(scores))     # 60
print("Total:  ", sum(scores))     # 394
print("Count:  ", len(scores))     # 5
print("Is 95 in the list?", 95 in scores)   # True

scores.sort()                      # sort from low to high (changes the list)
print("Sorted: ", scores)

words = ["banana", "apple", "cherry"]
words.sort()                       # sorts text alphabetically
print("Sorted words:", words)
