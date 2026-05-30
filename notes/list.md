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
# II. Manipulating Elements of List

List provides several functions to **add, insert, remove, and manipulate elements**.

Common list manipulation functions:

1. `append()`
2. `insert()`
3. `extend()`
4. `remove()`
5. `pop()`

---

# 1) `append()` Function

## Definition

`append()` is used to **add an element at the end of the list**.

### Syntax

```python
list.append(item)
```

---

## Example 1: Adding Elements

```python
fruits = []

fruits.append("Apple")
fruits.append("Mango")
fruits.append("Orange")

print(fruits)
```

### Output

```text
['Apple', 'Mango', 'Orange']
```

---

## Step-by-Step Explanation

Initially:

```python
fruits = []
```

After:

```python
fruits.append("Apple")
```

List becomes:

```text
['Apple']
```

After:

```python
fruits.append("Mango")
```

List becomes:

```text
['Apple', 'Mango']
```

Final list:

```text
['Apple', 'Mango', 'Orange']
```

---

## Example 2: Add Multiples of 10 up to 100

```python
numbers = []

for i in range(11):

    if i % 10 == 0:
        numbers.append(i)

print(numbers)
```

### Output

```text
[0, 10]
```

---

### Improved Example (Multiples of 10 till 100)

```python
numbers = []

for i in range(0, 101, 10):
    numbers.append(i)

print(numbers)
```

### Output

```text
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

---

## Important Point

`append()`:

```text
Always adds item at the end
```

---

# 2) `insert()` Function

## Definition

`insert()` is used to **insert an element at a specific index position**.

### Syntax

```python
list.insert(index, item)
```

---

## Example 1

```python
numbers = [1, 2, 3, 4, 5]

numbers.insert(1, 888)

print(numbers)
```

### Output

```text
[1, 888, 2, 3, 4, 5]
```

---

## Explanation

Before insertion:

```text
[1, 2, 3, 4, 5]
```

Insert:

```python
numbers.insert(1, 888)
```

At index:

```text
1
```

Result:

```text
[1, 888, 2, 3, 4, 5]
```

---

## Example 2

```python
numbers = [1, 2, 3, 4, 5]

numbers.insert(10, 777)
numbers.insert(-10, 999)

print(numbers)
```

### Output

```text
[999, 1, 2, 3, 4, 5, 777]
```

---

## Important Note

### If index is greater than maximum index

Element gets inserted at:

```text
Last position
```

Example:

```python
numbers.insert(100, 50)
```

---

### If index is smaller than minimum index

Element gets inserted at:

```text
First position
```

Example:

```python
numbers.insert(-100, 50)
```

---

# Difference Between `append()` and `insert()`

| `append()`         | `insert()`                     |
| ------------------ | ------------------------------ |
| Adds item at end   | Adds item at specific position |
| Takes one argument | Takes index and item           |
| Simpler            | More flexible                  |

---

## Example Comparison

### `append()`

```python
data = [10, 20]

data.append(30)

print(data)
```

Output:

```text
[10, 20, 30]
```

---

### `insert()`

```python
data = [10, 20]

data.insert(1, 30)

print(data)
```

Output:

```text
[10, 30, 20]
```

---

# 3) `extend()` Function

## Definition

`extend()` is used to **add all elements of one list into another list**.

### Syntax

```python
list1.extend(list2)
```

---

## Example 1

```python
food1 = ["Chicken", "Paneer", "Fish"]

food2 = ["Rice", "Curd", "Juice"]

food1.extend(food2)

print(food1)
```

### Output

```text
['Chicken', 'Paneer', 'Fish', 'Rice', 'Curd', 'Juice']
```

---

## Explanation

Before:

```text
food1 = ['Chicken', 'Paneer', 'Fish']
```

After extending:

```text
All elements of food2
are added to food1
```

Final:

```text
['Chicken', 'Paneer', 'Fish', 'Rice', 'Curd', 'Juice']
```

---

## Example 2: Extending with String

```python
items = ["Pen", "Book"]

items.extend("Bag")

print(items)
```

### Output

```text
['Pen', 'Book', 'B', 'a', 'g']
```

---

## Explanation

String behaves like sequence.

Each character becomes separate element.

---

# 4) `remove()` Function

## Definition

`remove()` is used to **remove a specific element from the list**.

### Syntax

```python
list.remove(item)
```

---

## Important Rule

If element appears multiple times:

```text
Only first occurrence is removed
```

---

## Example 1

```python
numbers = [10, 20, 10, 30]

numbers.remove(10)

print(numbers)
```

### Output

```text
[20, 10, 30]
```

---

## Explanation

Original list:

```text
[10, 20, 10, 30]
```

First `10` removed.

Second `10` remains.

Final:

```text
[20, 10, 30]
```

---

## Example 2: Item Not Present

```python
numbers = [10, 20, 30]

numbers.remove(40)

print(numbers)
```

### Output

```text
ValueError: list.remove(x): x not in list
```

---

## Important Note

Before using `remove()`:

Check item exists or not.

Example:

```python
if 40 in numbers:
    numbers.remove(40)
```

---

# 5) `pop()` Function

## Definition

`pop()`:

1. **Removes element**
2. **Returns removed element**

It is the **only function that manipulates list and returns a value**.

---

## Example 1

```python
numbers = [10, 20, 30, 40]

print(numbers.pop())
print(numbers.pop())

print(numbers)
```

### Output

```text
40
30

[10, 20]
```

---

## Explanation

First:

```python
numbers.pop()
```

Removes:

```text
40
```

Second:

```python
numbers.pop()
```

Removes:

```text
30
```

Remaining:

```text
[10, 20]
```

---

## Example 2: Empty List

```python
numbers = []

print(numbers.pop())
```

### Output

```text
IndexError: pop from empty list
```

---

## Important Notes

### 1. `pop()` Returns Value

Example:

```python
x = numbers.pop()
```

Removed item stored in:

```text
x
```

---

### 2. `pop()` Follows LIFO

LIFO means:

```text
Last In First Out
```

Last inserted element removes first.

---

### 3. Remove by Index

We can remove element at specific position.

### Syntax

```python
list.pop(index)
```

---

## Example

```python
numbers = [10,20,30,40,50,60]

print(numbers.pop())
print(numbers.pop(1))

print(numbers)
```

### Output

```text
60
20

[10, 30, 40, 50]
```

---

## Explanation

### First Pop

```python
numbers.pop()
```

Removes:

```text
Last element → 60
```

---

### Second Pop

```python
numbers.pop(1)
```

Removes:

```text
Element at index 1 → 20
```

---

### Invalid Index

```python
numbers.pop(100)
```

### Output

```text
IndexError: pop index out of range
```

---

# Text Diagram

```text
Original List

[10, 20, 30, 40]

pop()

Removes
   ↓
  40

Remaining

[10, 20, 30]
```

---

# Key Takeaways

* `append()` → Adds element at end
* `insert()` → Adds element at specific index
* `extend()` → Adds all elements from another list
* `remove()` → Removes specific item
* `pop()` → Removes and returns item
* `remove()` deletes first occurrence only
* `pop()` follows:

```text
LIFO (Last In First Out)
```

* Invalid removal may cause:

  * `ValueError`
  * `IndexError`
 
# Difference Between `remove()` and `pop()`

| `remove()`                           | `pop()`                             |
| ------------------------------------ | ----------------------------------- |
| Removes a specific element           | Removes last element by default     |
| Does not return value                | Returns removed value               |
| Requires element name                | Can use index                       |
| Gives `ValueError` if item not found | Gives `IndexError` if list is empty |

---

## Example: `remove()`

```python id="z3m8xq"
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

### Output

```text id="m7q2vp"
[10, 30]
```

---

## Example: `pop()`

```python id="p5w8rk"
numbers = [10, 20, 30]

print(numbers.pop())
```

### Output

```text id="r2x9mt"
30
```

---

## Important Note

Lists are:

```text id="g8m4pz"
Dynamic in Nature
```

Meaning:

We can:

* Increase size
* Decrease size

### For Increasing Size

Use:

```text id="u1q7vk"
append()
insert()
extend()
```

---

### For Decreasing Size

Use:

```text id="y6m2rt"
remove()
pop()
```

---

# III) Ordering Elements of List

We can arrange list elements in a specific order.

Functions used:

1. `reverse()`
2. `sort()`

---

# 1) `reverse()` Function

## Definition

`reverse()` is used to **reverse the order of list elements**.

### Syntax

```python id="h4m9wx"
list.reverse()
```

---

## Example

```python id="n2x7vp"
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

### Output

```text id="t8q1mz"
[40, 30, 20, 10]
```

---

## Step-by-Step Explanation

Original List:

```text id="y3m8vr"
[10, 20, 30, 40]
```

After reverse:

```text id="j6x2pk"
[40, 30, 20, 10]
```

Order completely changes.

---

## Text Diagram

```text id="f1m9qt"
Before Reverse

[10, 20, 30, 40]
```

```text id="v5x8rp"
After Reverse

[40, 30, 20, 10]
```

---

# 2) `sort()` Function

## Definition

`sort()` is used to **arrange elements according to default natural sorting order**.

### Syntax

```python id="g7m2vp"
list.sort()
```

---

## Default Sorting Order

### For Numbers

Sorting order is:

```text id="x9q4mk"
Ascending Order
```

Example:

```text id="m4x8rt"
5 → 10 → 15 → 20
```

---

### For Strings

Sorting order is:

```text id="r1m7vp"
Alphabetical Order
```

Example:

```text id="n5q2xz"
Apple → Banana → Cat → Dog
```

---

## Example 1: Sorting Numbers

```python id="y2x8rp"
numbers = [20, 5, 15, 10]

numbers.sort()

print(numbers)
```

### Output

```text id="w6m4qt"
[5, 10, 15, 20]
```

---

## Explanation

Before:

```text id="u9x1pk"
[20, 5, 15, 10]
```

After sorting:

```text id="f3m8vp"
[5, 10, 15, 20]
```

Ascending order.

---

## Example 2: Sorting Strings

```python id="k8q2mr"
fruits = ["Dog", "Banana", "Apple", "Cat"]

fruits.sort()

print(fruits)
```

### Output

```text id="x5m9rt"
['Apple', 'Banana', 'Cat', 'Dog']
```

---

## Important Note

To use `sort()`:

List must contain:

```text id="j7x4vp"
Homogeneous Elements
```

Meaning:

All elements should be same datatype.

---

## Wrong Example

```python id="g2m9xp"
data = [20, 10, "A", "B"]

data.sort()

print(data)
```

### Output

```text id="v8q3rt"
TypeError:
'<' not supported between instances of 'str' and 'int'
```

---

## Explanation

Problem:

```text id="m1x7pk"
Integers and strings
cannot be compared
```

---

## Note About Python 2 vs Python 3

In **Python 3**:

Mixed datatype sorting is:

```text id="r5m8qt"
Invalid
```

Example:

```python id="t9x2vp"
data = [20, "B", 10, "A"]

data.sort()
```

Produces:

```text id="c4m7rx"
TypeError
```

---

# Sorting in Reverse Order

We can sort in reverse order using:

```python id="x2m8qt"
reverse=True
```

---

## Example

```python id="u7x4pk"
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

numbers.sort(reverse=False)

print(numbers)
```

### Output

```text id="m5q9vr"
[10, 20, 30, 40]

[40, 30, 20, 10]

[10, 20, 30, 40]
```

---

## Explanation

### Default

```python id="k3m8xp"
sort()
```

Gives:

```text id="p7x2rt"
Ascending Order
```

---

### Reverse Sorting

```python id="f1q9mk"
sort(reverse=True)
```

Gives:

```text id="n6x4vp"
Descending Order
```

---

# Aliasing and Cloning of List Objects

---

# 1) Aliasing

## Definition

Assigning the same list reference to another variable is called:

```text id="y9m2qt"
Aliasing
```

---

## Example

```python id="r8x5vp"
x = [10, 20, 30, 40]

y = x

print(id(x))
print(id(y))
```

### Explanation

Both variables point to:

```text id="t4m7qx"
Same Memory Location
```

---

## Problem in Aliasing

If one list changes:

```text id="g2x9pk"
Other list also changes
```

because both refer to same object.

---

## Example

```python id="j5m8vr"
x = [10, 20, 30, 40]

y = x

y[1] = 777

print(x)
```

### Output

```text id="u1x4qt"
[10, 777, 30, 40]
```

---

## Explanation

Even though change happened in `y`:

```text id="n8m2vp"
x also changed
```

because:

```text id="w3q7rx"
Both point to same object
```

---

## Text Diagram

```text id="z6x8pk"
x ───────┐
         │
         ▼
     [10,20,30,40]
         ▲
         │
y ───────┘
```

---

# 2) Cloning

## Definition

Creating an exact duplicate copy of list is called:

```text id="m7q2vp"
Cloning
```

Cloning avoids aliasing problem.

We can do cloning using:

1. Slice Operator `[:]`
2. `copy()` function

---

# A) Cloning Using Slice Operator

## Example

```python id="q8x5rt"
x = [10, 20, 30, 40]

y = x[:]

y[1] = 777

print(x)
print(y)
```

### Output

```text id="w2m9xp"
[10, 20, 30, 40]

[10, 777, 30, 40]
```

---

## Explanation

Since cloning creates:

```text id="p6x4vk"
Separate object
```

Changes in `y`:

```text id="u8m1qt"
Do not affect x
```

---

# B) Cloning Using `copy()` Function

## Example

```python id="n5x8rp"
x = [10, 20, 30, 40]

y = x.copy()

y[1] = 777

print(x)
print(y)
```

### Output

```text id="k2m7vp"
[10, 20, 30, 40]

[10, 777, 30, 40]
```

---

## Explanation

`copy()` creates:

```text id="h9q3rt"
Independent list object
```

---

# Difference Between `=` Operator and `copy()`

| `=` Operator            | `copy()` Function       |
| ----------------------- | ----------------------- |
| Used for aliasing       | Used for cloning        |
| Same memory shared      | Separate memory created |
| Changes reflect in both | Changes independent     |

---

## Example Comparison

### Using `=`

```python id="z4m8qt"
a = [10,20]

b = a
```

Both point to same list.

---

### Using `copy()`

```python id="y7x2pk"
a = [10,20]

b = a.copy()
```

Separate lists created.

---

# Key Takeaways

* `reverse()` reverses list order.
* `sort()` sorts list elements.
* Default sorting:

  * Numbers → Ascending
  * Strings → Alphabetical
* `reverse=True` gives descending order.
* `sort()` requires homogeneous datatype.
* **Aliasing** means sharing same object.
* **Cloning** means creating duplicate independent copy.
* Cloning methods:

  * `[:]`
  * `copy()`
* `=` → aliasing
* `copy()` → cloning

# Using Mathematical Operators for List Objects

We can use:

```text id="q8m2vx"
+
*
```

operators for list objects.

---

# 1) Concatenation Operator (`+`)

## Definition

The `+` operator is used to **combine two lists into a single list**.

This process is called:

```text id="x4p7qt"
Concatenation
```

---

## Example 1

```python id="r2m9wx"
list1 = [10, 20, 30]

list2 = [40, 50, 60]

result = list1 + list2

print(result)
```

### Output

```text id="m7x2vp"
[10, 20, 30, 40, 50, 60]
```

---

## Step-by-Step Explanation

First List:

```text id="v5m8qt"
[10, 20, 30]
```

Second List:

```text id="k1x4rp"
[40, 50, 60]
```

Using:

```python id="g8m2vx"
list1 + list2
```

Combines both:

```text id="n6q9pk"
[10, 20, 30, 40, 50, 60]
```

---

## Important Note

For `+` operator:

```text id="t4m7wx"
Both operands must be lists
```

Otherwise:

```text id="p9x2vr"
TypeError occurs
```

---

## Wrong Example

```python id="w3m8qt"
data = [10, 20]

result = data + 40
```

### Output

```text id="r7x1vp"
TypeError:
can only concatenate list
(not "int") to list
```

---

## Correct Example

```python id="u5m9qx"
data = [10, 20]

result = data + [40]

print(result)
```

### Output

```text id="f8x2pk"
[10, 20, 40]
```

---

# 2) Repetition Operator (`*`)

## Definition

The `*` operator is used to **repeat list elements multiple times**.

### Syntax

```python id="m2q7vx"
list * number
```

---

## Example

```python id="k8m4qt"
numbers = [10, 20, 30]

result = numbers * 3

print(result)
```

### Output

```text id="x1p9vr"
[10, 20, 30, 10, 20, 30, 10, 20, 30]
```

---

## Explanation

Original list:

```text id="n4m8pk"
[10, 20, 30]
```

Repeated:

```text id="v7x2qt"
3 times
```

Final output:

```text id="u9m5rp"
[10,20,30,10,20,30,10,20,30]
```

---

# Comparing List Objects

We can compare lists using:

```text id="q6m2wx"
Comparison Operators
```

Example operators:

```text id="w2x8pk"
==
!=
<
>
<=
>=
```

---

## Example 1: Equality Comparison

```python id="r5m9qt"
x = ["Dog", "Cat", "Rat"]

y = ["Dog", "Cat", "Rat"]

z = ["DOG", "CAT", "RAT"]

print(x == y)

print(x == z)

print(x != z)
```

### Output

```text id="m1x7vp"
True

False

True
```

---

## Explanation

### `x == y`

Both lists have:

* Same elements
* Same order
* Same case

Result:

```text id="t8m2pk"
True
```

---

### `x == z`

Problem:

```text id="g3x9qt"
Case is different
```

Python is:

```text id="u6m4rp"
Case Sensitive
```

So:

```text id="w9x1pk"
False
```

---

## Important Note for `==` and `!=`

Python checks:

1. Number of elements
2. Order of elements
3. Content of elements (case sensitive)

---

# Relational Operators on Lists

When using:

```text id="h7m2vx"
<
>
<=
>=
```

Python compares:

```text id="y4x8qt"
Only first unmatched element
```

---

## Example 1

```python id="k2m9rp"
x = [50, 20, 30]

y = [40, 50, 60, 100]

print(x > y)

print(x >= y)

print(x < y)

print(x <= y)
```

### Output

```text id="p8x4qt"
True

True

False

False
```

---

## Explanation

Python compares:

First elements:

```text id="r1m7pk"
50 and 40
```

Since:

```text id="z5x2vp"
50 > 40
```

Python stops comparison.

---

## Example 2

```python id="n9m4qt"
x = ["Dog", "Cat", "Rat"]

y = ["Rat", "Cat", "Dog"]

print(x > y)

print(x >= y)

print(x < y)

print(x <= y)
```

### Output

```text id="j6x8rp"
False

False

True

True
```

---

## Explanation

First comparison:

```text id="m2q7pk"
"Dog" < "Rat"
```

So:

```text id="f4x9qt"
x < y → True
```

---

# Membership Operators

## Definition

Membership operators check whether an element exists in a list or not.

Operators:

1. `in`
2. `not in`

---

## Example

```python id="v7m2qx"
numbers = [10, 20, 30, 40]

print(10 in numbers)

print(10 not in numbers)

print(50 in numbers)

print(50 not in numbers)
```

### Output

```text id="r8x4vp"
True

False

False

True
```

---

## Explanation

### `10 in numbers`

Checks:

```text id="q1m9pk"
Does 10 exist?
```

Yes.

Output:

```text id="t6x2qt"
True
```

---

### `50 in numbers`

Checks:

```text id="n3m7rp"
Does 50 exist?
```

No.

Output:

```text id="p9x5vk"
False
```

---

# `clear()` Function

## Definition

`clear()` removes **all elements from the list**.

### Syntax

```python id="g2m8qt"
list.clear()
```

---

## Example

```python id="w5x9rp"
numbers = [10, 20, 30, 40]

print(numbers)

numbers.clear()

print(numbers)
```

### Output

```text id="k8m1vx"
[10, 20, 30, 40]

[]
```

---

## Explanation

Before:

```text id="u4x7qt"
[10, 20, 30, 40]
```

After:

```python id="r9m2pk"
numbers.clear()
```

All elements removed.

Result:

```text id="x6m8rp"
[]
```

---

# Nested Lists

## Definition

When one list is present inside another list, it is called:

```text id="f1x9qt"
Nested List
```

---

## Example

```python id="j7m4vx"
data = [10, 20, [30, 40]]

print(data)

print(data[0])

print(data[2])

print(data[2][0])

print(data[2][1])
```

### Output

```text id="m5x2pk"
[10, 20, [30, 40]]

10

[30, 40]

30

40
```

---

## Step-by-Step Explanation

### Access First Element

```python id="t9m7rp"
data[0]
```

Output:

```text id="q3x8qt"
10
```

---

### Access Nested List

```python id="r6m1vx"
data[2]
```

Output:

```text id="p4x9pk"
[30, 40]
```

---

### Access Nested Elements

```python id="k2m8rp"
data[2][0]
```

Output:

```text id="g8x4qt"
30
```

---

```python id="w1m9vx"
data[2][1]
```

Output:

```text id="u7x2pk"
40
```

---

## Important Note

Nested list elements are accessed using:

```text id="t5m8rp"
Multiple Indexes
```

Just like matrix or multidimensional arrays.

---

# Nested List as Matrix

Python can represent:

```text id="x9m4qt"
Matrix
```

using nested lists.

---

## Example

```python id="v2x8rp"
matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(matrix)

print("Elements Row Wise:")

for row in matrix:
    print(row)

print("Elements in Matrix Style:")

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        print(matrix[i][j], end=" ")

    print()
```

### Output

```text id="m7x1pk"
[[10,20,30],
 [40,50,60],
 [70,80,90]]

Elements Row Wise:

[10,20,30]

[40,50,60]

[70,80,90]

Elements in Matrix Style:

10 20 30

40 50 60

70 80 90
```

---

# Key Takeaways

* `+` → Concatenates lists
* `*` → Repeats list elements
* List comparison uses:

  * Elements
  * Order
  * Case sensitivity
* Membership operators:

  * `in`
  * `not in`
* `clear()` removes all elements.
* Nested list = list inside another list.
* Nested lists can represent matrices.
* Nested elements accessed using:

```python id="h8x4qt"
list[index1][index2]
```

