# ==========================================================
#  DO I EVEN NEED A LOOP HERE?  (a concept note)
# ==========================================================
# A super common beginner habit is to reach for a "for" loop
# every time you touch a list or dictionary. But sometimes a
# built-in function ALREADY does the whole job for you.
#
# This file is for READING. It explains when a loop is needed
# and when it's not. (Then accumulator_drills.py lets you
# practice the cases that DO need a loop.)
# ==========================================================


# ----------------------------------------------------------
#  RULE OF THUMB
# ----------------------------------------------------------
# Built-ins that already walk the WHOLE collection for you
# (NO loop needed):
#     sum(things)   -> the total of all numbers
#     max(things)   -> the biggest
#     min(things)   -> the smallest
#     len(things)   -> how many items

#
# You DO need to write your OWN loop when you:
#     - build something up step by step (a running total/count)
#     - apply a CONDITION to each item (count/filter only some)
#     - track "the best so far" with extra info (like a name)
#
# Short version:
#     "Whole thing at once?"   -> use a built-in, no loop.
#     "One item at a time, with my own rule?" -> write a loop.


# ----------------------------------------------------------
#  THE OVER-LOOPING MISTAKE (very common!)
# ----------------------------------------------------------
scores = [91, 84, 72, 55, 68]

# ❌ Over-looped: sum() already adds everything, so this loop
#    just recalculates the SAME number 5 times for no reason.
for s in scores:
    average = sum(scores) / len(scores)
print("Over-looped average:", average)   # right answer, wasteful + confusing

# ✅ Correct: sum() and len() do the whole job in ONE line.
average = sum(scores) / len(scores)
print("Clean average:      ", average)
print()
# Both print 74.0 — but the second one says exactly what it means.


# ----------------------------------------------------------
#  WHEN A LOOP IS GENUINELY NEEDED
# ----------------------------------------------------------
# There is NO built-in for "count how many scores are >= 50",
# because that's YOUR custom rule. So you build it yourself:
passed = 0                      # start a counter
for s in scores:                # look at each score
    if s >= 50:                 # your custom condition
        passed = passed + 1     # accumulate
print("Passed (needs a loop):", passed)   # 5 (all five scores are >= 50)
print()
# This is the "accumulator pattern" — practice it in
# accumulator_drills.py. It's the skill that unlocks the project.


# ----------------------------------------------------------
#  SELF-QUIZ:  loop, or no loop?  (answer in your head)
# ----------------------------------------------------------
# 1. "Add up all the prices in a list."
# 2. "Count how many prices are above 100."
# 3. "Find the biggest number in a list."
# 4. "Find the biggest number AND which name it belongs to."
# 5. "How many items are in the list?"
# 6. "Add up only the EVEN numbers."
#
# ---- answers ----
# 1. NO loop  -> sum(prices)
# 2. LOOP     -> custom condition (> 100), count them yourself
# 3. NO loop  -> max(numbers)
# 4. LOOP     -> max() gives the value but not the name; you must
#                loop to find which item matches (track-the-best)
# 5. NO loop  -> len(items)
# 6. LOOP     -> "only even" is a custom condition; sum them yourself
