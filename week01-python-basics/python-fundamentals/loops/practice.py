# ==========================================================
#  PYTHON LOOPS — PRACTICE EXERCISES
# ==========================================================
# Solve each exercise where it says "# YOUR CODE HERE".
# Then run this file to test yourself:
#
#       python practice.py
#
# (Solutions are at the very bottom — try first! No peeking 😄)
# ==========================================================


# ----------------------------------------------------------
# EXERCISE 1: Count to 5
# ----------------------------------------------------------
# Use a for-loop with range() to print the numbers 1 to 5
# (each on its own line).

# YOUR CODE HERE
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
print()


# ----------------------------------------------------------
# EXERCISE 2: Greet everyone
# ----------------------------------------------------------
# Loop through the list and print "Hello, <name>!" for each.
names = ["Abdul", "Sara", "Ali"]

# YOUR CODE HERE
for name in names:
    print("Hello, ", name)
print()


# ----------------------------------------------------------
# EXERCISE 3: Sum the numbers
# ----------------------------------------------------------
# Use a loop to add up all the numbers in the list and
# print the total. (Start a 'total' at 0, add each number.)
numbers = [5, 10, 15, 20]

# YOUR CODE HERE
total = 0

for num in numbers:
    total = total + num
print(total)



# ----------------------------------------------------------
# EXERCISE 4: Countdown with while
# ----------------------------------------------------------
# Use a WHILE loop to count down from 5 to 1, printing each
# number. Then print "Done!" after the loop.

# YOUR CODE HERE
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Done!")


# ----------------------------------------------------------
# EXERCISE 5: Only the even numbers
# ----------------------------------------------------------
# Loop through the list and print ONLY the even numbers.
# Hint: a number is even when  num % 2 == 0
values = [1, 2, 3, 4, 5, 6, 7, 8]

# YOUR CODE HERE
for num in values:
    if num % 2 == 0:
        print(num)


# ----------------------------------------------------------
# EXERCISE 6 (CHALLENGE): Find the biggest number yourself
# ----------------------------------------------------------
# WITHOUT using max(), use a loop to find the largest number.
# Hint: keep a variable 'biggest', start it at the first item,
#       and update it whenever you find a bigger number.
nums = [3, 41, 17, 9, 28]

# YOUR CODE HERE
biggest = nums[0]
for num in nums:
    if num > biggest:
        biggest = num
print(biggest)



# ==========================================================
#  SOLUTIONS  (scroll up and try first!)
# ==========================================================
# Remove the # at the start of each line to check.
#
# --- Exercise 1 ---
# for i in range(1, 6):
#     print(i)
#
# --- Exercise 2 ---
# for name in names:
#     print(f"Hello, {name}!")
#
# --- Exercise 3 ---
# total = 0
# for num in numbers:
#     total = total + num
# print(total)
#
# --- Exercise 4 ---
# count = 5
# while count > 0:
#     print(count)
#     count = count - 1
# print("Done!")
#
# --- Exercise 5 ---
# for num in values:
#     if num % 2 == 0:
#         print(num)
#
# --- Exercise 6 ---
# biggest = nums[0]
# for num in nums:
#     if num > biggest:
#         biggest = num
# print(biggest)
# ==========================================================
