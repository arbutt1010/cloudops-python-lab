# ==========================================================
#  PYTHON CONDITIONS (if / elif / else) — A Tutorial
# ==========================================================
# A "condition" lets your program make DECISIONS.
# It checks if something is True, then runs code accordingly.
#
#       if <something is true>:
#           do this
#       else:
#           do that instead
#
# You've already used 'if' inside loops — now let's go deep.
# ==========================================================


# ----------------------------------------------------------
# EXAMPLE 1: A basic if statement
# ----------------------------------------------------------
# The code INSIDE the if (indented) only runs when the
# condition is True.
age = 20

print("Example 1: basic if")
if age >= 18:
    print("You are an adult.")     # runs only if age >= 18
print()


# ----------------------------------------------------------
# EXAMPLE 2: if / else  (two paths)
# ----------------------------------------------------------
# 'else' catches everything the 'if' did NOT.
temperature = 15

print("Example 2: if / else")
if temperature > 25:
    print("It's hot.")
else:
    print("It's not hot.")         # runs because 15 is not > 25
print()


# ----------------------------------------------------------
# EXAMPLE 3: if / elif / else  (many paths)
# ----------------------------------------------------------
# 'elif' = "else if". Python checks each in order and runs
# the FIRST one that is True, then skips the rest.
score = 75

print("Example 3: if / elif / else")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")              # first True one -> runs this
else:
    print("Grade: F")
print()


# ----------------------------------------------------------
# EXAMPLE 4: Comparison operators
# ----------------------------------------------------------
# Conditions are built from comparisons that give True/False:
#     ==  equal to          !=  not equal to
#     >   greater than      <   less than
#     >=  greater or equal  <=  less or equal
print("Example 4: comparisons")
print(5 == 5)     # True
print(5 != 3)     # True
print(10 > 20)    # False
print(7 <= 7)     # True

# NOTE: "=" assigns a value, "==" compares. Don't mix them up!
print()


# ----------------------------------------------------------
# EXAMPLE 5: Combining conditions with and / or / not
# ----------------------------------------------------------
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips True<->False
age = 25
has_ticket = True

print("Example 5: and / or / not")
if age >= 18 and has_ticket:
    print("You may enter.")        # both are True -> runs

if age < 13 or age > 65:
    print("You get a discount.")
else:
    print("Full price.")           # neither True -> runs

print(not True)                    # False
print()


# ----------------------------------------------------------
# EXAMPLE 6 (BONUS): Conditions inside a loop
# ----------------------------------------------------------
# This is where it all comes together: loop + condition.
numbers = [4, 7, 10, 15, 22]
print("Example 6: condition inside a loop")
for n in numbers:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
