# ==========================================================
#  PYTHON LOOPS — A Beginner's Tutorial
# ==========================================================
# A "loop" repeats code so you don't have to write it
# over and over. Python has two kinds:
#
#   for   -> repeat ONCE for each item in a sequence
#   while -> repeat AS LONG AS a condition stays True
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: A basic for-loop over a list
# ----------------------------------------------------------
# The loop variable ('fruit') takes each value, one at a time.
fruits = ["apple", "banana", "cherry"]

print("Example 1: for-loop over a list")
for fruit in fruits:
    print("I see a", fruit)
print()


# ----------------------------------------------------------
# EXAMPLE 2: Looping a set number of times with range()
# ----------------------------------------------------------
# range(5) gives the numbers 0, 1, 2, 3, 4  (stops BEFORE 5).
print("Example 2: range()")
for i in range(5):
    print("Count:", i)

# range(start, stop) and range(start, stop, step):
print("Even numbers 2 to 10:")
for n in range(2, 11, 2):      # start 2, stop before 11, step 2
    print(n)
print()


# ----------------------------------------------------------
# EXAMPLE 3: Looping over the characters of a string
# ----------------------------------------------------------
print("Example 3: looping over a string")
for letter in "Hi!":
    print(letter)
print()


# ----------------------------------------------------------
# EXAMPLE 4: A while-loop (repeat until a condition is False)
# ----------------------------------------------------------
# Use while when you don't know HOW MANY times in advance.
# IMPORTANT: something inside must eventually make the
# condition False, or the loop runs forever!
print("Example 4: while-loop countdown")
count = 3
while count > 0:
    print("T-minus", count)
    count = count - 1      # this step is what eventually stops the loop
print("Lift off!")
print()


# ----------------------------------------------------------
# EXAMPLE 5: break and continue
# ----------------------------------------------------------
# break    -> stop the loop completely
# continue -> skip the rest of THIS round, go to the next
print("Example 5: break and continue")

print("Stop at 3 (break):")
for i in range(1, 10):
    if i == 3:
        break              # leave the loop entirely
    print(i)

print("Skip 2 (continue):")
for i in range(1, 5):
    if i == 2:
        continue           # skip printing 2, keep going
    print(i)
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Looping with a running total + enumerate
# ----------------------------------------------------------
# A common pattern: build up a result while looping.
scores = [10, 20, 30]
total = 0
for score in scores:
    total = total + score      # add each score to the running total
print("Example 6: running total =", total)   # 60

# enumerate() gives you the index AND the value together:
names = ["Abdul", "Sara", "Ali"]
for index, name in enumerate(names):
    print(index, name)         # 0 Abdul / 1 Sara / 2 Ali
