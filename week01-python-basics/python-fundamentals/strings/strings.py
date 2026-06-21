# ==========================================================
#  PYTHON STRINGS — A Beginner's Tutorial
# ==========================================================
# A "string" is text: a sequence of characters wrapped in
# quotes. You can use single ' ' or double " " quotes.
#
#       greeting = "Hello"
#       name     = 'Abdul'
#
# Strings are everywhere: names, messages, file paths,
# user input — anytime you work with text.
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: Creating strings (single, double, triple quotes)
# ----------------------------------------------------------
single = 'Hello'
double = "World"
triple = """This is a
multi-line string
spanning 3 lines."""        # triple quotes keep line breaks

print("Example 1: Creating strings")
print(single, double)
print(triple)
print()


# ----------------------------------------------------------
# EXAMPLE 2: Joining and repeating strings
# ----------------------------------------------------------
first_name = "Abdul"
last_name = "Rehman"

full_name = first_name + " " + last_name   # "+" joins (concatenation)
laugh = "ha" * 3                           # "*" repeats -> "hahaha"

print("Example 2: Joining and repeating")
print(full_name)
print(laugh)
print()


# ----------------------------------------------------------
# EXAMPLE 3: f-strings (the best way to build messages)
# ----------------------------------------------------------
name = "Abdul"
age = 25
# Put an "f" before the quotes, then use {variables} inside:
message = f"My name is {name} and I am {age} years old."

print("Example 3: f-strings")
print(message)
# You can even do math inside the braces:
print(f"Next year I will be {age + 1}.")
print()


# ----------------------------------------------------------
# EXAMPLE 4: Indexing and slicing (picking characters)
# ----------------------------------------------------------
# Each character has a position number (index), starting at 0:
#
#     word =   P  y  t  h  o  n
#     index    0  1  2  3  4  5
#     (also  -6 -5 -4 -3 -2 -1  counting from the end)
word = "Python"

print("Example 4: Indexing and slicing")
print(word[0])      # 'P'  -> first character
print(word[-1])     # 'n'  -> last character
print(word[0:3])    # 'Pyt' -> characters 0,1,2 (3 is NOT included)
print(word[2:])     # 'thon' -> from index 2 to the end
print(len(word))    # 6   -> len() gives the length
print()


# ----------------------------------------------------------
# EXAMPLE 5: Useful string methods
# ----------------------------------------------------------
# A "method" is a built-in action you call with a dot: text.method()
text = "  Hello World  "

print("Example 5: String methods")
print(text.upper())        # "  HELLO WORLD  "  -> all caps
print(text.lower())        # "  hello world  "  -> all lowercase
print(text.strip())        # "Hello World"      -> trims spaces at ends
print(text.replace("World", "Python"))  # swap part of the text
print("Hello World".split())  # ['Hello', 'World'] -> splits into a list
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Checking inside a string
# ----------------------------------------------------------
sentence = "I love Python programming"

print("Example 6: Searching and checking")
print("Python" in sentence)          # True  -> is the word present?
print(sentence.startswith("I"))      # True
print(sentence.endswith("ing"))      # True
print(sentence.count("o"))           # 2     -> how many 'o' letters
print(sentence.find("Python"))       # 7     -> index where it starts
