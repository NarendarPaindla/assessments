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
