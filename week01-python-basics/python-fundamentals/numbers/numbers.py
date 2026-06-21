# ==========================================================
#  PYTHON NUMBERS — A Beginner's Tutorial
# ==========================================================
# Python has two main number types:
#   - int   -> whole numbers:      5, -20, 1000
#   - float -> decimal numbers:    3.14, -0.5, 2.0
#
# You can do math directly with them, just like a calculator.
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: int vs float
# ----------------------------------------------------------
count = 10           # int   -> a whole number
price = 19.99        # float -> has a decimal point

print("Example 1: int vs float")
print(count, type(count))
print(price, type(price))
print()


# ----------------------------------------------------------
# EXAMPLE 2: Basic arithmetic (+  -  *  /)
# ----------------------------------------------------------
a = 12
b = 5

print("Example 2: Basic math")
print("Add:     ", a + b)   # 17
print("Subtract:", a - b)   # 7
print("Multiply:", a * b)   # 60
print("Divide:  ", a / b)   # 2.4   (/ always gives a float!)
print()


# ----------------------------------------------------------
# EXAMPLE 3: Special operators ( //  %  ** )
# ----------------------------------------------------------
print("Example 3: Special operators")
print("Floor divide 17 // 5:", 17 // 5)  # 3  -> divide, drop the decimal
print("Remainder   17 %  5:", 17 % 5)    # 2  -> what's left over (modulo)
print("Power       2 ** 3 :", 2 ** 3)    # 8  -> 2 to the power of 3
print()
# Handy trick: "number % 2 == 0" tells you if a number is even.
print("Is 10 even?", 10 % 2 == 0)        # True
print("Is 7 even? ", 7 % 2 == 0)         # False
print()


# ----------------------------------------------------------
# EXAMPLE 4: Order of operations (PEMDAS)
# ----------------------------------------------------------
# Python follows math rules: Parentheses first, then Exponents,
# then Multiply/Divide, then Add/Subtract.
print("Example 4: Order of operations")
print(2 + 3 * 4)        # 14  (multiply first, THEN add)
print((2 + 3) * 4)      # 20  (parentheses force add first)
print()


# ----------------------------------------------------------
# EXAMPLE 5: Converting between types (int, float, str)
# ----------------------------------------------------------
# Numbers typed by a user often arrive as TEXT (a string).
# Convert before doing math, or you'll join text instead of adding!
age_text = "25"               # this is a string, not a number

print("Example 5: Type conversion")
print(int(age_text) + 5)      # 30   -> int() turns "25" into 25
print(float("3.5") + 1)       # 4.5  -> float() turns text into a decimal
print(str(100) + " points")   # "100 points" -> str() turns number to text
print(int(9.99))              # 9    -> int() chops off the decimal
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Useful built-in number tools
# ----------------------------------------------------------
print("Example 6: Handy built-ins")
print("round(3.14159, 2):", round(3.14159, 2))  # 3.14 -> round to 2 places
print("abs(-8):          ", abs(-8))             # 8    -> absolute value
print("max(4, 9, 2):     ", max(4, 9, 2))        # 9    -> biggest
print("min(4, 9, 2):     ", min(4, 9, 2))        # 2    -> smallest
print("sum([1, 2, 3]):   ", sum([1, 2, 3]))      # 6    -> total of a list
