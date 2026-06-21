# ==========================================================
#  REFERENCE NOTE: FUNCTIONS vs METHODS
# ==========================================================
# A question that comes up a lot:
#   Why do we write   len(sentence)
#   but              messy.strip()  ?
#
# Because they are two different kinds of tools.
# ==========================================================


# ----------------------------------------------------------
#  FUNCTION  ->  len(sentence)
# ----------------------------------------------------------
# A function is a STANDALONE tool. It belongs to nobody.
# You call it by name and pass the data INSIDE the ().
#
#       len(sentence)     "Hey len, here is sentence. Measure it."
#
# Other common functions: print(...), type(...), input(...)
#
# Shape:  function_name( data )
#                        ^^^^  the data goes inside the parentheses


# ----------------------------------------------------------
#  METHOD  ->  messy.strip()
# ----------------------------------------------------------
# A method is a tool that BELONGS TO an object (like a string).
# You reach it with a DOT. The object before the dot is the
# thing being acted on, so the () can be empty.
#
#       messy.strip()     "Hey messy, clean yourself up."
#
# Other string methods: .upper(), .lower(), .replace(), .count()
#
# Shape:  object.method_name()
#         ^^^^^^ the data is before the dot (already given!)


# ----------------------------------------------------------
#  QUICK COMPARISON
# ----------------------------------------------------------
#   |  Function          |  Method             |
#   |--------------------|---------------------|
#   |  len(x)            |  x.strip()          |
#   |  "do this TO x"    |  "x, act on self"   |
#   |  data inside ()    |  data before the .  |
#   |  belongs to nobody |  belongs to object  |
#
# The giveaway is always the DOT:
#   if there is a "." before it  ->  it's a METHOD
#   otherwise                    ->  it's a FUNCTION


# ----------------------------------------------------------
#  METHODS CAN TAKE DATA TOO (when they need it)
# ----------------------------------------------------------
# The () is empty only when the method needs no extra info.
# When it does, the info goes inside the () as usual:
text = "banana milkshake"

print(text.replace(" ", "-"))   # replace needs: what -> with what
print(text.count("a"))          # count needs: which letter to count

# Run this file to see the two examples above in action:
#       python functions_vs_methods.py
