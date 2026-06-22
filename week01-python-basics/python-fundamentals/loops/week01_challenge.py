# ==========================================================
#  WEEK 01 CHALLENGE — Coffee Shop Daily Sales Report
# ==========================================================
#  Solve this on your own. No hints, no TODOs, no starter
#  code below — just the problem and the exact output you
#  must produce. Write all the code yourself.
# ==========================================================


# ----------------------------------------------------------
#  THE SCENARIO
# ----------------------------------------------------------
#  You run a small coffee shop. Below is one day of orders.
#  Each order is a dictionary with the customer's name, the
#  drink they bought, the price, and how many they ordered.
#
#  Use THIS data exactly (do not change it):

orders = [
    {"customer": "Abdul", "drink": "Latte",      "price": 4.50, "qty": 2},
    {"customer": "Sara",  "drink": "Espresso",   "price": 3.00, "qty": 1},
    {"customer": "Ali",   "drink": "Cappuccino", "price": 4.00, "qty": 3},
    {"customer": "Bilal", "drink": "Latte",      "price": 4.50, "qty": 1},
    {"customer": "Amna",  "drink": "Mocha",      "price": 5.50, "qty": 2},
    {"customer": "Sara",  "drink": "Mocha",      "price": 5.50, "qty": 1},
    {"customer": "Ali",   "drink": "Espresso",   "price": 3.00, "qty": 2},
]


# ----------------------------------------------------------
#  WHAT YOUR PROGRAM MUST PRINT
# ----------------------------------------------------------
#  Produce output that looks EXACTLY like this:
#
#  ===== ORDER RECEIPTS =====
#  Abdul : 2 x Latte      = $9.00
#  Sara  : 1 x Espresso   = $3.00
#  Ali   : 3 x Cappuccino = $12.00
#  Bilal : 1 x Latte      = $4.50
#  Amna  : 2 x Mocha      = $11.00
#  Sara  : 1 x Mocha      = $5.50
#  Ali   : 2 x Espresso   = $6.00
#
#  ------ DAILY STATS ------
#  Total drinks sold : 12
#  Total revenue     : $51.00
#  Average order value: $7.29
#  Biggest order     : Ali ($12.00)
#  Orders over $5    : 4
#
#  ---- DRINKS SOLD BY TYPE ----
#  Latte: 3
#  Espresso: 3
#  Cappuccino: 3
#  Mocha: 3
#
#  ---- LOYALTY ----
#  VIP customers (2+ orders): Sara, Ali
#
#
#  RULES YOUR NUMBERS MUST FOLLOW:
#   - Line total      = price * qty
#   - Total drinks    = sum of every qty
#   - Total revenue   = sum of every line total
#   - Average order   = total revenue / number of orders, rounded to 2 decimals
#   - Biggest order   = the single order with the highest line total
#   - Orders over $5  = how many line totals are strictly greater than 5.00
#   - Drinks by type  = how many drinks (by qty) of each drink name were sold
#   - VIP customers   = anyone who appears in 2 or more orders
#
#  Money must always show 2 decimal places (e.g. $9.00, not $9.0).
#
# ----------------------------------------------------------
#  Write your solution below this line.
# ----------------------------------------------------------

print(orders) # Our Dictionary name is orders, we can print it to see the data structure.
#  ===== ORDER RECEIPTS =====
#  Abdul : 2 x Latte      = $9.00
#  Sara  : 1 x Espresso   = $3.00
#  Ali   : 3 x Cappuccino = $12.00
#  Bilal : 1 x Latte      = $4.50
#  Amna  : 2 x Mocha      = $11.00
#  Sara  : 1 x Mocha      = $5.50
#  Ali   : 2 x Espresso   = $6.00
print("===== ORDER RECEIPTS =====")
# Code here 

print("------ DAILY STATS ------")
# Code here

print("---- DRINKS SOLD BY TYPE ----")
# Code here

print("---- LOYALTY ----")
# Code here