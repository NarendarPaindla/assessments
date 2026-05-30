# Set in Python

## What is a Set?

A **Set** is used to represent a **group of unique values as a single entity**.

In simple words:

```text id="x8m2qt"
Set stores only unique values
```

---

# Features of Set

### 1. Unique Values Only

Duplicate values are:

```text id="m4x7vp"
Not Allowed
```

Example:

```python id="k2m9qt"
s = {10, 20, 10, 30, 20}

print(s)
```

### Output

```text id="r5x8pk"
{10, 20, 30}
```

Duplicates automatically removed.

---

### 2. Insertion Order Not Preserved

Unlike list:

```text id="u9m2rp"
Order is not guaranteed
```

Example:

```python id="f7x4qt"
s = {10, 40, 20, 30}

print(s)
```

Output order may vary.

---

### 3. Indexing and Slicing Not Supported

Since order is not fixed:

```text id="t1m8vx"
Indexing is not allowed
```

Wrong Example:

```python id="w6x2pk"
s = {10, 20, 30}

print(s[0])
```

### Output

```text id="n8m4qt"
TypeError
```

---

### 4. Heterogeneous Objects Allowed

Different datatypes are supported.

Example:

```python id="g5x9rp"
s = {10, "Python", 25.5, True}

print(s)
```

---

### 5. Mutable Nature

Set objects are:

```text id="p2m7vk"
Mutable
```

Meaning:

We can:

* Add elements
* Remove elements
* Modify indirectly

---

### 6. Curly Braces Used

Set elements are represented using:

```text id="j7x1qt"
{ }
```

with comma separation.

Example:

```python id="y4m8rp"
s = {10, 20, 30, 40}

print(s)

print(type(s))
```

### Output

```text id="h9x2pk"
{40, 10, 20, 30}

<class 'set'>
```

---

### 7. Mathematical Operations Supported

We can perform:

* Union
* Intersection
* Difference

on sets.

---

# Creation of Set Objects

---

## 1) Directly Using Curly Braces

### Example

```python id="q3m8qt"
s = {10, 20, 30, 40}

print(s)

print(type(s))
```

### Output

```text id="v6x2rp"
{40, 10, 20, 30}

<class 'set'>
```

---

# 2) Using `set()` Function

### Syntax

```python id="n9m4pk"
set(any_iterable)
```

---

## Example 1: Removing Duplicates

```python id="t5x8qt"
data = [10, 20, 30, 40, 10, 20]

s = set(data)

print(s)
```

### Output

```text id="m2x7rp"
{40, 10, 20, 30}
```

---

## Explanation

Duplicates:

```text id="k8m1vx"
10
20
```

automatically removed.

---

## Example 2: Using `range()`

```python id="u4x9qt"
s = set(range(5))

print(s)
```

### Output

```text id="g7m2pk"
{0, 1, 2, 3, 4}
```

---

# Important Note: Empty Set

We must be careful while creating an empty set.

---

## Wrong Way

```python id="r2x8rp"
s = {}

print(type(s))
```

### Output

```text id="x5m9qt"
<class 'dict'>
```

Reason:

```text id="f1x7vk"
{} creates Dictionary
```

---

## Correct Way

```python id="w8m2rp"
s = set()

print(s)

print(type(s))
```

### Output

```text id="p4x9qt"
set()

<class 'set'>
```

---

# Important Functions of Set

---

# 1) `add(x)` Function

## Definition

`add()` adds:

```text id="m7x4pk"
Single item
```

to the set.

### Syntax

```python id="q1m8qt"
set.add(item)
```

---

## Example

```python id="t9x2rp"
s = {10, 20, 30}

s.add(40)

print(s)
```

### Output

```text id="y5m7vk"
{40, 10, 20, 30}
```

---

## Explanation

Added:

```text id="n2x9qt"
40
```

to set.

---

# 2) `update(x, y, z)` Function

## Definition

`update()` adds:

```text id="g8m4rp"
Multiple items
```

to the set.

Arguments must be:

```text id="v1x7pk"
Iterable Objects
```

Examples:

* List
* Tuple
* Range
* Set

---

### Syntax

```python id="u6m2qt"
set.update(iterable1, iterable2)
```

---

## Example

```python id="k3x8rp"
s = {10, 20, 30}

data = [40, 50, 60]

s.update(data, range(5))

print(s)
```

### Output

```text id="r9m1qt"
{0,1,2,3,4,10,20,30,40,50,60}
```

---

## Explanation

Added:

```text id="m5x7vk"
40
50
60
```

and:

```text id="w2m9qt"
0,1,2,3,4
```

---

# Difference Between `add()` and `update()`

| `add()`                       | `update()`                 |
| ----------------------------- | -------------------------- |
| Adds single item              | Adds multiple items        |
| Takes one argument            | Takes multiple iterables   |
| Argument need not be iterable | Arguments must be iterable |

---

## Valid and Invalid Examples

### Valid

```python id="j8x2rp"
s.add(10)
```

Correct.

---

### Invalid

```python id="f4m9qt"
s.add(10, 20)
```

### Output

```text id="x1m7vk"
TypeError
```

Reason:

```text id="k6x4pk"
add() takes one argument only
```

---

### Invalid

```python id="g9m2qt"
s.update(10)
```

### Output

```text id="t3x8rp"
TypeError:
'int' object is not iterable
```

Reason:

```text id="v7m1qt"
10 is not iterable
```

---

### Valid

```python id="z5x9vk"
s.update(range(1,10,2))
```

---

# 3) `copy()` Function

## Definition

`copy()` returns:

```text id="r1m8qt"
Copy of the set
```

This is:

```text id="w4x7pk"
Cloning
```

---

## Example

```python id="k9m2rp"
s = {10, 20, 30}

s1 = s.copy()

print(s1)
```

### Output

```text id="m8x4qt"
{10, 20, 30}
```

---

# 4) `pop()` Function

## Definition

`pop()` removes and returns:

```text id="x2m7vk"
Random element
```

from the set.

Reason:

```text id="g5x8qt"
Set has no order
```

---

## Example

```python id="u9m1rp"
s = {40, 10, 30, 20}

print(s)

print(s.pop())

print(s)
```

### Output (May Vary)

```text id="h7x2qt"
{40,10,20,30}

40

{10,20,30}
```

---

## Important Note

Since set order changes:

```text id="n4m9pk"
Output may vary
```

---

# 5) `remove(x)` Function

## Definition

`remove()` removes:

```text id="q8x1rp"
Specified element
```

from the set.

### Syntax

```python id="p6m7qt"
set.remove(item)
```

---

## Example

```python id="z3x9vk"
s = {40, 10, 30, 20}

s.remove(30)

print(s)
```

### Output

```text id="r5m2qt"
{40,10,20}
```

---

## Important Rule

If item not present:

```text id="j1x8rp"
KeyError occurs
```

Example:

```python id="t7m4qt"
s.remove(100)
```

### Output

```text id="w9x2vk"
KeyError
```

---

# Key Takeaways

* Set stores:

```text id="k4m7rp"
Unique Values
```

* Duplicate values are removed automatically.
* Set does not support:

  * Indexing
  * Slicing
* Empty set:

```python id="g8x1qt"
set()
```

not:

```python id="v3m9pk"
{}
```

* `add()` → add one item
* `update()` → add multiple items
* `copy()` → clone set
* `pop()` → removes random item
* `remove()` → removes specific item
* `remove()` may cause:

```text id="u6x2rp"
KeyError
```

if item not found.


# 6) `discard(x)` Function

## Definition

`discard()` is used to:

```text id="m7x2qt"
Remove specified element
```

from the set.

### Syntax

```python id="p4m8vk"
set.discard(item)
```

---

## Important Rule

If item is:

```text id="u8m1rp"
Not present
```

then:

```text id="g5x9qt"
No error occurs
```

This is the main difference between:

```text id="r2x7pk"
remove()
discard()
```

---

## Example

```python id="w9m4qt"
s = {10, 20, 30}

s.discard(10)

print(s)

s.discard(50)

print(s)
```

### Output

```text id="k1x8rp"
{20, 30}

{20, 30}
```

---

## Explanation

### First Operation

```python id="f6m2vk"
s.discard(10)
```

Removes:

```text id="y3x9qt"
10
```

Result:

```text id="v7m1pk"
{20, 30}
```

---

### Second Operation

```python id="n5x4rp"
s.discard(50)
```

Since:

```text id="h9m2qt"
50 not present
```

No error occurs.

---

# Difference Between `remove()` and `discard()`

| `remove()`                       | `discard()`              |
| -------------------------------- | ------------------------ |
| Removes specified item           | Removes specified item   |
| Gives `KeyError` if item missing | No error if item missing |
| Strict removal                   | Safe removal             |

---

## Example Comparison

### `remove()`

```python id="j4x8vk"
s = {10,20,30}

s.remove(50)
```

### Output

```text id="q7m1rp"
KeyError
```

---

### `discard()`

```python id="z2m9qt"
s = {10,20,30}

s.discard(50)
```

### Output

```text id="p8x4pk"
No Error
```

---

# Difference Between `pop()`, `remove()`, and `discard()`

| Function    | Purpose                | Error                |
| ----------- | ---------------------- | -------------------- |
| `pop()`     | Removes random element | Error if set empty   |
| `remove()`  | Removes specified item | `KeyError` if absent |
| `discard()` | Removes specified item | No error             |

---

# 7) `clear()` Function

## Definition

`clear()` removes:

```text id="t6m2qt"
All elements
```

from the set.

### Syntax

```python id="x1m9rp"
set.clear()
```

---

## Example

```python id="r8x4qt"
s = {10, 20, 30}

print(s)

s.clear()

print(s)
```

### Output

```text id="g5m8pk"
{10, 20, 30}

set()
```

---

## Explanation

Before:

```text id="u9x1rp"
{10,20,30}
```

After:

```python id="n2m7qt"
s.clear()
```

All elements removed.

Result:

```text id="y7x4vk"
set()
```

---

# Mathematical Operations on Set

Set supports mathematical operations like:

1. `union()`
2. `intersection()`
3. `difference()`
4. `symmetric_difference()`

---

# 1) `union()`

## Definition

`union()` returns:

```text id="f3m8qt"
All elements
from both sets
```

### Syntax

```python id="k9x2rp"
x.union(y)
```

OR

```python id="p5m7qt"
x | y
```

---

## Example

```python id="m1x8vk"
x = {10, 20, 30, 40}

y = {30, 40, 50, 60}

print(x.union(y))

print(x | y)
```

### Output

```text id="r4m9pk"
{10,20,30,40,50,60}
```

---

## Explanation

Duplicate elements:

```text id="v8x2qt"
30
40
```

appear only once.

---

# 2) `intersection()`

## Definition

`intersection()` returns:

```text id="q2m7rp"
Common elements
```

present in both sets.

### Syntax

```python id="u6x4vk"
x.intersection(y)
```

OR

```python id="t9m1qt"
x & y
```

---

## Example

```python id="g7x8rp"
x = {10, 20, 30, 40}

y = {30, 40, 50, 60}

print(x.intersection(y))

print(x & y)
```

### Output

```text id="h4m2pk"
{40, 30}
```

---

## Explanation

Common elements:

```text id="k1x9qt"
30
40
```

---

# 3) `difference()`

## Definition

`difference()` returns:

```text id="n8m4rp"
Elements present in first set
but not in second set
```

### Syntax

```python id="y5x2qt"
x.difference(y)
```

OR

```python id="v7m1pk"
x - y
```

---

## Example

```python id="m2x9rp"
x = {10, 20, 30, 40}

y = {30, 40, 50, 60}

print(x.difference(y))

print(x - y)

print(y - x)
```

### Output

```text id="j8m4qt"
{10, 20}

{10, 20}

{50, 60}
```

---

## Explanation

### `x - y`

Present in `x` but not in `y`

Result:

```text id="g3x7pk"
10
20
```

---

### `y - x`

Present in `y` but not in `x`

Result:

```text id="q6m1rp"
50
60
```

---

# 4) `symmetric_difference()`

## Definition

Returns:

```text id="r1x9qt"
Elements present in
either x OR y
but not both
```

### Syntax

```python id="z4m8vk"
x.symmetric_difference(y)
```

OR

```python id="w9m2qt"
x ^ y
```

---

## Example

```python id="k5x7rp"
x = {10, 20, 30, 40}

y = {30, 40, 50, 60}

print(x.symmetric_difference(y))

print(x ^ y)
```

### Output

```text id="p8m1qt"
{10, 20, 50, 60}
```

---

## Explanation

Common elements removed:

```text id="u3x9pk"
30
40
```

Remaining:

```text id="n7m2rp"
10
20
50
60
```

---

# Membership Operators (`in`, `not in`)

These operators check whether an element exists in set or not.

---

## Example

```python id="f9x4qt"
s = set("python")

print(s)

print('p' in s)

print('z' in s)
```

### Output

```text id="m5x1vk"
{'p', 'y', 't', 'h', 'o', 'n'}

True

False
```

---

## Explanation

### `'p' in s`

Exists.

Output:

```text id="r8m2qt"
True
```

---

### `'z' in s`

Does not exist.

Output:

```text id="t4x7rp"
False
```

---

# Set Comprehension

## Definition

Python supports:

```text id="v2m9pk"
Set Comprehension
```

for creating sets in compact way.

### Syntax

```python id="y6x1qt"
{
 expression
 for item in iterable
}
```

---

## Example 1: Squares

```python id="g1m8rp"
s = {x * x for x in range(5)}

print(s)
```

### Output

```text id="h9x2qt"
{0, 1, 4, 9, 16}
```

---

## Example 2: Powers of 2

```python id="m4x7pk"
s = {2 ** x for x in range(2, 10, 2)}

print(s)
```

### Output

```text id="k7m1rp"
{16, 256, 64, 4}
```

---

# Set Does Not Support Indexing and Slicing

Wrong Example:

```python id="u8x4qt"
s = {10, 20, 30, 40}

print(s[0])
```

### Output

```text id="r3m9pk"
TypeError:
'set' object does not support indexing
```

---

Wrong Example:

```python id="p5x7rp"
print(s[1:3])
```

### Output

```text id="f2m8qt"
TypeError:
'set' object is not subscriptable
```

---

# Program: Eliminate Duplicates in List

## Approach 1: Using Set

```python id="w6x2vk"
values = eval(
    input("Enter List of Values: ")
)

result = list(set(values))

print(result)
```

### Example Input

```text id="n9m4rp"
[10,20,30,10,20,40]
```

### Output

```text id="x7m1qt"
[40, 10, 20, 30]
```

---

## Approach 2: Without Set

```python id="q8x5rp"
values = eval(
    input("Enter List of Values: ")
)

result = []

for value in values:

    if value not in result:
        result.append(value)

print(result)
```

### Output

```text id="v3m8qt"
[10, 20, 30, 40]
```

---

# Program: Print Different Vowels in a Word

```python id="z1x9pk"
word = input(
    "Enter word to search vowels: "
)

letters = set(word)

vowels = {'a', 'e', 'i', 'o', 'u'}

result = letters.intersection(vowels)

print(
    "The different vowels present in",
    word,
    "are",
    result
)
```

### Example Input

```text id="g5m2rp"
programming
```

### Output

```text id="r9x7qt"
The different vowels present in programming are {'a', 'i', 'o'}
```

---

# Key Takeaways

* `discard()` removes item without error.
* `remove()` gives `KeyError` if missing.
* `union()` → combines sets
* `intersection()` → common values
* `difference()` → uncommon values
* `symmetric_difference()` → values in one set only
* Set comprehension is supported.
* Set does not support:

  * Indexing
  * Slicing
* Membership operators:

  * `in`
  * `not in`
