# ==========================================================
#  HOW TO MASTER LOOPS — best ways to learn, as QUESTIONS
# ==========================================================
# You said loops are important and you want to go deep. The
# fastest way to truly learn loops is to keep asking yourself
# the RIGHT questions. Below are the habits that work best,
# each written as a question to ask while you practice.
#
# This file is for READING, not running. Use it as a checklist.
# ==========================================================


# ----------------------------------------------------------
#  HABIT 1: "Predict before you run"  (the #1 technique)
# ----------------------------------------------------------
# Before pressing run, ALWAYS ask yourself:
#   - "What will this print, line by line?"
#   - "How many times will the loop run?"
#   - "What is the loop variable on the FIRST round? The LAST?"
# Then run it and compare. When you are wrong, that gap is
# EXACTLY the thing you needed to learn. This single habit
# teaches loops faster than anything else.


# ----------------------------------------------------------
#  HABIT 2: "Trace it on paper"  (be the computer)
# ----------------------------------------------------------
# For any loop, draw a small table and fill one row per round:
#
#       round | i  | total
#       ------|----|------
#         1   | 1  |  1
#         2   | 2  |  3
#         3   | 3  |  6
#
# Ask: "What changes each round? What stays the same?"
# If you can fill this table, you understand the loop.


# ----------------------------------------------------------
#  HABIT 3: "for or while?"  (pick the right tool)
# ----------------------------------------------------------
# Before writing a loop, ask:
#   - "Do I know what I'm looping OVER (a list/range/string)?"
#         -> use FOR
#   - "Do I loop UNTIL something changes, unknown # of times?"
#         -> use WHILE
# Example questions to test yourself:
#   - "Print every name in a list" -> for or while?   (for)
#   - "Keep asking until the user types 'quit'" -> ?   (while)


# ----------------------------------------------------------
#  HABIT 4: "Will this while-loop ever STOP?"
# ----------------------------------------------------------
# Every time you write a while-loop, ask:
#   - "What makes the condition become False?"
#   - "Is that change actually INSIDE the loop?"
# If you can't point to the line that moves toward stopping,
# you have an infinite loop. (Ctrl+C stops a runaway loop.)


# ----------------------------------------------------------
#  HABIT 5: "What are my edge cases?"
# ----------------------------------------------------------
# Test your loop with tricky inputs and ask:
#   - "What if the list is EMPTY?"            (does it crash?)
#   - "What if there's only ONE item?"
#   - "What about the FIRST and LAST item?" (off-by-one bugs)
# range(1, 6) gives 1..5 — ask "does it include the stop number?"
# (No! range stops BEFORE it. This is the most common loop bug.)


# ----------------------------------------------------------
#  HABIT 6: "What's my accumulator?"  (the build-up pattern)
# ----------------------------------------------------------
# Tons of loops follow this shape:
#       result = <start value>      # 0 for sums, [] for lists
#       for item in things:
#           result = result <update> item
#       print(result)
# Ask yourself:
#   - "What do I start the accumulator at?"
#   - "How does each item change it?"
# Recognising this pattern lets you solve half of all loop tasks.


# ----------------------------------------------------------
#  HABIT 7: "Can I explain it out loud?"  (rubber-duck test)
# ----------------------------------------------------------
# Say your loop in plain English, e.g.:
#   "Start total at 0. For each price, add it to total.
#    After the last price, print total."
# If you can't say it simply, you don't fully understand it yet.


# ----------------------------------------------------------
#  A QUICK SELF-QUIZ (answer these in your head)
# ----------------------------------------------------------
# 1. How many times does 'for i in range(3):' run?
# 2. What numbers does range(2, 8, 2) produce?
# 3. What's the difference between break and continue?
# 4. Why might a while-loop run forever?
# 5. In 'for x in "Hi":', what is x on each round?
# 6. What value should 'total' start at to SUM a list?
# 7. Does range(1, 5) include 5?
# 8. When would you choose while instead of for?
#
# ---- answers ----
# 1. 3 times (i = 0, 1, 2)
# 2. 2, 4, 6  (stops before 8)
# 3. break leaves the loop; continue skips to the next round
# 4. because nothing inside makes the condition False
# 5. 'H' then 'i'  (one character per round)
# 6. 0
# 7. No — it stops before 5, so 1, 2, 3, 4
# 8. when you don't know how many rounds you'll need in advance
