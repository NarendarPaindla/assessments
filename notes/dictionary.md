# Dictionary in Python

## What is a Dictionary?

We can use:

* List
* Tuple
* Set

to represent a group of objects as a single entity.

But if we want to represent data in:

```text id="m8x2qt"
Key : Value format
```

then we use:

```text id="p4m9vk"
Dictionary
```

---

## Real-Life Examples of Dictionary

| Key          | Value        |
| ------------ | ------------ |
| Roll Number  | Student Name |
| Phone Number | Address      |
| IP Address   | Domain Name  |

Example:

```text id="t7x1rp"
101 → Rahul

9876543210 → Hyderabad

192.168.1.1 → google.com
```

---

# Features of Dictionary

### 1. Key-Value Pair Structure

Dictionary stores data as:

```text id="g5m8qt"
key : value
```

Example:

```python id="u2x9pk"
student = {
    101: "Rahul",
    102: "Amit"
}
```

---

### 2. Duplicate Keys Not Allowed

Keys must be:

```text id="k8m1rp"
Unique
```

Example:

```python id="r4x7qt"
data = {
    101: "Rahul",
    101: "Amit"
}

print(data)
```

### Output

```text id="n9m2vk"
{101: 'Amit'}
```

Old value gets replaced.

---

### 3. Duplicate Values Allowed

Example:

```python id="w6x4pk"
data = {
    101: "Rahul",
    102: "Rahul"
}

print(data)
```

### Output

```text id="j3m8qt"
{101: 'Rahul', 102: 'Rahul'}
```

---

### 4. Heterogeneous Objects Allowed

Different datatypes allowed for:

* Keys
* Values

Example:

```python id="q7x2rp"
data = {
    101: "Python",
    "course": 5000,
    1.5: True
}
```

---

### 5. Insertion Order Not Preserved

Dictionary order is not guaranteed in traditional explanation.

---

### 6. Mutable Nature

Dictionary is:

```text id="f1m9vk"
Mutable
```

Meaning:

We can:

* Add items
* Delete items
* Update items

---

### 7. Dynamic Nature

Dictionary size can:

```text id="x5m2qt"
Increase or decrease
```

---

### 8. Indexing and Slicing Not Supported

We access dictionary data using:

```text id="u8x4rp"
Keys
```

not index.

---

# How to Create Dictionary?

We can create dictionary using:

```python id="g2m7qt"
{}
```

OR

```python id="v9x1pk"
dict()
```

---

## 1) Creating Empty Dictionary

### Method 1

```python id="t4m8vk"
d = {}

print(d)

print(type(d))
```

### Output

```text id="n7x2rp"
{}

<class 'dict'>
```

---

### Method 2

```python id="k1m9qt"
d = dict()

print(d)
```

### Output

```text id="q5x8pk"
{}
```

---

## 2) Adding Entries Dynamically

We can add values using:

```python id="w8m2rp"
dictionary[key] = value
```

---

### Example

```python id="p3x7qt"
d = {}

d[101] = "Rahul"
d[102] = "Amit"
d[103] = "Vijay"

print(d)
```

### Output

```text id="m6x1vk"
{
101: 'Rahul',
102: 'Amit',
103: 'Vijay'
}
```

---

## 3) Creating Dictionary with Known Data

If data is already available:

```python id="h9m4qt"
students = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(students)
```

---

## Syntax

```python id="u4x8rp"
{
 key : value,
 key : value
}
```

---

# How to Access Data from Dictionary?

Dictionary data is accessed using:

```text id="r8m1qt"
Keys
```

---

## Example

```python id="g5x9pk"
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d[101])

print(d[103])
```

### Output

```text id="t2m7rp"
Rahul

Vijay
```

---

## Explanation

```python id="v7x4qt"
d[101]
```

returns:

```text id="x1m8vk"
Rahul
```

---

```python id="n5x2qt"
d[103]
```

returns:

```text id="f8m9rp"
Vijay
```

---

# Key Not Available

If key does not exist:

```text id="m4x7pk"
KeyError occurs
```

Example:

```python id="q9m1qt"
print(d[400])
```

### Output

```text id="w3x8rp"
KeyError: 400
```

---

## Safe Way to Check Key

### Using `in` Operator

```python id="j7m2vk"
if 400 in d:
    print(d[400])
```

This avoids error.

---

# Program: Store Student Name and Percentage Marks

## Problem Statement

Write a program to:

```text id="p8x4qt"
Store student names
and marks in dictionary
```

and display the information.

---

## Program

```python id="u2m9rp"
records = {}

n = int(
    input("Enter number of students: ")
)

i = 1

while i <= n:

    name = input(
        "Enter Student Name: "
    )

    marks = input(
        "Enter Percentage Marks: "
    )

    records[name] = marks

    i = i + 1

print(
    "Name of Student",
    "\t",
    "% of Marks"
)

for student in records:

    print(
        student,
        "\t\t",
        records[student]
    )
```

---

## Example Input

```text id="k6x1pk"
3
```

Student Details:

```text id="g9m4qt"
Rahul → 65%

Amit → 72%

Vijay → 80%
```

### Output

```text id="r3m8rp"
Name of Student     % of Marks

Rahul               65%

Amit                72%

Vijay               80%
```

---

# How to Update Dictionary?

### Syntax

```python id="x7m2qt"
dictionary[key] = value
```

---

## Case 1: Key Not Present

New entry gets added.

### Example

```python id="m2x8vk"
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d)

d[104] = "Arjun"

print(d)
```

### Output

```text id="v8m1qt"
{
101:'Rahul',
102:'Amit',
103:'Vijay'
}

{
101:'Rahul',
102:'Amit',
103:'Vijay',
104:'Arjun'
}
```

---

## Case 2: Key Already Present

Old value gets replaced.

### Example

```python id="t4x7rp"
d[101] = "Sunny"

print(d)
```

### Output

```text id="p9m2vk"
{
101:'Sunny',
102:'Amit',
103:'Vijay',
104:'Arjun'
}
```

---

# How to Delete Elements from Dictionary?

---

# 1) `del d[key]`

## Definition

Deletes:

```text id="f6x8qt"
Entry associated
with specified key
```

---

## Example

```python id="n1m7rp"
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d)

del d[101]

print(d)
```

### Output

```text id="u5x2pk"
{
101:'Rahul',
102:'Amit',
103:'Vijay'
}

{
102:'Amit',
103:'Vijay'
}
```

---

## Key Not Present

Example:

```python id="z8m4qt"
del d[400]
```

### Output

```text id="k2x9rp"
KeyError: 400
```

---

# 2) `d.clear()`

## Definition

Removes:

```text id="g7m1qt"
All entries
```

from dictionary.

---

## Example

```python id="r4x8vk"
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d)

d.clear()

print(d)
```

### Output

```text id="x9m2rp"
{
101:'Rahul',
102:'Amit',
103:'Vijay'
}

{}
```

---

# Key Takeaways

* Dictionary stores:

```text id="m6x7qt"
Key : Value
```

pairs.

* Keys must be unique.
* Duplicate values are allowed.
* Dictionary is mutable.
* Data accessed using:

```python id="p1x8vk"
dictionary[key]
```

* Missing key causes:

```text id="j8m4rp"
KeyError
```

* Add/update:

```python id="t3m9qt"
d[key] = value
```

* Delete single item:

```python id="w7x2pk"
del d[key]
```

* Delete all items:

```python id="g5m1rp"
d.clear()
```
# 3) `del d`

## Definition

`del d` is used to:

```text
Delete the complete dictionary
```

After deleting:

```text
We cannot access dictionary again
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d)

del d

print(d)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit',
103: 'Vijay'
}

NameError:
name 'd' is not defined
```

---

## Explanation

Before deletion:

```text
Dictionary exists
```

After:

```python
del d
```

Dictionary is:

```text
Completely removed from memory
```

So accessing:

```python
print(d)
```

causes:

```text
NameError
```

---

# Important Functions of Dictionary

Common dictionary functions:

1. `dict()`
2. `len()`
3. `clear()`
4. `get()`
5. `pop()`
6. `popitem()`
7. `keys()`
8. `values()`
9. `items()`

---

# 1) `dict()` Function

## Definition

Used to:

```text
Create Dictionary
```

---

## A) Create Empty Dictionary

```python
d = dict()

print(d)
```

### Output

```text
{}
```

---

## B) Create Dictionary with Data

```python
d = dict({
    101: "Rahul",
    102: "Amit"
})

print(d)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit'
}
```

---

## C) Using List of Tuples

```python
d = dict([
    (101, "Rahul"),
    (102, "Amit"),
    (103, "Vijay")
])

print(d)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit',
103: 'Vijay'
}
```

---

# 2) `len()` Function

## Definition

Returns:

```text
Total number of items
```

present in dictionary.

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(len(d))
```

### Output

```text
3
```

---

# 3) `clear()` Function

## Definition

Removes:

```text
All elements
```

from dictionary.

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit"
}

print(d)

d.clear()

print(d)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit'
}

{}
```

---

# 4) `get()` Function

## Definition

`get()` returns:

```text
Value associated with key
```

without causing error.

### Syntax

```python
dictionary.get(key)
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d.get(101))

print(d.get(400))
```

### Output

```text
Rahul

None
```

---

## Explanation

### Existing Key

```python
d.get(101)
```

Returns:

```text
Rahul
```

---

### Missing Key

```python
d.get(400)
```

Returns:

```text
None
```

No error occurs.

---

## `get(key, default_value)`

If key exists:

```text
Returns actual value
```

Otherwise:

```text
Returns default value
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit"
}

print(d.get(101, "Guest"))

print(d.get(500, "Guest"))
```

### Output

```text
Rahul

Guest
```

---

# Difference Between `[]` and `get()`

| `[]` Operator          | `get()` Function |
| ---------------------- | ---------------- |
| Gives `KeyError`       | No error         |
| Used for direct access | Safer access     |
| Fails if key absent    | Returns `None`   |

---

## Example Comparison

### Using `[]`

```python
print(d[500])
```

### Output

```text
KeyError
```

---

### Using `get()`

```python
print(d.get(500))
```

### Output

```text
None
```

---

# 5) `pop()` Function

## Definition

`pop()`:

```text
Removes key-value pair
and returns value
```

### Syntax

```python
dictionary.pop(key)
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d.pop(101))

print(d)
```

### Output

```text
Rahul

{
102: 'Amit',
103: 'Vijay'
}
```

---

## Explanation

Removed:

```text
101 → Rahul
```

Returned:

```text
Rahul
```

---

## Key Not Present

```python
d.pop(500)
```

### Output

```text
KeyError
```

---

# 6) `popitem()` Function

## Definition

Removes:

```text
Last inserted
key-value pair
```

and returns it.

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d)

print(d.popitem())

print(d)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit',
103: 'Vijay'
}

(103, 'Vijay')

{
101: 'Rahul',
102: 'Amit'
}
```

---

## Important Note

If dictionary is empty:

```text
KeyError occurs
```

Example:

```python
d = {}

print(d.popitem())
```

### Output

```text
KeyError:
'popitem(): dictionary is empty'
```

---

# 7) `keys()` Function

## Definition

Returns:

```text
All keys
```

present in dictionary.

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d.keys())

for key in d.keys():
    print(key)
```

### Output

```text
dict_keys([101,102,103])

101
102
103
```

---

# 8) `values()` Function

## Definition

Returns:

```text
All values
```

present in dictionary.

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d.values())

for value in d.values():
    print(value)
```

### Output

```text
dict_values(
['Rahul', 'Amit', 'Vijay']
)

Rahul
Amit
Vijay
```

---

# 9) `items()` Function

## Definition

Returns:

```text
Key-Value pairs
```

in tuple format.

### Format

```text
(key, value)
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

for key, value in d.items():
    print(key, "-->", value)
```

### Output

```text
101 --> Rahul

102 --> Amit

103 --> Vijay
```

---

# Key Takeaways

* `del d` → deletes entire dictionary
* `dict()` → creates dictionary
* `len()` → total items
* `clear()` → remove all entries
* `get()` → safe access without error
* `pop()` → removes specified key
* `popitem()` → removes last inserted pair
* `keys()` → returns keys
* `values()` → returns values
* `items()` → returns key-value pairs as tuples

# 10) `copy()` Function

## Definition

`copy()` is used to create:

```text
Exact duplicate dictionary
```

This is called:

```text
Cloned Copy
```

### Syntax

```python
new_dictionary = old_dictionary.copy()
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

d1 = d.copy()

print(d1)
```

### Output

```text
{
101: 'Rahul',
102: 'Amit',
103: 'Vijay'
}
```

---

## Explanation

Original dictionary:

```text
{
101:'Rahul',
102:'Amit',
103:'Vijay'
}
```

Copied into:

```text
d1
```

Both dictionaries contain same data.

---

## Important Note

`copy()` creates:

```text
Separate Dictionary Object
```

Changes in copied dictionary:

```text
Do not affect original dictionary
```

---

# 11) `setdefault()` Function

## Definition

`setdefault()` checks whether key exists or not.

### Case 1: Key Already Exists

Returns:

```text
Corresponding value
```

### Case 2: Key Not Present

Adds:

```text
New key-value pair
```

to dictionary.

### Syntax

```python
dictionary.setdefault(key, value)
```

---

## Example

```python
d = {
    101: "Rahul",
    102: "Amit",
    103: "Vijay"
}

print(d.setdefault(400, "Arjun"))

print(d)

print(d.setdefault(100, "Sachin"))

print(d)
```

### Output

```text
Arjun

{
101:'Rahul',
102:'Amit',
103:'Vijay',
400:'Arjun'
}

Sachin

{
101:'Rahul',
102:'Amit',
103:'Vijay',
400:'Arjun',
100:'Sachin'
}
```

---

## Explanation

### First Operation

```python
d.setdefault(400, "Arjun")
```

Key:

```text
400
```

not present.

So Python:

```text
Adds new entry
```

---

### Second Operation

```python
d.setdefault(100, "Sachin")
```

Since key not available:

```text
Added to dictionary
```

---

## Example with Existing Key

```python
d = {
    101: "Rahul"
}

print(
    d.setdefault(
        101,
        "Sunny"
    )
)
```

### Output

```text
Rahul
```

Existing value remains unchanged.

---

# 12) `update()` Function

## Definition

`update()` is used to:

```text
Add all items
from one dictionary
to another dictionary
```

### Syntax

```python
dictionary.update(other_dictionary)
```

---

## Example

```python
d1 = {
    101: "Rahul",
    102: "Amit"
}

d2 = {
    103: "Vijay",
    104: "Arjun"
}

d1.update(d2)

print(d1)
```

### Output

```text
{
101:'Rahul',
102:'Amit',
103:'Vijay',
104:'Arjun'
}
```

---

## Important Rule

If key already exists:

```text
Old value replaced
with new value
```

---

## Example

```python
d1 = {
    101: "Rahul"
}

d2 = {
    101: "Sunny"
}

d1.update(d2)

print(d1)
```

### Output

```text
{
101:'Sunny'
}
```

---

# Program: Sum of Dictionary Values

## Problem Statement

Write a program to:

```text
Take dictionary input
and print sum of values
```

---

## Program

```python
d = eval(
    input("Enter dictionary: ")
)

total = sum(d.values())

print("Sum =", total)
```

---

## Example Input

```text
{
'A':100,
'B':200,
'C':300
}
```

### Output

```text
Sum = 600
```

---

## Explanation

### `d.values()`

Returns:

```text
100
200
300
```

Then:

```python
sum()
```

calculates:

```text
100 + 200 + 300 = 600
```

---

# Program: Count Occurrences of Each Letter in String

## Problem Statement

Write a program to:

```text
Find number of occurrences
of each character
in a string
```

---

## Program

```python
word = input(
    "Enter any word: "
)

d = {}

for ch in word:

    d[ch] = d.get(ch, 0) + 1

for k, v in d.items():

    print(
        k,
        "occurred",
        v,
        "times"
    )
```

---

## Example Input

```text
mississippi
```

### Output

```text
m occurred 1 times

i occurred 4 times

s occurred 4 times

p occurred 2 times
```

---

## Step-by-Step Explanation

### First Character

```text
m
```

Added:

```text
m : 1
```

---

### When Character Repeats

Example:

```text
i
```

Count increases:

```text
1 → 2 → 3 → 4
```

---

## Important Logic

```python
d[ch] = d.get(ch, 0) + 1
```

Meaning:

If character exists:

```text
Increase count
```

Otherwise:

```text
Start from 0
```

---

# Program: Count Occurrences of Each Vowel

## Problem Statement

Write a program to:

```text
Count number of vowels
present in string
```

---

## Program

```python
word = input(
    "Enter any word: "
)

vowels = {
    'a',
    'e',
    'i',
    'o',
    'u'
}

d = {}

for ch in word:

    if ch in vowels:

        d[ch] = d.get(ch, 0) + 1

for k, v in sorted(d.items()):

    print(
        k,
        "occurred",
        v,
        "times"
    )
```

---

## Example Input

```text
programminglanguage
```

### Output

```text
a occurred 3 times

i occurred 1 times

o occurred 1 times

u occurred 1 times
```

---

## Explanation

Only vowels counted:

```text
a
e
i
o
u
```

Consonants ignored.

---

# Program: Student Marks Management System

## Problem Statement

Write a program to:

```text
Accept student names
and marks
```

Store in dictionary and:

```text
Search student marks
```

---

## Program

```python
n = int(
    input(
        "Enter the number of students: "
    )
)

d = {}

for i in range(n):

    name = input(
        "Enter Student Name: "
    )

    marks = input(
        "Enter Student Marks: "
    )

    d[name] = marks

while True:

    name = input(
        "Enter Student Name to get Marks: "
    )

    marks = d.get(name, -1)

    if marks == -1:

        print(
            "Student Not Found"
        )

    else:

        print(
            "The Marks of",
            name,
            "are",
            marks
        )

    option = input(
        "Do you want to find another student marks [Yes|No] "
    )

    if option == "No":
        break

print(
    "Thanks for using our application"
)
```

---

## Example Output

```text
Enter Student Name:
Sunny

Enter Student Marks:
90

Enter Student Name to get Marks:
Sunny

The Marks of Sunny are 90
```

---

## If Student Not Found

Output:

```text
Student Not Found
```

---

# Dictionary Comprehension

## Definition

Comprehension concept is applicable to:

```text
Dictionary also
```

---

## Syntax

```python
{
key:value
for item in iterable
}
```

---

## Example 1: Squares

```python
squares = {
    x: x * x
    for x in range(1, 6)
}

print(squares)
```

### Output

```text
{
1:1,
2:4,
3:9,
4:16,
5:25
}
```

---

## Example 2: Double Values

```python
doubles = {
    x: x * 2
    for x in range(1, 6)
}

print(doubles)
```

### Output

```text
{
1:2,
2:4,
3:6,
4:8,
5:10
}
```

---

# Key Takeaways

* `copy()` → creates cloned dictionary
* `setdefault()` → adds key if absent
* `update()` → merges dictionaries
* `sum(d.values())` → sum of dictionary values
* `get(key,0)+1` → useful for counting
* `items()` → returns key-value pairs
* Dictionary comprehension supported:

```python
{
k:v
for item in iterable
}
```

* `update()` replaces duplicate keys.
* `setdefault()` does not overwrite existing values.
