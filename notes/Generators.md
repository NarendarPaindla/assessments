# Generators in Python

# What is a Generator?

A **Generator** is a special type of function that generates a sequence of values one at a time instead of returning all values at once.

Generators use the **yield** keyword.

---

## Definition

A generator is a function that:

* Produces values lazily (on demand)
* Uses the `yield` keyword
* Returns a generator object
* Saves memory by generating values one at a time

---

## Generator Flow

```text
Generator Function
        |
       yield
        |
        v
Sequence of Values
```

---

## Generator vs Normal Function

| Normal Function               | Generator Function        |
| ----------------------------- | ------------------------- |
| Uses `return`                 | Uses `yield`              |
| Returns entire result at once | Returns values one by one |
| More memory consumption       | Less memory consumption   |
| Execution ends after return   | Execution pauses at yield |
| Not suitable for huge data    | Suitable for huge data    |

---

# Creating a Generator

## Example 1

```python
def mygen():

    yield 'A'
    yield 'B'
    yield 'C'


g = mygen()

print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

---

## Output

```text
<class 'generator'>

A
B
C

StopIteration
```

---

## Explanation

### Step 1

```python
g = mygen()
```

Creates a generator object.

---

### Step 2

```python
next(g)
```

Execution starts and reaches:

```python
yield 'A'
```

Returns:

```text
A
```

and pauses.

---

### Step 3

Next call resumes execution.

```python
yield 'B'
```

Returns:

```text
B
```

---

### Step 4

Next call:

```python
yield 'C'
```

Returns:

```text
C
```

---

### Step 5

No values left.

```python
next(g)
```

Raises:

```text
StopIteration
```

---

# Example 2: Countdown Generator

```python
def countdown(num):

    print("Start Countdown")

    while num > 0:

        yield num

        num = num - 1


values = countdown(5)

for x in values:
    print(x)
```

---

## Output

```text
Start Countdown
5
4
3
2
1
```

---

## Explanation

Generator produces:

```text
5
4
3
2
1
```

one value at a time.

---

# Example 3: Generate First N Numbers

```python
def first(num):

    n = 1

    while n <= num:

        yield n

        n = n + 1


values = first(5)

for x in values:
    print(x)
```

---

## Output

```text
1
2
3
4
5
```

---

# Converting Generator into List

Generators can be converted into a list.

```python
values = first(10)

l = list(values)

print(l)
```

---

## Output

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# Example 4: Fibonacci Generator

Fibonacci Sequence:

```text
0,1,1,2,3,5,8,13,21,...
```

Each number is the sum of previous two numbers.

---

## Program

```python
def fib():

    a = 0
    b = 1

    while True:

        yield a

        a, b = b, a + b


for f in fib():

    if f > 100:
        break

    print(f)
```

---

## Output

```text
0
1
1
2
3
5
8
13
21
34
55
89
```

---

## Fibonacci Flow

```text
a=0  b=1

0

a=1  b=1

1

a=1  b=2

1

a=2  b=3

2

a=3  b=5

3
...
```

---

# Advantages of Generator Functions

## 1. Easy to Use

Generators are easier than creating custom iterator classes.

---

## 2. Better Memory Utilization

Values are generated only when needed.

---

## 3. Better Performance

No need to store all values in memory.

---

## 4. Suitable for Large Files

Useful while reading huge files.

---

## 5. Useful for Web Scraping

Large amounts of data can be processed efficiently.

---

## 6. Infinite Sequences

Generators can generate unlimited values.

Example:

```python
while True:
    yield value
```

---

# Generators vs Normal Collections (Performance)

Suppose we want to generate 1 crore records.

---

## Using List

```python
def people_list(num_people):

    result = []

    for i in range(num_people):

        person = {
            "id": i
        }

        result.append(person)

    return result
```

---

### Problem

```text
All records are created and stored in memory first.
```

Memory consumption becomes very high.

---

## Using Generator

```python
def people_generator(num_people):

    for i in range(num_people):

        person = {
            "id": i
        }

        yield person
```

---

### Benefit

```text
One record generated at a time.
```

No huge memory requirement.

---

# Generators vs Collections (Memory Utilization)

## Normal Collection

```python
l = [x*x for x in range(100000000000)]
```

### Problem

Python tries to store all values.

May result in:

```text
MemoryError
```

---

## Generator Expression

```python
g = (x*x for x in range(100000000000))

print(next(g))
```

---

## Output

```text
0
```

---

### Why No Memory Error?

Because values are not stored immediately.

They are generated only when requested.

---

# Generator Expressions

Similar to List Comprehension.

---

## List Comprehension

```python
l = [x*x for x in range(5)]

print(l)
```

Output:

```text
[0, 1, 4, 9, 16]
```

---

## Generator Expression

```python
g = (x*x for x in range(5))

print(g)
```

Output:

```text
<generator object>
```

---

## Accessing Values

```python
for x in g:
    print(x)
```

Output:

```text
0
1
4
9
16
```

---

# Real-Time Example: Reading Large Log File

Without Generator:

```python
data = file.readlines()
```

Entire file loads into memory.

---

Using Generator:

```python
for line in file:
    yield line
```

Only one line is loaded at a time.

---

# Generator Lifecycle

```text
Generator Created
        |
        v
next()
        |
        v
yield Value
        |
Execution Paused
        |
next()
        |
Execution Resumes
        |
yield Value
        |
...
        |
No More Values
        |
StopIteration
```

---

# Generator vs Iterator

| Generator                 | Iterator                       |
| ------------------------- | ------------------------------ |
| Created using function    | Created using class            |
| Uses yield                | Uses **iter**() and **next**() |
| Easy to write             | More code                      |
| Automatic state handling  | Manual state handling          |
| Recommended in most cases | Used for advanced control      |

---

# When Should We Use Generators?

Use Generators when:

* Data is very large
* Reading files
* Processing logs
* Streaming data
* Web scraping
* Infinite sequences
* Memory optimization is required

---

# Key Takeaways

* Generators are functions that use `yield`.
* They return values one at a time.
* Generator functions return a generator object.
* `next()` is used to fetch the next value.
* When all values are exhausted, `StopIteration` occurs.
* Generators consume less memory than lists.
* Generators are ideal for large datasets and file processing.
* Generator expressions use parentheses `()`.
* Generators improve memory utilization and performance.
* Fibonacci sequences, countdowns, and large file processing are common generator use cases.
