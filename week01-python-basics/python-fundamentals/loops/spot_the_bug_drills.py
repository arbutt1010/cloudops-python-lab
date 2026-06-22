# ==========================================================
#  SPOT THE BUG — train your eye for "right answer by luck"
# ==========================================================
# Your biggest recurring weakness isn't writing loops — it's
# that some code RUNS and even prints a believable number, but
# the LOGIC is actually wrong. It only "works" by coincidence.
#
# Each drill below is BROKEN on purpose. Your job:
#   1. Read the TASK (what it's supposed to do).
#   2. Read the CODE and predict what it really does.
#   3. Find the bug and write the corrected line(s).
#
# The bugs here are the exact kinds you hit before:
#   - counting when you should be summing (or vice versa)
#   - printing the WRONG variable
#   - a condition that doesn't match the question
#   - a wrong STARTING value
#
# Fixes are in the answer key at the bottom.
# ==========================================================


# ----------------------------------------------------------
# BUG 1 — TASK: print the SUM of these numbers (expected 60)
# ----------------------------------------------------------
nums = [10, 20, 30]
result = 0
for n in nums:
    result = result + 1        # <-- what is this actually counting?
print("Bug 1:", result)
# What does it REALLY print, and what should the line be?
# YOUR FIX (as a comment):
the actual counting of the numbers, not the sum. It prints 3, not 60.
# Fix:  result = result + n


# ----------------------------------------------------------
# BUG 2 — TASK: print how MANY numbers are above 10 (expected 2)
# ----------------------------------------------------------
values = [5, 12, 8, 30]
above = 0
for v in values:
    if v > 10:
        above = above + v      # <-- count, or add the value?
print("Bug 2:", above)
# YOUR FIX:
# Fix: above = above + 1


# ----------------------------------------------------------
# BUG 3 — TASK: print the pass count, scores >= 50 (expected 2)
# ----------------------------------------------------------
scores = [40, 75, 20, 90]
passed = 0
failed = 0
for s in scores:
    if s >= 50:
        passed = passed + 1
    else:
        failed = failed + 1
print("Bug 3:", failed)        # <-- printing the right variable?
# YOUR FIX:
# Fix: print("Bug 3:", passed)


# ----------------------------------------------------------
# BUG 4 — TASK: count students who scored >= 60 (expected 2)
# ----------------------------------------------------------
marks = {"A": 91, "B": 55, "C": 40, "D": 72}
count = 0
for name, score in marks.items():
    if score % 2 == 0:         # <-- does this match "scored >= 60"?
        count = count + 1
print("Bug 4:", count)
# YOUR FIX:
# Fix: if score >= 60:


# ----------------------------------------------------------
# BUG 5 — TASK: find the LOWEST number (expected 4)
# ----------------------------------------------------------
data = [23, 9, 41, 4, 18]
lowest = 0                     # <-- is 0 a safe starting value here?
for n in data:
    if n < lowest:
        lowest = n
print("Bug 5:", lowest)
# Why does this print 0? What should 'lowest' start at?
# YOUR FIX:
# Fix: lowest = data[0]


# ----------------------------------------------------------
# BUG 6 — TASK: print the average (expected 20.0)
# ----------------------------------------------------------
marks2 = [10, 20, 30]
total = 0
count2 = 0
for m in marks2:
    total = total + m
    count2 = count2 + 1
    print(total / count2)      # <-- right value, but printed in the WRONG PLACE
# It prints 3 times (a running average each round) instead of
# one final answer. Where should the print go?
# YOUR FIX:
# Fix: Move print OUT of the loop so it runs once, after:
#       for m in marks2:
#           total = total + m
#           count2 = count2 + 1
#       print(total / count2)        # 20.0




# ==========================================================
#  ANSWERS  (try to find each bug yourself first!)
# ==========================================================
#
# --- Bug 1 ---  counting instead of summing
#   It prints 3 (it added 1 three times), not 60.
#   Fix:  result = result + n
#
# --- Bug 2 ---  summing instead of counting
#   It prints 42 (12 + 30), not 2.
#   Fix:  above = above + 1
#
# --- Bug 3 ---  printing the wrong variable
#   The counting is fine; it just prints 'failed' (2) — which
#   happens to look plausible. It should print the pass count.
#   Fix:  print("Bug 3:", passed)
#
# --- Bug 4 ---  condition doesn't match the question
#   "% 2 == 0" counts EVEN scores, not scores >= 60.
#   Fix:  if score >= 60:
#
# --- Bug 5 ---  wrong starting value
#   No number is < 0, so 'lowest' never updates and stays 0.
#   Start at a real value from the list (the first item).
#   Fix:  lowest = data[0]
#
# --- Bug 6 ---  print in the wrong place (inside the loop)
#   Move print OUT of the loop so it runs once, after:
#       for m in marks2:
#           total = total + m
#           count2 = count2 + 1
#       print(total / count2)        # 20.0
# ==========================================================
