# ==========================================================
#  WHILE LOOPS — FOCUSED DRILLS
# ==========================================================
# We drilled `for` loops a lot but barely touched `while`.
# This file fixes that.
#
# A `for` loop repeats ONCE PER ITEM in a sequence.
# A `while` loop repeats AS LONG AS a condition stays True —
# use it when you DON'T know how many times in advance.
#
# The shape of every while-loop:
#       <set up a variable>
#       while <condition is True>:
#           <do something>
#           <CHANGE the variable>   # <-- or it runs FOREVER!
#
# ⚠️ THE #1 RULE: something inside the loop MUST move the
#    condition toward False, or the loop never stops.
#    (If you ever get stuck in an infinite loop, press Ctrl+C.)
#
# Do each drill at "# YOUR CODE HERE". Run often:
#       python while_loops_drills.py
# Expected answers are stated; full answers at the bottom.
# ==========================================================


# ----------------------------------------------------------
# DRILL 1: Count UP from 1 to 5 with a while-loop
# ----------------------------------------------------------
# Print 1, 2, 3, 4, 5 (each on its own line).
# Hint: start n = 1; loop while n <= 5; print n; then n = n + 1
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 2: Count DOWN from 5 to 1, then print "Lift off!"
# ----------------------------------------------------------
# Expected: 5 4 3 2 1 then Lift off!
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 3: Running total with while (accumulator, while-style)
# ----------------------------------------------------------
# Add up the numbers 1 + 2 + 3 + ... + 10 using a while-loop.
# Expected: 55
# Hint: keep a 'total' AND a counter 'n'; loop while n <= 10.
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 4: Keep doubling until past 1000
# ----------------------------------------------------------
# Start at 1 and keep doubling (n = n * 2), printing each
# value, WHILE n is less than 1000.
# Expected: 1 2 4 8 16 32 64 128 256 512
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 5: Sum numbers 1, 2, 3... and STOP once total passes 20
# ----------------------------------------------------------
# Add 1, then 2, then 3... to a running total. Keep going
# WHILE the total is <= 20. Print the final total.
# (This is a condition-controlled stop — you don't know up
#  front how many numbers it takes.)
# Expected: 21   (1+2+3+4+5+6 = 21, which is the first time it passes 20)
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 6: break — stop a while-loop early
# ----------------------------------------------------------
# Loop "forever" with  while True:  but BREAK as soon as a
# counter reaches 3. Print the counter each round before breaking.
# Expected: 1 2 3   (then stop)
# Hint: start count = 0; inside: count += 1; print; if count == 3: break
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 7: continue — skip one value inside a while-loop
# ----------------------------------------------------------
# Count from 1 to 5 but SKIP printing 3 (use continue).
# Expected: 1 2 4 5
# ⚠️ TRAP: you must still increase the counter BEFORE continue,
#    or you'll skip the increment and loop forever on 3!
# YOUR CODE HERE



# ----------------------------------------------------------
# DRILL 8 (THINK): for or while?
# ----------------------------------------------------------
# You don't write code here — just answer in a comment.
# For each task, write "for" or "while":
#   a) Print every name in a list.                  -> ?
#   b) Keep halving a number until it is below 1.   -> ?
#   c) Add up all scores in a dictionary.           -> ?
#   d) Ask the user again and again until they      -> ?
#      type the correct password.
# YOUR ANSWERS HERE (as a comment):
# a)
# b)
# c)
# d)




# ==========================================================
#  ANSWERS  (try first! Remove # to check.)
# ==========================================================
#
# --- Drill 1 ---
# n = 1
# while n <= 5:
#     print(n)
#     n = n + 1
#
# --- Drill 2 ---
# n = 5
# while n >= 1:
#     print(n)
#     n = n - 1
# print("Lift off!")
#
# --- Drill 3 ---
# total = 0
# n = 1
# while n <= 10:
#     total = total + n
#     n = n + 1
# print(total)                 # 55
#
# --- Drill 4 ---
# n = 1
# while n < 1000:
#     print(n)
#     n = n * 2
#
# --- Drill 5 ---
# total = 0
# n = 1
# while total <= 20:
#     total = total + n
#     n = n + 1
# print(total)                 # 21
#
# --- Drill 6 ---
# count = 0
# while True:
#     count = count + 1
#     print(count)
#     if count == 3:
#         break
#
# --- Drill 7 ---
# n = 0
# while n < 5:
#     n = n + 1          # increase FIRST, so continue can't trap us
#     if n == 3:
#         continue
#     print(n)
#
# --- Drill 8 ---
# a) for    (you know the collection -> loop over each item)
# b) while  (stop when a condition is met; unknown count)
# c) for    (or just sum(d.values()) -- a known collection)
# d) while  (repeat until something becomes true; unknown count)
# ==========================================================
