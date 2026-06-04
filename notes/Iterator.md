# Iterators in Python

# What is an Iterator?

An **Iterator** is an object that allows us to traverse (visit) elements one by one from a collection such as:

* List
* Tuple
* Set
* Dictionary
* String
* File

Instead of loading all values at once, an iterator gives values **one at a time when requested**.

---

# Real-Life Analogy

Imagine a TV Remote.

```text
TV Channels

1. News
2. Sports
3. Movies
4. Music
5. Kids
```

You don't receive all channels at once.

Every time you press:

```text
Next Channel
```

you get the next channel.

Similarly:

```python
next(iterator)
```

returns the next element.

---

# Why Do We Need Iterators?

Without Iterator:

```python
names = ["Raj", "Amit", "Kiran"]

print(names[0])
print(names[1])
print(names[2])
```

Not practical for large collections.

---

With Iterator:

```python
names = ["Raj", "Amit", "Kiran"]

it = iter(names)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
Raj
Amit
Kiran
```

---

# Iterable vs Iterator

Students often confuse these terms.

| Iterable                      | Iterator                     |
| ----------------------------- | ---------------------------- |
| Collection of data            | Object used to traverse data |
| Can create iterator           | Traverses elements           |
| Uses iter()                   | Uses next()                  |
| Examples: List, Tuple, String | Result of iter()             |

---

## Example

```python
nums = [10, 20, 30]
```

Here:

```text
nums
```

is an Iterable.

---

```python
it = iter(nums)
```

Now:

```text
it
```

is an Iterator.

---

# How Iterator Works?

```text
List
  |
iter()
  |
Iterator
  |
next()
  |
Element
```

---

# Creating Iterator

## Example 1

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(type(it))
```

Output:

```text
<class 'list_iterator'>
```

---

# Using next()

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
10
20
30
```

---

# What Happens After Last Element?

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
10
20
30

StopIteration
```

---

# StopIteration Exception

When iterator has no more elements:

```python
next(iterator)
```

raises:

```python
StopIteration
```

---

Example:

```python
names = ["A", "B"]

it = iter(names)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
A
B

StopIteration
```

---

# Iterator with Tuple

```python
t = (100, 200, 300)

it = iter(t)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
100
200
300
```

---

# Iterator with String

```python
s = "PYTHON"

it = iter(s)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
P
Y
T
```

---

# Iterator with Dictionary

By default dictionary iterates through keys.

```python
d = {
    "id": 101,
    "name": "Ravi",
    "salary": 50000
}

it = iter(d)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
id
name
salary
```

---

# Iterator with Set

```python
s = {10,20,30}

it = iter(s)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
10
20
30
```

Note:

Order may vary because set is unordered.

---

# for Loop Internally Uses Iterator

Students think:

```python
for x in data:
    print(x)
```

is special.

Internally Python does:

```python
it = iter(data)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

---

# Iterator Protocol

For an object to become an iterator it must implement:

### 1. **iter**()

Returns iterator object.

### 2. **next**()

Returns next value.

---

# Custom Iterator Example

```python
class Count:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        value = self.num

        self.num += 1

        return value


c = Count()

it = iter(c)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
1
2
3
```

---

# Finite Iterator

```python
class Numbers:

    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.x > 5:
            raise StopIteration

        value = self.x
        self.x += 1

        return value


n = Numbers()

for i in n:
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

# Iterator Lifecycle

```text
Create Iterable
       |
       v
Create Iterator
       |
       v
next()
       |
       v
Return Element
       |
More Elements?
  /        \
Yes        No
 |          |
next()   StopIteration
```

---

# Iterators vs Lists

| List              | Iterator                  |
| ----------------- | ------------------------- |
| Stores all data   | Produces data one by one  |
| More memory       | Less memory               |
| Supports indexing | No indexing               |
| Reusable          | Usually consumed once     |
| Faster access     | Better for large datasets |

---

# Memory Advantage

List:

```python
nums = [x for x in range(1000000)]
```

Stores all one million values.

---

Iterator:

```python
nums = iter(range(1000000))
```

Creates values only when needed.

Less memory usage.

---

# Iterator vs Generator

| Iterator                       | Generator                |
| ------------------------------ | ------------------------ |
| Need **iter**() and **next**() | Need yield               |
| More code                      | Less code                |
| Manual implementation          | Automatic implementation |
| Complex                        | Simple                   |
| Memory Efficient               | More Memory Efficient    |

---

## Iterator Example

```python
class Counter:

    def __iter__(self):
        return self

    def __next__(self):
        pass
```

Many lines of code.

---

## Generator Equivalent

```python
def counter():

    yield 1
    yield 2
    yield 3
```

Much simpler.

---

# Common Built-in Iterators

```python
list_iterator
tuple_iterator
str_iterator
dict_keyiterator
set_iterator
range_iterator
file_iterator
```

---

# Practical Example: Reading File

```python
f = open("data.txt")

it = iter(f)

print(next(it))
print(next(it))
```

Reads file line by line.

---

# Advantages of Iterators

1. Memory Efficient
2. Suitable for Large Data
3. Lazy Evaluation
4. Used Internally by for Loop
5. Faster Processing of Large Collections
6. Foundation for Generators

---

# Disadvantages of Iterators

1. Cannot Access Random Elements
2. No Indexing
3. Usually One-Time Traversal
4. StopIteration Must Be Handled

---

# Interview Questions

### Q1: What is an Iterator?

An object that allows sequential access to elements using `next()`.

---

### Q2: What is an Iterable?

An object that can produce an iterator using `iter()`.

Examples:

```python
list
tuple
set
dict
string
```

---

### Q3: Which exception is raised when iterator is exhausted?

```python
StopIteration
```

---

### Q4: Which methods must an Iterator implement?

```python
__iter__()
__next__()
```

---

### Q5: Is every Iterator an Iterable?

Yes.

Because iterator contains:

```python
__iter__()
```

---

### Q6: Is every Iterable an Iterator?

No.

List is iterable but not iterator.

```python
l = [1,2,3]

next(l)
```

Output:

```text
TypeError
```

Need:

```python
it = iter(l)
```

---

# Key Takeaways

* Iterator is an object used to traverse data one element at a time.
* `iter()` converts an iterable into an iterator.
* `next()` returns the next element.
* When elements are exhausted, `StopIteration` is raised.
* Iterator protocol requires:

  * `__iter__()`
  * `__next__()`
* `for` loop internally uses iterators.
* Iterators are memory efficient and useful for large datasets.
* Generators are a simpler way to create iterators using `yield`.
