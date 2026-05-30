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
