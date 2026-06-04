# Context Managers in Python

# What is a Context Manager?

A **Context Manager** is an object that properly manages resources such as:

* Files
* Database Connections
* Network Connections
* Locks
* Sockets

It automatically performs:

```text
Resource Allocation
        |
        v
     Use Resource
        |
        v
Resource Cleanup
```

even if exceptions occur.

---

# Why Do We Need Context Managers?

Consider file handling.

## Without Context Manager

```python
f = open("data.txt", "w")

f.write("Hello")

f.close()
```

Problem:

If an exception occurs before:

```python
f.close()
```

the file may remain open.

This can lead to:

* Memory leaks
* Resource wastage
* File locking issues

---

# Solution: Context Manager

```python
with open("data.txt", "w") as f:

    f.write("Hello")
```

File will automatically close after execution.

No need to call:

```python
f.close()
```

---

# Real-Life Analogy

Imagine borrowing a book from a library.

### Without Context Manager

```text
Take Book
Read Book
Forget to Return
```

Problem:

Library loses track of the book.

---

### With Context Manager

```text
Take Book
Read Book
Automatically Return Book
```

Resource management becomes automatic.

---

# The with Statement

The most common use of Context Managers is through the `with` statement.

## Syntax

```python
with resource as variable:

    statements
```

---

# Example 1: File Handling

```python
with open("sample.txt", "w") as f:

    f.write("Python")
```

---

## Execution Flow

```text
Open File
    |
Execute Statements
    |
Automatically Close File
```

---

# Checking File Closure

```python
with open("sample.txt", "w") as f:

    print(f.closed)

print(f.closed)
```

### Output

```text
False
True
```

Explanation:

Inside block:

```text
File is Open
```

Outside block:

```text
File is Closed
```

---

# Context Manager with Exception

```python
try:

    with open("sample.txt", "w") as f:

        print(10/0)

except ZeroDivisionError:

    print("Exception Handled")
```

Output:

```text
Exception Handled
```

Even though exception occurred:

```text
File was automatically closed.
```

---

# How Context Managers Work Internally

A Context Manager uses two special methods.

```python
__enter__()
__exit__()
```

---

# **enter**()

Executed when entering the with block.

```text
Resource Acquisition
```

---

# **exit**()

Executed when leaving the with block.

```text
Resource Cleanup
```

---

# Internal Flow

```text
with statement
      |
      v
 __enter__()
      |
 Execute Block
      |
      v
 __exit__()
```

---

# Creating Our Own Context Manager

## Example

```python
class MyContext:

    def __enter__(self):

        print("Resource Allocated")

        return self

    def __exit__(self,
                 exc_type,
                 exc_value,
                 traceback):

        print("Resource Released")


with MyContext():

    print("Inside Block")
```

---

## Output

```text
Resource Allocated
Inside Block
Resource Released
```

---

# Understanding **enter**()

```python
def __enter__(self):

    print("Resource Allocated")

    return self
```

Runs automatically before entering the block.

---

# Understanding **exit**()

```python
def __exit__(
        self,
        exc_type,
        exc_value,
        traceback):
```

Runs automatically after leaving the block.

Even if exceptions occur.

---

# Example with Exception

```python
class MyContext:

    def __enter__(self):

        print("Start")

        return self

    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback):

        print("End")


with MyContext():

    print(10/0)
```

---

## Output

```text
Start
End
ZeroDivisionError
```

Notice:

```text
__exit__()
```

still executed.

---

# Exception Information in **exit**()

Parameters:

```python
exc_type
exc_value
traceback
```

contain exception details.

---

## Example

```python
class MyContext:

    def __enter__(self):

        return self

    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback):

        print("Exception Type:", exc_type)
        print("Exception Value:", exc_value)


with MyContext():

    print(10/0)
```

---

## Output

```text
Exception Type: <class 'ZeroDivisionError'>
Exception Value: division by zero
```

---

# Suppressing Exceptions

If `__exit__()` returns:

```python
True
```

Python suppresses the exception.

---

## Example

```python
class MyContext:

    def __enter__(self):

        return self

    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback):

        print("Exception Handled")

        return True


with MyContext():

    print(10/0)

print("Program Continues")
```

---

## Output

```text
Exception Handled
Program Continues
```

No error displayed.

---

# Context Manager Using contextlib

Python provides:

```python
contextlib
```

module.

---

# Using @contextmanager

```python
from contextlib import contextmanager

@contextmanager
def my_context():

    print("Start")

    yield

    print("End")


with my_context():

    print("Inside Block")
```

---

## Output

```text
Start
Inside Block
End
```

---

# How yield Works Here

Before yield:

```text
Setup Code
```

After yield:

```text
Cleanup Code
```

---

# Example: Database Connection

```python
from contextlib import contextmanager

@contextmanager
def database():

    print("Database Connected")

    yield

    print("Database Closed")


with database():

    print("Executing Query")
```

---

## Output

```text
Database Connected
Executing Query
Database Closed
```

---

# Common Built-in Context Managers

| Context Manager              | Purpose                |
| ---------------------------- | ---------------------- |
| open()                       | File Handling          |
| threading.Lock()             | Thread Synchronization |
| sqlite3.connect()            | Database Connection    |
| tempfile.TemporaryFile()     | Temporary Files        |
| contextlib.redirect_stdout() | Output Redirection     |

---

# Nested Context Managers

```python
with open("a.txt") as f1, \
     open("b.txt") as f2:

    print(f1.read())
    print(f2.read())
```

---

# Real-Time Example

## Without Context Manager

```python
connection = connect()

# execute query

connection.close()
```

Need manual cleanup.

---

## With Context Manager

```python
with connect() as connection:

    # execute query
```

Automatic cleanup.

---

# Advantages of Context Managers

### 1. Automatic Resource Cleanup

No need to manually release resources.

---

### 2. Prevent Resource Leaks

Files and connections are always closed.

---

### 3. Better Readability

Cleaner code.

---

### 4. Exception Safety

Cleanup happens even if exceptions occur.

---

### 5. Less Boilerplate Code

No need for:

```python
try
finally
```

everywhere.

---

# Context Manager vs try-finally

## Using try-finally

```python
f = open("data.txt")

try:

    print(f.read())

finally:

    f.close()
```

---

## Using Context Manager

```python
with open("data.txt") as f:

    print(f.read())
```

Cleaner and recommended.

---

# Key Takeaways

* A Context Manager manages resources automatically.
* Most commonly used with the `with` statement.
* Automatically performs setup and cleanup.
* Uses special methods:

  * `__enter__()`
  * `__exit__()`
* Resources are released even if exceptions occur.
* `open()` is the most common built-in context manager.
* Custom context managers can be created using:

  * `__enter__()` and `__exit__()`
  * `contextlib.contextmanager`
* Context Managers help write safer, cleaner, and more maintainable Python code.
