# ==========================================================
#  PROJECT: STUDENT GRADE MANAGER  (you build this!)
# ==========================================================
# Read README.md first. Then complete the steps below, one
# at a time. Run the file after EACH step:
#
#       python grade_manager.py
#
# A complete answer lives in solution.py — only peek if stuck.
# ==========================================================


# ----------------------------------------------------------
# STEP 1: The data  (DICTIONARIES)
# ----------------------------------------------------------
# This dictionary maps each student's name (key) to their
# score (value). It's already filled in for you — read it.
students = {
    "Abdul": 91,
    "Sara": 84,
    "Ali": 72,
    "Bilal": 55,
    "Amna": 68,
}


# ----------------------------------------------------------
# STEP 2 + 3 + 4: Print a report line for each student
#   - LOOP through the dictionary           (loops)
#   - turn each score into a grade A/B/C/F  (conditions)
#   - print a neat line with an f-string    (strings)
# ----------------------------------------------------------
# Grade rules:  90+ -> "A"   80-89 -> "B"   70-79 -> "C"   below 70 -> "F"
#
# Goal output (one line per student), for example:
#       Abdul : 91 -> Grade A
#
# TIP: loop with  ->  for name, score in students.items():
#      then use if/elif/else to pick the grade.

print("===== CLASS REPORT =====")

# YOUR CODE HERE (Steps 2-4)
for name, score in students.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"{name} : {score} -> Grade {grade}") # Abdul : 91 -> Grade A

# ----------------------------------------------------------
# STEP 5: Class statistics  (NUMBERS + LOOPS)
# ----------------------------------------------------------
# Using the scores, calculate and print:
#   a) the class AVERAGE   (sum of scores / number of students)
#   b) the HIGHEST score
#   c) the LOWEST score
#   d) how many students PASSED (score >= 50)
#
# TIP: students.values() gives you all the scores.
#      You can use sum(), len(), max(), min() on them,
#      OR practice doing it with your own loop!

print()
print("------ STATISTICS ------")

# YOUR CODE HERE (Step 5)

# a) AVERAGE — your own loop building a total + a count, then dividing.
#    (You could also just write:  sum(students.values()) / len(students)  )
total = 0
student_count = 0
for name, score in students.items():
    total = total + score          # running total of all scores
    student_count = student_count + 1   # count of students
average = total / student_count
print(f"Class average : {average}")

# b) HIGHEST score — track-the-best (start at the first score, keep the bigger).
highest_score = 0
for name, score in students.items():
    if score > highest_score:
        highest_score = score
print(f"Highest score : {highest_score}")

# c) LOWEST score — track-the-best, but the OTHER way.
#    IMPORTANT: start 'lowest' at a real score (the first one), NOT 0!
#    If you start at 0, no positive score is ever < 0, so it stays 0 forever.
lowest_score = list(students.values())[0]   # start at the first student's score
for name, score in students.items():
    if score < lowest_score:
        lowest_score = score
print(f"Lowest score  : {lowest_score}")

# d) PASS COUNT — this is your Drill 4, applied to the dictionary's scores.
passed = 0
for name, score in students.items():
    if score >= 50:
        passed = passed + 1
print(f"Students passed: {passed} out of {student_count}")


# ----------------------------------------------------------
# 🌟 BONUS
# ----------------------------------------------------------
print()
print("------ BONUS ------")

# Bonus 1: WHICH student had the highest / lowest score (track name too).
top_name = ""
low_name = ""
for name, score in students.items():
    if score == highest_score:
        top_name = name
    if score == lowest_score:
        low_name = name
print(f"Top student   : {top_name} ({highest_score})")
print(f"Lowest student: {low_name} ({lowest_score})")

# Bonus 2: count how many got each grade, using the COUNTING pattern in a dict.
grade_tally = {}
for name, score in students.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    # the dictionary counting pattern (like the letter-count drill):
    if grade in grade_tally:
        grade_tally[grade] = grade_tally[grade] + 1
    else:
        grade_tally[grade] = 1
print(f"Grade tally   : {grade_tally}")


# students = {
#     "Abdul": 91,
#     "Sara": 84,
#     "Ali": 72,
#     "Bilal": 55,
#     "Amna": 68,
# }

# ----------------------------------------------------------
# 🌟 BONUS (optional, only if you want a challenge):
#   - Show WHICH student had the highest/lowest score (the name)
#   - Count how many got each grade (A/B/C/F) using a dictionary
#   - Ask the user to type a new student + score with input()
#     and add them to the dictionary before printing the report
# ----------------------------------------------------------
