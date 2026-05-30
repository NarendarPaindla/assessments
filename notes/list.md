# Python Lists

## What is a List?

A **List** is used to store a group of individual objects as a single entity where:

* **Insertion order is preserved**
* **Duplicate values are allowed**
* **Different datatype elements are allowed**
* **List is dynamic** (size can increase or decrease)
* Elements are stored inside **square brackets `[ ]`** separated by commas
* We can access elements using **index**
* Python supports both:

  * **Positive Index**
  * **Negative Index**
* List objects are **mutable**, meaning we can modify content.

---

## Features of List

### 1. Insertion Order Preserved

Elements are stored in the same order they are inserted.

Example:

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

Order remains same.

---

### 2. Duplicate Elements Allowed

Lists allow repeated values.

Example:

```python
data = [10, 20, 10, 30, 20]

print(data)
```

### Output

```text
[10, 20, 10, 30, 20]
```

Duplicates are allowed.

---

### 3. Heterogeneous Objects Allowed

List can store different datatypes.

Example:

```python
items = [10, "Python", 45.6, True]

print(items)
```

### Output

```text
[10, 'Python', 45.6, True]
```

Different datatypes are allowed.

---

### 4. Dynamic Nature

List size can change.

We can:

* Add elements
* Remove elements

Example:

```python
marks = [45, 60]

marks.append(75)

print(marks)
```

### Output

```text
[45, 60, 75]
```

---

### 5. Supports Indexing

Each element has an index position.

Example:

```text
          -6   -5   -4   -3   -2   -1
          --------------------------------
List =    10   A    B    20   30   40
          --------------------------------
           0    1    2    3    4    5
```

### Explanation

#### Positive Index

Moves from:

```text
Left → Right
```

Starts from:

```text
0
```

---

#### Negative Index

Moves from:

```text
Right → Left
```

Starts from:

```text
-1
```

---

### 6. Lists are Mutable

We can change values.

Example:

```python
numbers = [10, 20, 30]

numbers[1] = 100

print(numbers)
```

### Output

```text
[10, 100, 30]
```

---

# Creation of List Objects

There are different ways to create a list.

---

## 1) Creating an Empty List

We can create an empty list as follows:

### Method 1

```python
list1 = []

print(list1)
print(type(list1))
```

### Output

```text
[]
<class 'list'>
```

---

### Method 2

```python
list1 = list()

print(list1)
print(type(list1))
```

### Output

```text
[]
<class 'list'>
```

---

## 2) Creating List with Known Elements

If elements are already known:

```python
marks = [45, 60, 75, 90]

print(marks)
```

### Output

```text
[45, 60, 75, 90]
```

---

## 3) Creating List with Dynamic Input

We can take input dynamically.

```python
numbers = eval(input("Enter List: "))

print(numbers)
print(type(numbers))
```

### Example Input

```text
[5, 10, 15, 20]
```

### Output

```text
[5, 10, 15, 20]
<class 'list'>
```

---

## 4) Using `list()` Function

We can create a list using `range()`.

```python
numbers = list(range(0, 12, 3))

print(numbers)
print(type(numbers))
```

### Output

```text
[0, 3, 6, 9]
<class 'list'>
```

---

### Example with String

```python
name = "Rahul"

result = list(name)

print(result)
```

### Output

```text
['R', 'a', 'h', 'u', 'l']
```

### Explanation

Each character becomes a separate element.

---

## 5) Using `split()` Function

`split()` converts string into list.

```python
sentence = "Python programming becomes simple with practice"

words = sentence.split()

print(words)
print(type(words))
```

### Output

```text
['Python', 'programming', 'becomes', 'simple', 'with', 'practice']

<class 'list'>
```

---

## Nested List

Sometimes we place one list inside another list.

Such lists are called:

```text
Nested Lists
```

Example:

```python
data = [10, 20, [30, 40], 50]

print(data)
```

### Output

```text
[10, 20, [30, 40], 50]
```

---

# Accessing Elements of List

We can access list elements by:

1. **Using Index**
2. **Using Slice Operator**

---

# 1) By Using Index

### Important Points

* Lists use **zero-based indexing**
* First element index is:

```text
0
```

* Supports:

  * Positive Index
  * Negative Index

Example:

```python
numbers = [10, 20, 30, 40]
```

### Index Representation

```text
          -4   -3   -2   -1
          -------------------
List =    10   20   30   40
          -------------------
           0    1    2    3
```

---

### Accessing Elements

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
print(numbers[10])
```

### Output

```text
10
40

IndexError: list index out of range
```

### Explanation

```python
numbers[0]
```

Output:

```text
10
```

---

```python
numbers[-1]
```

Output:

```text
40
```

---

```python
numbers[10]
```

Invalid index.

Error:

```text
IndexError
```

---

# 2) By Using Slice Operator

## Syntax

```python
list2 = list1[start:stop:step]
```

---

### Start

Represents:

```text
Index where slicing starts
```

Default value:

```text
0
```

---

### Stop

Represents:

```text
Index where slicing ends
```

Default value:

```text
Length of list
```

---

### Step

Represents:

```text
Increment value
```

Default value:

```text
1
```

---

## Example Program

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[2:7])

print(numbers[3:8])

print(numbers[::2])

print(numbers[8:2:-2])

print(numbers[4:100])
```

### Output

```text
[3, 4, 5, 6, 7]

[4, 5, 6, 7, 8]

[1, 3, 5, 7, 9]

[9, 7, 5]

[5, 6, 7, 8, 9, 10]
```

---

# Key Takeaways

* List stores multiple values in a single variable.
* Lists preserve insertion order.
* Duplicate values are allowed.
* Different datatype values are allowed.
* Lists are mutable.
* List indexing starts from `0`.
* Negative indexing starts from `-1`.
* List can be created using:

  * `[]`
  * `list()`
  * `range()`
  * `split()`
  * Dynamic input
* Slice operator syntax:

```python
list[start:stop:step]
```

* Invalid index causes:

```text
IndexError: list index out of range
```
# List vs Mutability

## What is Mutability?

Once a **List object is created**, we can **modify (change) its content**.

Hence:

```text id="b1q7md"
Lists are Mutable
```

This means:

* We can change elements
* Add elements
* Remove elements

---

## Example Program

```python id="p9w2mk"
numbers = [10, 20, 30, 40]

print(numbers)

numbers[1] = 777

print(numbers)
```

### Output

```text id="j7v5xt"
[10, 20, 30, 40]

[10, 777, 30, 40]
```

---

## Step-by-Step Explanation

### Original List

```python id="h2z8kp"
numbers = [10, 20, 30, 40]
```

List contains:

```text id="v4x1mz"
10
20
30
40
```

---

### Modify Element

```python id="r8m6qw"
numbers[1] = 777
```

Index:

```text id="d9t2yw"
1
```

contains:

```text id="t1q5xc"
20
```

It gets replaced with:

```text id="m8p2vr"
777
```

Updated list:

```text id="g4w9ks"
[10, 777, 30, 40]
```

---

## Text Diagram

```text id="x5r7qt"
Before Change

Index:    0    1    2    3
         ------------------
List =   10   20   30   40
         ------------------
```

```text id="f3m8zw"
After Change

Index:    0    1    2    3
         -------------------
List =   10  777   30   40
         -------------------
```

---

# Traversing the Elements of List

## Definition

The **sequential access of each element in a list** is called:

```text id="z8n2qm"
Traversal
```

We can traverse a list using:

1. `while` loop
2. `for` loop

---

# 1) Traversing List Using `while` Loop

## Example Program

```python id="n6x1pt"
numbers = [0,1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    print(numbers[i])
    i = i + 1
```

### Output

```text id="q2m9rv"
0
1
2
3
4
5
6
7
8
9
10
```

---

## Step-by-Step Explanation

### List Creation

```python id="c5p8xy"
numbers = [0,1,2,3,4,5,6,7,8,9,10]
```

---

### Variable Initialization

```python id="t7m2wk"
i = 0
```

Traversal starts from:

```text id="g1v9pl"
index 0
```

---

### While Condition

```python id="h4x8zs"
while i < len(numbers)
```

Meaning:

```text id="u6r2qm"
Run loop until
i becomes list length
```

---

### Accessing Elements

```python id="w9m4kx"
numbers[i]
```

Python prints elements one by one.

---

### Increment

```python id="y2p7vc"
i = i + 1
```

Moves to next index.

---

# 2) Traversing List Using `for` Loop

## Example Program

```python id="k5x2rt"
numbers = [0,1,2,3,4,5,6,7,8,9,10]

for value in numbers:
    print(value)
```

### Output

```text id="x4q8mz"
0
1
2
3
4
5
6
7
8
9
10
```

---

## Explanation

`for` loop directly accesses elements.

Instead of index:

```text id="r8v2pl"
value gets each element
one by one
```

First iteration:

```text id="m1x9qt"
value = 0
```

Second iteration:

```text id="k7w5rv"
value = 1
```

And continues till end.

---

## `while` Loop vs `for` Loop

| Feature       | `while` Loop      | `for` Loop       |
| ------------- | ----------------- | ---------------- |
| Uses Index    | Yes               | No               |
| Easy to Write | No                | Yes              |
| Best For      | Index-based logic | Direct Traversal |

---

# 3) Display Only Even Numbers

## Example Program

```python id="v8r2kx"
numbers = [0,1,2,3,4,5,6,7,8,9,10]

for value in numbers:

    if value % 2 == 0:
        print(value)
```

### Output

```text id="c9w1pm"
0
2
4
6
8
10
```

---

## Step-by-Step Explanation

Condition:

```python id="g2x7rv"
value % 2 == 0
```

Means:

```text id="u5p8mq"
Even number
```

Python checks:

```text id="t1m9vx"
0 → Even

1 → Odd

2 → Even

3 → Odd
```

Only even numbers printed.

---

# 4) Display Elements Index Wise

## Example Program

```python id="j6r2qt"
letters = ["X", "Y", "Z"]

x = len(letters)

for i in range(x):

    print(
        letters[i],
        "is available at positive index:",
        i,
        "and at negative index:",
        i - x
    )
```

### Output

```text id="m3x8vp"
X is available at positive index: 0 and at negative index: -3

Y is available at positive index: 1 and at negative index: -2

Z is available at positive index: 2 and at negative index: -1
```

---

## Explanation

Length:

```python id="z9q1rt"
len(letters)
```

returns:

```text id="r5m8vx"
3
```

Loop runs:

```text id="w2x7pk"
0
1
2
```

Negative index formula:

```python id="g8r4tm"
i - x
```

Calculation:

```text id="f4v2qp"
0 - 3 = -3

1 - 3 = -2

2 - 3 = -1
```

---

# Important Functions of List

## 1) `len()`

### Definition

`len()` returns the **number of elements present in the list**.

---

### Example

```python id="h7q2vx"
numbers = [10, 20, 30, 40]

print(len(numbers))
```

### Output

```text id="u1m9zk"
4
```

---

## Explanation

List contains:

```text id="t8r5vp"
10
20
30
40
```

Total elements:

```text id="j4x2qm"
4
```

---

## 2) `count()`

### Definition

`count()` returns **how many times an element occurs in a list**.

---

### Example Program

```python id="x6v2pk"
numbers = [1,2,2,2,3,3]

print(numbers.count(1))
print(numbers.count(2))
print(numbers.count(3))
print(numbers.count(4))
```

### Output

```text id="q5m8rt"
1
3
2
0
```

---

## Explanation

Occurrences:

```text id="n7x4qp"
1 → appears 1 time

2 → appears 3 times

3 → appears 2 times

4 → appears 0 times
```

---

## 3) `index()`

### Definition

`index()` returns the **index of first occurrence** of an element.

---

### Example Program

```python id="w9q2pk"
numbers = [1,2,2,2,3,3]

print(numbers.index(1))
print(numbers.index(2))
print(numbers.index(3))
print(numbers.index(4))
```

### Output

```text id="p4x7mq"
0
1
4

ValueError: 4 is not in list
```

---

## Explanation

First occurrence positions:

```text id="y8r2vp"
1 → index 0

2 → index 1

3 → index 4
```

---

### Important Note

If element is not present:

```text id="z1m9qt"
ValueError occurs
```

Before using `index()`, check using:

```python id="g7x2rv"
4 in numbers
```

### Output

```text id="r2v8pk"
False
```

---

# Key Takeaways

* Lists are **mutable**.
* Traversal means accessing elements sequentially.
* Traversal methods:

  * `while` loop
  * `for` loop
* `len()` → returns total elements.
* `count()` → returns occurrences of an item.
* `index()` → returns first occurrence position.
* Invalid element in `index()` causes:

```text id="w4q9mk"
ValueError
```
