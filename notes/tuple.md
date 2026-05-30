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
# Differences Between List and Tuple

Although **List** and **Tuple** look similar, there are some important differences between them.

Both:

* Store multiple values
* Preserve insertion order
* Allow duplicate values
* Support indexing and slicing
* Allow heterogeneous datatypes

But the main difference is:

```text id="m7x2qt"
List → Mutable

Tuple → Immutable
```

---

# Comparison Between List and Tuple

| Feature        | List                       | Tuple                  |
| -------------- | -------------------------- | ---------------------- |
| Representation | Uses square brackets `[ ]` | Uses parentheses `( )` |
| Mutability     | Mutable                    | Immutable              |
| Data Changes   | Can be modified            | Cannot be modified     |
| Best Use Case  | Frequently changing data   | Fixed data             |
| Dictionary Key | Cannot be used             | Can be used            |
| Performance    | Slightly slower            | Faster                 |

---

# 1) Representation Difference

## List

A list is a collection of comma-separated values enclosed inside:

```text id="p4m8vx"
Square Brackets [ ]
```

### Example

```python id="x9m2qt"
numbers = [10, 20, 30, 40]

print(numbers)
```

### Output

```text id="u3x7pk"
[10, 20, 30, 40]
```

---

## Tuple

A tuple is a collection of comma-separated values enclosed inside:

```text id="k8m1vp"
Parentheses ( )
```

### Example

```python id="w2x9rt"
numbers = (10, 20, 30, 40)

print(numbers)
```

### Output

```text id="g7m4qx"
(10, 20, 30, 40)
```

---

## Important Note

For tuples:

```text id="f1x8pk"
Parentheses are optional
```

Example:

```python id="n6m2qt"
t = 10, 20, 30
```

Still treated as:

```text id="z5x9rp"
Tuple
```

---

# 2) Mutability Difference

## List is Mutable

### Definition

After creating a list:

```text id="v8m4qt"
We can modify content
```

---

### Example

```python id="r3x7pk"
numbers = [10, 20, 30]

numbers[1] = 70

print(numbers)
```

### Output

```text id="t1m9vx"
[10, 70, 30]
```

---

## Explanation

Original:

```text id="p7x2qt"
[10, 20, 30]
```

Changed:

```python id="g4m8rp"
numbers[1] = 70
```

Updated:

```text id="x2m5vk"
[10, 70, 30]
```

Lists support modification.

---

## Tuple is Immutable

### Definition

After tuple creation:

```text id="u9m1qt"
We cannot change content
```

---

### Example

```python id="q8x4rp"
t = (10, 20, 30)

t[1] = 70
```

### Output

```text id="n5m8vx"
TypeError:
'tuple' object does not support item assignment
```

---

## Explanation

Tuple does not allow:

```text id="m2x7pk"
Modification
```

Hence:

```text id="w6m9qt"
Immutable
```

---

# 3) Fixed vs Changing Data

## Use List When Data Changes Frequently

Example:

```text id="f3x8rp"
Shopping Cart
Student Marks
Attendance List
```

Because values may:

```text id="r7m2vk"
Increase
Decrease
Change
```

---

## Use Tuple When Data is Fixed

Example:

```text id="t4x9qt"
Days of Week
Months
GPS Coordinates
```

Because values:

```text id="p1m7rp"
Never change
```

---

# 4) Dictionary Key Difference

## List Cannot Be Used as Dictionary Key

Reason:

```text id="j8x2vk"
List is Mutable
```

Dictionary keys must be:

```text id="z3m9qt"
Hashable
Immutable
```

---

### Wrong Example

```python id="g5x1rp"
data = {
    [1, 2]: "Python"
}
```

### Output

```text id="k7m4vx"
TypeError:
unhashable type: 'list'
```

---

## Tuple Can Be Used as Dictionary Key

Reason:

```text id="x9m2qt"
Tuple is Immutable
```

---

### Correct Example

```python id="u2x8rp"
data = {
    (1, 2): "Python"
}

print(data)
```

### Output

```text id="r5m7vk"
{(1, 2): 'Python'}
```

---

# Real-Life Analogy

Imagine:

### List = Whiteboard

You can:

```text id="n8x4qt"
Write
Erase
Modify
```

Again and again.

---

### Tuple = Printed Book

You:

```text id="m1x9rp"
Cannot change printed content
```

It stays fixed.

---

# Summary Table

| Property        | List         | Tuple       |
| --------------- | ------------ | ----------- |
| Symbol          | `[ ]`        | `( )`       |
| Mutable         | Yes          | No          |
| Immutable       | No           | Yes         |
| Size Change     | Allowed      | Not Allowed |
| Modify Elements | Yes          | No          |
| Dictionary Key  | No           | Yes         |
| Performance     | Slower       | Faster      |
| Best For        | Dynamic Data | Fixed Data  |

---

# Text Diagram

```text id="w4x2qt"
LIST

[10, 20, 30]

Can Change
     ↓

[10, 70, 30]
```

```text id="v7m8rp"
TUPLE

(10, 20, 30)

Cannot Change
      ↓

TypeError
```

---

# Key Takeaways

* List and Tuple both store multiple values.
* Main difference:

```text id="q9x1vk"
List → Mutable

Tuple → Immutable
```

* List uses:

```text id="u5m8qt"
[ ]
```

* Tuple uses:

```text id="p2x7rp"
( )
```

* Use **List** for changing data.
* Use **Tuple** for fixed data.
* Tuple can be used as:

```text id="t6m4vk"
Dictionary Key
```

because it is immutable.

