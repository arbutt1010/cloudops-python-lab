# ==========================================================
#  ACCUMULATOR PATTERN — FOCUSED DRILLS
# ==========================================================
# THE most important loop skill: building up a result with a
# running variable. Master this and the project's Step 5
# becomes easy.
#
# The pattern always has the same 3 parts:
#
#       result = <start value>     # 1. START (0 for sums/counts)
#       for item in things:        # 2. LOOP over each item
#           result = result ...    # 3. UPDATE the result
#       print(result)              #    use it after the loop
#
# Do each drill where it says "# YOUR CODE HERE". Run often:
#       python accumulator_drills.py
# Each drill tells you the expected answer. Answers at bottom.
# ==========================================================


# ----------------------------------------------------------
# DRILL 1: Running total (the simplest accumulator)
# ----------------------------------------------------------
# Add up all the numbers. Start total at 0, add each one.
# Expected: 100
nums = [10, 20, 30, 40] # Items
# YOUR CODE HERE
accumulator_variable = 0 # Start accumulator variable to count items
for n in nums: # LOOP over each item in the nums item list
    accumulator_variable = accumulator_variable + n # Update the result
print(accumulator_variable) # Use the updated result 

# ----------------------------------------------------------
# DRILL 2: Count the items (counter accumulator)
# ----------------------------------------------------------
# Count how many numbers are in the list using a loop
# (start count at 0, add 1 each time). Expected: 5
# (Yes, len() does this — but practice the PATTERN here.)
items = [7, 3, 9, 1, 6]
# YOUR CODE HERE
accu = 0
for i in items:
    accu = accu + 1
print(accu)


# ----------------------------------------------------------
# DRILL 3: Count only some (counter + condition)
# ----------------------------------------------------------
# Count how many numbers are GREATER THAN 10.
# Start count at 0; add 1 only when the condition is true.
# Expected: 3
values = [4, 15, 8, 23, 11, 2]
# YOUR CODE HERE
counter = 0
for var in values:
    if var > 10:
        counter = counter + 1
print(counter)


# ----------------------------------------------------------
# DRILL 4: Count passing scores  (mirrors the PROJECT!)
# ----------------------------------------------------------
# Count how many scores are >= 50 (a "pass"). Expected: 3
# This is the exact pattern the project's Step 5 (d) needs,
# just with different data so YOU still solve the project.
test_scores = [88, 42, 50, 71, 33]
# YOUR CODE HERE
counter2 = 0
for score in test_scores:
    if score >= 50:
        counter2 = counter2 + 1
print("Q4")
print(counter2)


# ----------------------------------------------------------
# DRILL 5: Sum only some (total + condition)
# ----------------------------------------------------------
# Add up ONLY the even numbers. Start total at 0; add a
# number only if it is even (num % 2 == 0). Expected: 12
mixed = [1, 2, 3, 4, 6, 7]
# YOUR CODE HERE
counter3 = 0
for num in mixed:
    if num % 2 == 0:
        counter3 = counter3 + num
print(counter3)


# ----------------------------------------------------------
# DRILL 6: Accumulate from a DICTIONARY's values
# ----------------------------------------------------------
# Count how many students scored >= 60.
# Hint: loop over  grades.values()  (or grades.items()).
# Expected: 3
grades = {"A": 91, "B": 55, "C": 72, "D": 40, "E": 68}
# YOUR CODE HERE
counter4 = 0
for grade, score in grades.items():
    print(grade, score)
    if score >= 60:
        counter4 = counter4 + 1
        print(grade, score)
print("Q6")    
print(counter4)


# ----------------------------------------------------------
# DRILL 7: Two accumulators at once
# ----------------------------------------------------------
# In ONE loop, count how many numbers are even AND how many
# are odd. Print both. Expected: even = 3, odd = 3
data = [10, 7, 4, 5, 2, 9]
# YOUR CODE HERE
even = 0
odd = 0
print("Two Accumulators at Once")
for d in data:
    if d % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"Even = {even}, Odd = {odd}")

# ----------------------------------------------------------
# DRILL 8: Build the average yourself (total + count + divide)
# ----------------------------------------------------------
# WITHOUT using sum() or len(): use a loop to build a running
# total AND a running count, then divide after the loop.
# Expected: 20.0
marks = [10, 20, 30]
# YOUR CODE HERE
x = 0
t = 0
for m in marks:
    x = x + 1
    t = t + m
print(t / x)


# ----------------------------------------------------------
# DRILL 9: Track the biggest yourself (track-the-best)
# ----------------------------------------------------------
# WITHOUT using max(): start 'biggest' at the first item and
# update it whenever you find a larger number. Expected: 88
list9 = [23, 88, 41, 9, 60]
# YOUR CODE HERE
biggest = list9[0] 
for i in list9:
    if i > biggest:
        biggest = i
print(biggest)


# ----------------------------------------------------------
# DRILL 10 (CHALLENGE): Biggest value AND its name
# ----------------------------------------------------------
# Find the highest score AND which student got it.
# max() alone can't give you the name — you must loop.
# Start best_score at -1 and best_name at ""; update BOTH
# when you find a higher score. Expected: Sara with 95
people = {"Abdul": 80, "Sara": 95, "Ali": 72}
# YOUR CODE HERE
ac = 0
for x, y in people.items():
    if y > ac:
        ac = y
        name = x
print("Result: ")
print(f"{name} with {ac}")



# ==========================================================
#  ANSWERS  (try every drill first! Remove # to check.)
# ==========================================================
#
# --- Drill 1 ---
# total = 0
# for n in nums:
#     total = total + n
# print(total)                       # 100
#
# --- Drill 2 ---
# count = 0
# for item in items:
#     count = count + 1
# print(count)                       # 5
#
# --- Drill 3 ---
# count = 0
# for v in values:
#     if v > 10:
#         count = count + 1
# print(count)                       # 3
#
# --- Drill 4 ---
# passed = 0
# for s in test_scores:
#     if s >= 50:
#         passed = passed + 1
# print(passed)                      # 3
#
# --- Drill 5 ---
# total = 0
# for num in mixed:
#     if num % 2 == 0:
#         total = total + num
# print(total)                       # 12
#
# --- Drill 6 ---
# count = 0
# for score in grades.values():
#     if score >= 60:
#         count = count + 1
# print(count)                       # 3
#
# --- Drill 7 ---
# even = 0
# odd = 0
# for n in data:
#     if n % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("even =", even, " odd =", odd)   # even = 3  odd = 3
#
# --- Drill 8 ---
# total = 0
# count = 0
# for m in marks:
#     total = total + m
#     count = count + 1
# print(total / count)               # 20.0
#
# --- Drill 9 ---
# biggest = list9[0]
# for n in list9:
#     if n > biggest:
#         biggest = n
# print(biggest)                     # 88
#
# --- Drill 10 ---
# best_score = -1
# best_name = ""
# for name, score in people.items():
#     if score > best_score:
#         best_score = score
#         best_name = name
# print(f"{best_name} with {best_score}")   # Sara with 95
# ==========================================================
