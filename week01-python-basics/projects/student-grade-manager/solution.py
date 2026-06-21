# ==========================================================
#  STUDENT GRADE MANAGER — SOLUTION (one possible answer)
# ==========================================================
# There are many correct ways to write this. Compare yours
# to this only AFTER you've given it a real try. If yours
# produces the right output, it's correct even if different!
#
# Run it with:  python solution.py
# ==========================================================


# ---- STEP 1: the data (dictionary) ----
students = {
    "Abdul": 91,
    "Sara": 84,
    "Ali": 72,
    "Bilal": 55,
    "Amna": 68,
}


# ---- A small helper: turn a score into a grade ----
# (Putting the grade logic in a function keeps it tidy and
#  means we don't repeat the if/elif/else. Functions are a
#  week02 topic, but here's a gentle preview!)
def grade_for(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


# ---- STEPS 2-4: the report (loop + conditions + f-strings) ----
print("===== CLASS REPORT =====")
for name, score in students.items():
    grade = grade_for(score)
    # :<8 left-aligns the name in 8 spaces so the columns line up
    print(f"{name:<8} : {score:>2}  -> Grade {grade}")


# ---- STEP 5: statistics (numbers + loops) ----
scores = list(students.values())          # [91, 84, 72, 55, 68]

average = sum(scores) / len(scores)       # 74.0
highest = max(scores)                     # 91
lowest = min(scores)                      # 55

# count how many passed (score >= 50) with our own loop
passed = 0
for score in scores:
    if score >= 50:
        passed = passed + 1

# BONUS: find WHICH student had the highest / lowest score
top_student = ""
low_student = ""
for name, score in students.items():
    if score == highest:
        top_student = name
    if score == lowest:
        low_student = name

print()
print("------ STATISTICS ------")
print(f"Class average : {average}")
print(f"Highest score : {highest} ({top_student})")
print(f"Lowest score  : {lowest} ({low_student})")
print(f"Students passed: {passed} out of {len(students)}")


# ---- BONUS: count how many of each grade (a counting dict) ----
grade_counts = {}
for score in scores:
    g = grade_for(score)
    if g in grade_counts:
        grade_counts[g] = grade_counts[g] + 1
    else:
        grade_counts[g] = 1

print()
print("------ GRADE TALLY ------")
print(grade_counts)
