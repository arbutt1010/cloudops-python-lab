# ==========================================================
#  PYTHON LOOPS — EXTRA PRACTICE (20 questions)
# ==========================================================
# Loops are SO important that this file gives you lots of
# practice. It has two parts:
#
#   PART A (Q1-Q10): Worked examples. The answer is shown
#                    right there. Read it, then TYPE IT OUT
#                    yourself and run it. Then change the
#                    numbers and predict the new output.
#
#   PART B (Q11-Q20): Challenges. NO answers next to them.
#                     Solve them yourself. The answers are
#                     all the way at the BOTTOM of this file.
#
# How to use: run "python practice_extra.py" often. Try to
# PREDICT the output in your head BEFORE you run it.
# ==========================================================


# ==========================================================
#  PART A  —  WORKED EXAMPLES (study + retype these)
# ==========================================================

# ----------------------------------------------------------
# Q1: Print the numbers 1 to 5 using range().
# ----------------------------------------------------------
# ANSWER:
for i in range(1, 6):
    print(i)

for i in range(1, 6):
    print(i)

# ----------------------------------------------------------
# Q2: Print each name in the list with a greeting (f-string).
# ----------------------------------------------------------
names = ["Abdul", "Sara", "Ali"]
# ANSWER:
for name in names:
    print(f"Hello, {name}!")

for name in names:
    print(f"Hello, {name}!")

# ----------------------------------------------------------
# Q3: Add up all numbers in a list and print the total.
# ----------------------------------------------------------
prices = [100, 250, 75]
# ANSWER:
total = 0
for price in prices:
    total = total + price       # running total pattern
print("Total:", total)

total = 0
for price in prices:
    total = total + price
print("Total: ", total)

# ----------------------------------------------------------
# Q4: Count DOWN from 5 to 1 with a while-loop.
# ----------------------------------------------------------
# ANSWER:
count = 5
while count > 0:
    print(count)
    count = count - 1           # <- this is what stops the loop

count = 5
while count > 0:
    print(count)
    count = count -1

# ----------------------------------------------------------
# Q5: Print only the EVEN numbers from a list.
# ----------------------------------------------------------
values = [1, 2, 3, 4, 5, 6]
# ANSWER:
for num in values:
    if num % 2 == 0:
        print(num)

print("You are here")
for num in values:
    if num % 2 == 0:
        print(num)

# ----------------------------------------------------------
# Q6: Print the first 5 multiples of 3 (3, 6, 9, 12, 15).
# ----------------------------------------------------------
# ANSWER:
for i in range(1, 6):
    print(i * 3)

for i in range(1, 6):
    print(1 * 3)


# ----------------------------------------------------------
# Q7: Count how many words are longer than 4 letters.
# ----------------------------------------------------------
words = ["cat", "elephant", "dog", "tiger"]
# ANSWER:
long_count = 0
print("Animals Example:")
for word in words:
    if len(word) > 4:
        long_count = long_count + 1
print("Long words:", long_count)


# ----------------------------------------------------------
# Q8: Use break to stop the loop at the first number > 10.
# ----------------------------------------------------------
nums = [3, 7, 9, 12, 5, 20]
# ANSWER:
for n in nums:
    if n > 10:
        print("First big number:", n)
        break                   # leave the loop immediately


# ----------------------------------------------------------
# Q9: Use continue to skip the number 3, print the rest.
# ----------------------------------------------------------
# ANSWER:
for i in range(1, 6):
    if i == 3:
        continue                # skip this round only
    print(i)


# ----------------------------------------------------------
# Q10: Use enumerate() to print position + value.
# ----------------------------------------------------------
fruits = ["apple", "mango", "grapes"]
# ANSWER:
for index, fruit in enumerate(fruits):
    print(index, fruit)


# ==========================================================
#  PART B  —  CHALLENGES (no answers here! see the bottom)
# ==========================================================
# Write your code under each "# YOUR CODE HERE".
# Try to predict the output before running.

# ----------------------------------------------------------
# Q11: Print the numbers 10 down to 1 using range().
#      Hint: range(start, stop, step) can step BACKWARDS
#            with a negative step, e.g. range(10, 0, -1).
# ----------------------------------------------------------
# YOUR CODE HERE
print("Using number range(start, stop, step) method")
print(list(range(10, 1, -1)))
for i in range(10, 0, -1):
    print(i)

# ----------------------------------------------------------
# Q12: Given the list, print the SQUARE of each number
#      (number * number).
list12 = [2, 4, 6, 8]
# ----------------------------------------------------------
# YOUR CODE HERE
print("######")
print("Q12:")
print("######")
for i in list12:
    x = i * i
    print(x)


# ----------------------------------------------------------
# Q13: Count how many numbers in the list are ODD.
#      Print the final count.
list13 = [3, 8, 11, 14, 7, 2, 5]
# ----------------------------------------------------------
# YOUR CODE HERE
print("######")
print("Q13:")
print("######")
odd_count = 0
for num in list13:
    if num % 2 != 0:
        odd_count = odd_count + 1
print(odd_count)


# ----------------------------------------------------------
# Q14: Add up only the EVEN numbers from 1 to 10 and print
#      the total. (Use range() and the % trick.)
# ----------------------------------------------------------
# YOUR CODE HERE
even_count = 0
for num in range(1, 11):
    if num % 2 == 0:
        even_count = even_count + num
print(even_count)

# ----------------------------------------------------------
# Q15: Loop through the word "PYTHON" and print each letter
#      on its own line.
# ----------------------------------------------------------
# YOUR CODE HERE
chars = "PYTHON"
for char in chars:
    print(char)

# ----------------------------------------------------------
# Q16: Use a while-loop to keep doubling a number starting
#      at 1, printing it, while it is less than 100.
#      (1, 2, 4, 8, 16, 32, 64)
# ----------------------------------------------------------
# YOUR CODE HERE
n = 1 
while n < 100:
    print(n)
    n = n * 2

# ----------------------------------------------------------
# Q17: Find the SMALLEST number in the list WITHOUT min().
#      Hint: start 'smallest' at the first item, update it
#      whenever you find something smaller.
list17 = [25, 9, 41, 4, 18]
# ----------------------------------------------------------
# YOUR CODE HERE
smallest = list17[0]
for num in list17:
    if num < smallest:
        smallest = num
print(smallest)               # 4



# ----------------------------------------------------------
# Q18: Given a list of names, print only the ones that
#      start with the letter "A".
#      Hint: name.startswith("A")
list18 = ["Abdul", "Sara", "Ali", "Bilal", " Amna".strip()]
# ----------------------------------------------------------
# YOUR CODE HERE
for name in list18:
    if name.startswith("A"):
        print(name)


# ----------------------------------------------------------
# Q19: Count down from 5 to 1, but SKIP the number 3
#      (use a loop + continue). Print "Go!" at the end.
# ----------------------------------------------------------
# YOUR CODE HERE
count = 5
while count > 0:
    if count == 3:
        count = count - 1
        continue
    print(count)
    count = count -1
print("Go!")

# ----------------------------------------------------------
# Q20 (CHALLENGE): Print a multiplication table for 5
#      from 5x1 to 5x10, like:  "5 x 1 = 5"
#      Hint: loop i in range(1, 11) and use an f-string.
# ----------------------------------------------------------
# YOUR CODE HERE
table = 5
for i in range(1, 11):
    result = table * i
    print(f"{table} x {i} = {result}")



# ==========================================================
#  ANSWERS FOR PART B (Q11-Q20)
# ==========================================================
# Try first! Remove the # to check each one.
#
# --- Q11 ---
# for i in range(10, 0, -1):
#     print(i)
#
# --- Q12 ---
# for num in list12:
#     print(num * num)
#
# --- Q13 ---
# odd_count = 0
# for num in list13:
#     if num % 2 != 0:          # != 0 means "not even" = odd
#         odd_count = odd_count + 1
# print(odd_count)              # 4
#
# --- Q14 ---
# total = 0
# for n in range(1, 11):
#     if n % 2 == 0:
#         total = total + n
# print(total)                  # 30
#
# --- Q15 ---
# for letter in "PYTHON":
#     print(letter)
#
# --- Q16 ---
# n = 1
# while n < 100:
#     print(n)
#     n = n * 2
#
# --- Q17 ---
# smallest = list17[0]
# for num in list17:
#     if num < smallest:
#         smallest = num
# print(smallest)               # 4
#
# --- Q18 ---
# for name in list18:
#     if name.startswith("A"):
#         print(name)
#
# --- Q19 ---
# count = 5
# while count > 0:
#     if count == 3:
#         count = count - 1     # still must decrease before skipping!
#         continue
#     print(count)
#     count = count - 1
# print("Go!")
#
# --- Q20 ---
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")
# ==========================================================
