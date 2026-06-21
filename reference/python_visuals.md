# 🎨 Python Visuals — ASCII Diagrams for the Concepts You Learned

Pictures of how things work "under the hood." Read top to bottom — it follows the
same order you learned: variables → strings → numbers → lists → dictionaries →
conditions → loops → the accumulator pattern.

> Tip: view this in your editor (monospace) so the diagrams line up. Pair it with
> https://pythontutor.com to watch the same ideas animate live.

---

## 1. Variables = a labeled box that holds a value

```
        name = "Abdul"              age = 25

        name                        age
      +-----------+               +-------+
      |  "Abdul"  |               |  25   |
      +-----------+               +-------+
        ^                           ^
      the LABEL                   the VALUE
   (how you find it)            (what's inside)

   "="  means: put the value on the right INTO the box on the left.
```

Reassigning replaces what's in the box:

```
   score = 10            score = 50            score = score + 25
   +------+              +------+              +------+
   |  10  |   ----->     |  50  |   ----->     |  75  |
   +------+              +------+              +------+
   (old value thrown away each time)
```

---

## 2. Data types — what kind of value is in the box

```
   int        float        str           bool         list            dict
  +----+    +------+    +---------+     +------+    +-----------+   +-----------+
  | 25 |    | 3.14 |    | "hello" |     | True |   | [1, 2, 3] |   | {"a": 1}  |
  +----+    +------+    +---------+     +------+    +-----------+   +-----------+
  whole     decimal      text          yes/no      many items      key->value
```

---

## 3. Strings — every character has an INDEX (position)

```
        P    y    t    h    o    n
      +----+----+----+----+----+----+
      | P  | y  | t  | h  | o  | n  |
      +----+----+----+----+----+----+
        0    1    2    3    4    5      <- index counts from the START (at 0!)
       -6   -5   -4   -3   -2   -1      <- negative counts from the END

   word[0]  -> 'P'        (first)
   word[-1] -> 'n'        (last)
   word[0:3]-> 'Pyt'      (slice: 0,1,2 ... the 3 is NOT included!)
                ^^^^ start at 0, STOP BEFORE 3
```

---

## 4. Lists — ordered boxes, found by index (and you CAN change them)

```
   fruits = ["apple", "banana", "cherry"]

      index:    0          1          2
            +---------+----------+----------+
   fruits = |  apple  |  banana  |  cherry  |
            +---------+----------+----------+

   fruits[1]            -> "banana"
   fruits.append("kiwi")-> adds a new box at the END
   fruits[0] = "mango"  -> CHANGES box 0   (lists are MUTABLE)
```

---

## 5. Dictionaries — look up by KEY, not by position

```
   student = {"name": "Abdul", "age": 25, "grade": "A"}

        KEY            VALUE
     +---------+    +---------+
     | "name"  | -> | "Abdul" |
     +---------+    +---------+
     | "age"   | -> |   25    |
     +---------+    +---------+
     | "grade" | -> |   "A"   |
     +---------+    +---------+

   student["name"]  -> "Abdul"     (use the KEY, like a real dictionary word)
   student["city"] = "Lahore"      (add a new key->value pair)
```

**List vs Dictionary** — the key difference:

```
   LIST: find by POSITION number        DICT: find by LABEL (key)
        fruits[0]                              student["name"]
        "the 0th item"                         "the item labeled name"
```

---

## 6. Conditions — if / elif / else is a fork in the road

```
                      ┌─────────────────────┐
                      │  score >= 90 ?      │
                      └─────────┬───────────┘
                       True ◄───┴───► False
                        │              │
                   print "A"     ┌─────────────────────┐
                                 │  score >= 80 ?      │
                                 └─────────┬───────────┘
                                  True ◄───┴───► False
                                   │             │
                              print "B"     ┌─────────────────────┐
                                            │  score >= 70 ?      │
                                            └─────────┬───────────┘
                                             True ◄───┴───► False
                                              │             │
                                         print "C"      print "F"  (else)

   Python checks top-to-bottom and runs the FIRST True branch, then SKIPS the rest.
```

---

## 7. The `for` loop — do something once per item

```
   for fruit in ["apple", "banana", "cherry"]:
       print(fruit)

   ┌─────────────────────────────────────────────┐
   │  any items left in the list?                │◄──────────┐
   └───────────────┬─────────────────────────────┘           │
            Yes ◄──┴──► No ──► loop ends, continue below      │
             │                                                │
             ▼                                                │
   take the next item, call it 'fruit'                        │
             │                                                │
             ▼                                                │
   run the loop body (print fruit) ──────────────────────────┘

   Round 1: fruit = "apple"
   Round 2: fruit = "banana"
   Round 3: fruit = "cherry"
   (then stops — no items left)
```

---

## 8. The `while` loop — repeat AS LONG AS a condition is True

```
   count = 3
   while count > 0:
       print(count)
       count = count - 1        # <- THIS is what eventually stops it

   ┌──────────────────────┐
   │   count > 0 ?        │◄────────────────┐
   └──────────┬───────────┘                 │
       True ◄─┴─► False ──► loop ends        │
        │                                    │
        ▼                                    │
   print(count)                              │
        │                                    │
        ▼                                    │
   count = count - 1  ──────────────────────┘

   count: 3 -> print 3 -> 2 -> print 2 -> 1 -> print 1 -> 0 -> STOP

   ⚠️  If you forget "count = count - 1", count stays 3 forever = INFINITE LOOP
```

---

## 9. break vs continue

```
   BREAK = leave the loop completely        CONTINUE = skip THIS round only

   for i in 1..5:                           for i in 1..5:
       if i == 3: break                         if i == 3: continue
       print(i)                                 print(i)

   1                                        1
   2                                        2
   (i==3 -> jump OUT)                       (i==3 -> skip, go to next)
   [loop ended]                             4
                                            5
```

---

## 10. ⭐ The Accumulator Pattern (your key skill!)

A variable that **builds up** a result as the loop runs.

```
   total = 0
   for n in [10, 20, 30]:
       total = total + n

   step      n       total (the accumulator grows)
   -----   -----   -------------------------------
   start     -        0     +-----+
   round 1   10       10     | +10 |
   round 2   20       30     | +20 |
   round 3   30       60     | +30 |
                            =  60   <- final answer, AFTER the loop

         0  ──+10──►  10  ──+20──►  30  ──+30──►  60
```

A **counter** is the same idea, adding 1 instead of a value:

```
   passed = 0
   for score in [88, 42, 50, 71, 33]:
       if score >= 50:
           passed = passed + 1

   score:   88     42      50      71      33
   >= 50?   YES    no      YES     YES     no
   passed:   1      1       2       3       3   <- final: 3
            (+1)   (same)  (+1)    (+1)    (same)
```

**Track-the-best** (find biggest) — the box keeps the champion so far:

```
   biggest = first item
   for n in [23, 88, 41, 9, 60]:
       if n > biggest: biggest = n

   n:        23     88      41      9       60
   biggest:  23     88      88      88      88   <- only changes when beaten
                    ▲
              new champion!
```

---

## 11. Functions vs Methods (the dot is the giveaway)

```
   FUNCTION                          METHOD
   len(word)                         word.upper()
       └── data INSIDE the ( )           └── data is BEFORE the dot

   +----------------------+          +-----------------------------+
   | stands alone         |          | belongs to a value (word)   |
   | len(x), print(x)     |          | x.upper(), list.append()    |
   | "do this TO x"       |          | "x, do this to yourself"    |
   +----------------------+          +-----------------------------+

   Rule: see a DOT before it ( . ) -> it's a METHOD.  Otherwise -> FUNCTION.
```

---

## 12. Mutable vs Immutable (can it be changed?)

```
   IMMUTABLE (cannot change in place)     MUTABLE (can change in place)
   strings, numbers, tuples               lists, dicts

   name = "abdul"                         nums = [1, 2, 3]
   name[0] = "X"   --> ❌ ERROR           nums[0] = 99   --> ✅ works
   name = name.upper()  ✅ (NEW string)   nums.append(4) --> ✅ works

   Immutable -> methods RETURN a new value (assign it: x = x.upper())
   Mutable   -> methods CHANGE the original (don't assign: nums.sort())
```

---

> 🎯 Want these to *move*? Paste any of the code snippets above into
> **https://pythontutor.com** and press Next — you'll watch the boxes fill in
> and the arrows move exactly like these diagrams, but live.
