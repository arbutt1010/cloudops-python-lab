# 🐍 Abdul's Python Vocabulary & Reference

A living cheat-sheet of Python's most useful **functions, methods, and terms**.
Skim it to review what you know and preview what's next.

**Legend:**  ✅ = you've learned it   ·   🔜 = coming later   ·   ⭐ = especially handy

---

## 1. Built-in Functions (no import needed)

These come ready to use. Called like `name(arguments)` — data goes **inside** the `()`.

### Everyday essentials
| Function | What it does | Example | Status |
|----------|--------------|---------|--------|
| `print(x)` | Show something on screen | `print("hi")` | ✅ ⭐ |
| `len(x)` | How many items / characters | `len("cat")` → 3 | ✅ ⭐ |
| `type(x)` | What kind of value it is | `type(5)` → `int` | ✅ |
| `input(msg)` | Read text the user types (always a string!) | `name = input("Name? ")` | 🔜 ⭐ |
| `range(a, b, step)` | A sequence of numbers for looping | `range(1, 5)` → 1,2,3,4 | ✅ ⭐ |
| `help(x)` | Show built-in documentation | `help(str)` | 🔜 |

### Converting types
| Function | What it does | Example | Status |
|----------|--------------|---------|--------|
| `int(x)` | Make a whole number | `int("5")` → 5 | ✅ ⭐ |
| `float(x)` | Make a decimal number | `float("3.5")` → 3.5 | ✅ |
| `str(x)` | Make text | `str(100)` → `"100"` | ✅ ⭐ |
| `bool(x)` | Make True/False | `bool(0)` → False | ✅ |
| `list(x)` | Make a list | `list("ab")` → `['a','b']` | ✅ |
| `dict(...)` | Make a dictionary | `dict(a=1)` → `{'a':1}` | ✅ |

### Numbers & math
| Function | What it does | Example | Status |
|----------|--------------|---------|--------|
| `sum(items)` | Total of all numbers | `sum([1,2,3])` → 6 | ✅ ⭐ |
| `max(items)` | Biggest | `max([4,9,2])` → 9 | ✅ ⭐ |
| `min(items)` | Smallest | `min([4,9,2])` → 2 | ✅ ⭐ |
| `abs(x)` | Distance from 0 (drops the minus) | `abs(-8)` → 8 | ✅ |
| `round(x, n)` | Round to n decimal places | `round(3.14159, 2)` → 3.14 | ✅ |
| `pow(a, b)` | a to the power b (same as `a ** b`) | `pow(2, 3)` → 8 | 🔜 |

### Looping helpers ⭐
| Function | What it does | Example | Status |
|----------|--------------|---------|--------|
| `enumerate(items)` | Gives index + value together | `for i, v in enumerate(x):` | ✅ ⭐ |
| `sorted(items)` | Returns a NEW sorted list | `sorted([3,1,2])` → `[1,2,3]` | 🔜 ⭐ |
| `reversed(items)` | Items in reverse order | `list(reversed([1,2]))` → `[2,1]` | 🔜 |
| `zip(a, b)` | Pair up two lists item-by-item | `zip([1,2],["a","b"])` | 🔜 ⭐ |

### True/False checkers
| Function | What it does | Example | Status |
|----------|--------------|---------|--------|
| `any(items)` | True if AT LEAST ONE is true | `any([False, True])` → True | 🔜 |
| `all(items)` | True only if ALL are true | `all([True, True])` → True | 🔜 |

### Advanced (you'll meet these later)
| Function | What it does | Status |
|----------|--------------|--------|
| `map(f, items)` | Apply a function to every item | 🔜 |
| `filter(f, items)` | Keep only items that pass a test | 🔜 |
| `open(file)` | Open a file to read/write | 🔜 |

---

## 2. String Methods  (text.method())

Methods belong to a value — reached with a **dot**. Strings are **immutable**, so
these return a NEW string (assign the result: `x = x.strip()`).

| Method | What it does | Example | Status |
|--------|--------------|---------|--------|
| `.upper()` | ALL CAPS | `"hi".upper()` → `"HI"` | ✅ |
| `.lower()` | all lowercase | `"HI".lower()` → `"hi"` | ✅ |
| `.strip()` | Remove spaces at both ends | `"  hi  ".strip()` → `"hi"` | ✅ ⭐ |
| `.replace(a, b)` | Swap part of the text | `"cat".replace("c","b")` → `"bat"` | ✅ |
| `.split()` | Break text into a list | `"a b".split()` → `['a','b']` | ✅ ⭐ |
| `.join(list)` | Glue a list into text | `"-".join(['a','b'])` → `"a-b"` | 🔜 ⭐ |
| `.startswith(x)` | Does it start with x? | `"Abdul".startswith("A")` → True | ✅ |
| `.endswith(x)` | Does it end with x? | `"file.py".endswith(".py")` → True | ✅ |
| `.count(x)` | How many times x appears | `"banana".count("a")` → 3 | ✅ |
| `.find(x)` | Index where x starts (-1 if absent) | `"hi".find("i")` → 1 | ✅ |
| `.title()` | Capitalize Each Word | `"abc def".title()` | 🔜 |
| `.isdigit()` | Is it all digits? | `"123".isdigit()` → True | 🔜 |

**f-strings** ⭐ ✅ — the best way to build text: `f"Hi {name}, you are {age}"`.

---

## 3. List Methods  (mylist.method())

Lists are **mutable** — these change the list IN PLACE (don't assign the result).

| Method | What it does | Example | Status |
|--------|--------------|---------|--------|
| `.append(x)` | Add x to the END | `nums.append(5)` | ✅ ⭐ |
| `.insert(i, x)` | Add x at position i | `nums.insert(0, 5)` | ✅ |
| `.remove(x)` | Remove the first x by value | `nums.remove(5)` | ✅ |
| `.pop()` | Remove & return the LAST item | `last = nums.pop()` | ✅ |
| `.sort()` | Sort the list in place | `nums.sort()` | ✅ ⭐ |
| `.reverse()` | Flip order in place | `nums.reverse()` | 🔜 |
| `.index(x)` | Position of x | `["a","b"].index("b")` → 1 | 🔜 |
| `.count(x)` | How many x in the list | `[1,1,2].count(1)` → 2 | 🔜 |
| `.clear()` | Empty the list | `nums.clear()` | 🔜 |

⚠️ `.sort()` returns `None` — never write `nums = nums.sort()`.

---

## 4. Dictionary Methods  (mydict.method())

| Method | What it does | Example | Status |
|--------|--------------|---------|--------|
| `.get(key)` | Value for key, or None (no crash) | `d.get("x")` | ✅ ⭐ |
| `.keys()` | All the keys | `d.keys()` | ✅ |
| `.values()` | All the values | `sum(d.values())` | ✅ ⭐ |
| `.items()` | Key+value pairs (for looping) | `for k, v in d.items():` | ✅ ⭐ |
| `.pop(key)` | Remove a key, return its value | `d.pop("x")` | 🔜 |
| `.update(other)` | Merge another dict in | `d.update({"y":2})` | 🔜 |

---

## 5. Operators

| Operator | Meaning | Example | Status |
|----------|---------|---------|--------|
| `+ - * /` | add, subtract, multiply, divide | `7 / 2` → 3.5 | ✅ |
| `//` | Floor divide (drop decimal) | `7 // 2` → 3 | ✅ ⭐ |
| `%` | Remainder (modulo) | `7 % 2` → 1 | ✅ ⭐ |
| `**` | Power | `2 ** 3` → 8 | ✅ |
| `==` `!=` | equal / not equal | `5 == 5` → True | ✅ ⭐ |
| `>` `<` `>=` `<=` | comparisons | `5 >= 3` → True | ✅ |
| `and` `or` `not` | combine conditions | `a >= 18 and b` | ✅ ⭐ |
| `in` | Is it inside? | `"a" in "cat"` → True | ✅ ⭐ |
| `=` | **assign** a value (not compare!) | `x = 5` | ✅ |

💡 The #1 beginner trap: `=` assigns, `==` compares.

---

## 6. Data Types

| Type | What it is | Example | Status |
|------|-----------|---------|--------|
| `int` | Whole number | `25` | ✅ |
| `float` | Decimal number | `3.14` | ✅ |
| `str` | Text | `"hello"` | ✅ |
| `bool` | True / False | `True` | ✅ |
| `list` | Ordered collection `[ ]` | `[1, 2, 3]` | ✅ |
| `dict` | Key→value pairs `{ }` | `{"a": 1}` | ✅ |
| `tuple` | Like a list but UNCHANGEABLE `( )` | `(1, 2)` | 🔜 |
| `set` | Unique items, no duplicates | `{1, 2, 3}` | 🔜 |
| `None` | "nothing / no value" | `x = None` | 🔜 |

---

## 7. Keywords & Terminology (the words we use)

| Term | Plain-English meaning | Status |
|------|----------------------|--------|
| **variable** | A named box that stores a value | ✅ |
| **assign** | Put a value into a variable (`=`) | ✅ |
| **string** | Text in quotes | ✅ |
| **index** | A position number (starts at 0) | ✅ |
| **slice** | A piece of a list/string `x[1:3]` | ✅ |
| **loop / iterate** | Repeat code over each item | ✅ |
| **condition** | A True/False test (`if`) | ✅ |
| **boolean** | A True or False value | ✅ |
| **mutable** | CAN be changed (lists, dicts) | ✅ |
| **immutable** | CANNOT be changed (strings, numbers, tuples) | ✅ |
| **accumulator** | A variable you build up in a loop (total/counter) | ✅ ⭐ |
| **function** | A reusable named block of code (`def`) | 🔜 ⭐ |
| **argument / parameter** | The input you pass to a function | 🔜 |
| **return** | The value a function hands back | 🔜 |
| **method** | A function that belongs to a value (`x.upper()`) | ✅ |
| **comprehension** | A short one-line way to build a list | 🔜 |
| **module / library** | A file of ready-made code you import | 🔜 |
| **exception / error** | When code crashes; handled with `try/except` | 🔜 |
| **comment** | A note for humans, ignored by Python (`#`) | ✅ |

---

## 8. Keywords you'll type (reserved words)

`if` ✅ · `elif` ✅ · `else` ✅ · `for` ✅ · `while` ✅ · `in` ✅ · `and` ✅ ·
`or` ✅ · `not` ✅ · `break` ✅ · `continue` ✅ · `True`/`False` ✅ · `None` 🔜 ·
`def` 🔜 · `return` 🔜 · `import` 🔜 · `try`/`except` 🔜 · `class` 🔜 · `with` 🔜

---

## 9. Tools & Ecosystem (the world around Python)

| Tool | What it is | Status |
|------|-----------|--------|
| **Python interpreter** | The program that runs your `.py` files (`python file.py`) | ✅ |
| **IDE / editor** | Where you write code (you use VS Code) | ✅ |
| **REPL** | Interactive prompt — type `python` to try code live | 🔜 |
| **`import`** | Pull in extra code: `import math`, `import random` | 🔜 ⭐ |
| **Standard library** | Hundreds of built-in modules (`math`, `random`, `datetime`, `os`) | 🔜 |
| **`pip`** | Installs extra packages: `pip install requests` | 🔜 |
| **virtual environment** | An isolated set of packages per project | 🔜 |
| **`print()` debugging** | Add prints to see what variables hold (your best friend!) | ✅ ⭐ |

### Handy standard-library modules to know later 🔜
| Module | Gives you |
|--------|-----------|
| `math` | `sqrt`, `pi`, `ceil`, `floor`... |
| `random` | random numbers / picks (`random.choice`) |
| `datetime` | dates and times |
| `os` / `pathlib` | files and folders |
| `json` | read/write JSON data |

---

## 📌 How to use this file
- **Reviewing?** Skim the ✅ rows — you should recognize every one.
- **Curious what's next?** The 🔜 rows are your roadmap. Functions (`def`),
  `sorted`, `zip`, comprehensions, and `import` are the most useful next steps.
- This is a **living document** — as you learn each 🔜 item, change it to ✅.
