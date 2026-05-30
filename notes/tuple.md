# Tuple in Python

## What is a Tuple?

A **Tuple** is almost the same as a **List**, but the main difference is:

```text id="x8m2qt"
Tuple is Immutable
```

Meaning:

Once a tuple is created:

```text id="p4x7vk"
We cannot modify its content
```

---

## Features of Tuple

### 1. Tuple is Immutable

After creation:

```text id="g7m2vp"
No changes are allowed
```

We cannot:

* Add elements
* Remove elements
* Modify elements

---

### 2. Read-Only Version of List

Since modification is not possible:

```text id="u9x4pk"
Tuple is called
Read-Only List
```

---

### 3. Best for Fixed Data

If data:

```text id="k2m8qt"
Never changes
```

then use:

```text id="v6x1rp"
Tuple
```

Examples:

* Days of week
* Months
* Fixed settings

---

### 4. Insertion Order Preserved

Tuple stores elements in the same order.

Example:

```python id="r8m4vx"
t = (10, 20, 30)

print(t)
```

### Output

```text id="n5x9pk"
(10, 20, 30)
```

---

### 5. Duplicate Values Allowed

Example:

```python id="q7m2qt"
t = (10, 20, 10, 30)

print(t)
```

### Output

```text id="w4x8rp"
(10, 20, 10, 30)
```

Duplicates allowed.

---

### 6. Heterogeneous Objects Allowed

Tuple supports multiple datatypes.

Example:

```python id="j1m9vp"
t = (10, "Python", 25.5, True)

print(t)
```

### Output

```text id="y6x2qt"
(10, 'Python', 25.5, True)
```

---

### 7. Supports Indexing

Tuple supports:

* Positive Index
* Negative Index

```text id="f9m4pk"
Positive → Left to Right

Negative → Right to Left
```

---

### 8. Tuple Uses Parentheses

Tuple elements are represented using:

```text id="r3x8vp"
()
```

with comma separator.

Example:

```python id="m8q2rt"
t = (10, 20, 30, 40)

print(t)

print(type(t))
```

### Output

```text id="p5x7vk"
(10, 20, 30, 40)

<class 'tuple'>
```

---

## Parentheses are Optional

Example:

```python id="u2m9qt"
t = 10, 20, 30

print(type(t))
```

### Output

```text id="v7x1rp"
<class 'tuple'>
```

---

# Important Note: Single Value Tuple

We must be careful while creating:

```text id="x4m8pk"
Single Value Tuple
```

---

## Wrong Example

```python id="k9m2vp
```
# Important Functions of Tuple

Tuple supports several useful functions.

Common tuple functions are:

1. `len()`
2. `count()`
3. `index()`
4. `sorted()`
5. `min()` and `max()`
6. `cmp()` (Python 2 only)

---

# 1) `len()` Function

## Definition

`len()` returns the **number of elements present in the tuple**.

### Syntax

```python
len(tuple_name)
```

---

## Example

```python
t = (10, 20, 30, 40)

print(len(t))
```

### Output

```text
4
```

---

## Explanation

Tuple contains:

```text
10
20
30
40
```

Total elements:

```text
4
```

So:

```python
len(t)
```

returns:

```text
4
```

---

# 2) `count()` Function

## Definition

`count()` returns the **number of occurrences of a given element in the tuple**.

### Syntax

```python
tuple.count(element)
```

---

## Example

```python
t = (10, 20, 10, 10, 20)

print(t.count(10))
```

### Output

```text
3
```

---

## Explanation

Tuple:

```text
(10, 20, 10, 10, 20)
```

Occurrences of:

```text
10
```

Count:

```text
3 times
```

Hence:

```python
t.count(10)
```

returns:

```text
3
```

---

# 3) `index()` Function

## Definition

`index()` returns the **index of first occurrence** of the specified element.

### Syntax

```python
tuple.index(element)
```

---

## Example

```python
t = (10, 20, 10, 10, 20)

print(t.index(10))

print(t.index(30))
```

### Output

```text
0

ValueError:
tuple.index(x): x not in tuple
```

---

## Explanation

### First Occurrence

Tuple:

```text
(10, 20, 10, 10, 20)
```

First `10` is at:

```text
index 0
```

So:

```python
t.index(10)
```

returns:

```text
0
```

---

### Item Not Present

```python
t.index(30)
```

Since:

```text
30 does not exist
```

Python gives:

```text
ValueError
```

---

## Important Note

Before using `index()`:

Check item exists or not.

Example:

```python
if 30 in t:
    print(t.index(30))
```

---

# 4) `sorted()` Function

## Definition

`sorted()` is used to **sort tuple elements according to default natural sorting order**.

### Syntax

```python
sorted(tuple_name)
```

---

## Example

```python
t = (40, 10, 30, 20)

t1 = sorted(t)

print(t1)

print(t)
```

### Output

```text
[10, 20, 30, 40]

(40, 10, 30, 20)
```

---

## Important Point

`sorted()`:

```text
Does not modify original tuple
```

Because tuple is:

```text
Immutable
```

Also:

```text
sorted() returns a list
```

---

## Explanation

Original tuple:

```text
(40, 10, 30, 20)
```

Sorted result:

```text
[10, 20, 30, 40]
```

Original tuple remains unchanged.

---

# Sorting in Reverse Order

We can sort in reverse order using:

```python
reverse=True
```

---

## Example

```python
t = (40, 10, 30, 20)

t1 = sorted(t, reverse=True)

print(t1)
```

### Output

```text
[40, 30, 20, 10]
```

---

## Explanation

By default:

```text
Ascending Order
```

Using:

```python
reverse=True
```

gives:

```text
Descending Order
```

---

# 5) `min()` and `max()` Functions

## Definition

These functions return:

* Minimum value
* Maximum value

according to default natural sorting order.

---

## Example

```python
t = (40, 10, 30, 20)

print(min(t))

print(max(t))
```

### Output

```text
10

40
```

---

## Explanation

Minimum value:

```text
10
```

Maximum value:

```text
40
```

---

# 6) `cmp()` Function

## Definition

`cmp()` compares elements of two tuples.

---

## Rules of `cmp()`

### If both tuples are equal

Returns:

```text
0
```

---

### If first tuple is smaller

Returns:

```text
-1
```

---

### If first tuple is greater

Returns:

```text
+1
```

---

## Example

```python
t1 = (10, 20, 30)

t2 = (40, 50, 60)

t3 = (10, 20, 30)

print(cmp(t1, t2))

print(cmp(t1, t3))

print(cmp(t2, t3))
```

### Output

```text
-1

0

+1
```

---

## Important Note

`cmp()`:

```text
Available only in Python 2
```

Not supported in:

```text
Python 3
```

---

# Tuple Packing and Unpacking

---

# 1) Tuple Packing

## Definition

Creating a tuple by packing multiple variables together is called:

```text
Tuple Packing
```

---

## Example

```python
a = 10
b = 20
c = 30
d = 40

t = a, b, c, d

print(t)
```

### Output

```text
(10, 20, 30, 40)
```

---

## Explanation

Variables:

```text
a
b
c
d
```

are packed into:

```text
Single Tuple
```

This process is called:

```text
Tuple Packing
```

---

# 2) Tuple Unpacking

## Definition

Assigning tuple values to different variables is called:

```text
Tuple Unpacking
```

---

## Example

```python
t = (10, 20, 30, 40)

a, b, c, d = t

print("a =", a)

print("b =", b)

print("c =", c)

print("d =", d)
```

### Output

```text
a = 10

b = 20

c = 30

d = 40
```

---

## Explanation

Tuple values are distributed into variables.

```text
10 → a

20 → b

30 → c

40 → d
```

---

## Important Rule

At the time of unpacking:

```text
Number of variables
=
Number of values
```

Otherwise:

```text
ValueError occurs
```

---

## Wrong Example

```python
t = (10, 20, 30, 40)

a, b, c = t
```

### Output

```text
ValueError:
too many values to unpack
```

---

# Tuple Comprehension

## Important Note

Python does **not support tuple comprehension directly**.

Instead:

```text
Generator Object
```

is created.

---

## Example

```python
t = (x * x for x in range(1, 6))

print(type(t))

for x in t:
    print(x)
```

### Output

```text
<class 'generator'>

1
4
9
16
25
```

---

## Explanation

This:

```python
(x*x for x in range(1,6))
```

does not create tuple.

It creates:

```text
Generator Object
```

---

# Program: Sum and Average of Tuple Elements

## Problem Statement

Write a program to:

```text
Take tuple input
Find sum and average
```

---

## Program

```python
t = eval(input("Enter Tuple of Numbers: "))

length = len(t)

total = 0

for value in t:
    total = total + value

print("The Sum =", total)

print("The Average =", total / length)
```

---

## Example Input

```text
(10,20,30,40)
```

### Output

```text
The Sum = 100

The Average = 25.0
```

---

## Step-by-Step Explanation

### Length

```python
len(t)
```

gives total elements.

---

### Loop

```python
for value in t
```

adds all values.

---

### Average Formula

```python
sum / length
```

---

# Key Takeaways

* `len()` → total elements
* `count()` → number of occurrences
* `index()` → first occurrence position
* `sorted()` → sorts tuple and returns list
* `min()` → smallest value
* `max()` → largest value
* `cmp()` → only in Python 2
* Tuple packing → combining variables
* Tuple unpacking → splitting tuple into variables
* Number of variables and values must match.
* Tuple comprehension creates:

```text
Generator Object
```

not tuple.

