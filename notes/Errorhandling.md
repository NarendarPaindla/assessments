# Exception Handling in Python

# What is an Exception?

## Definition

An **Exception** is an unwanted and unexpected event that occurs during program execution and disturbs the normal flow of the program.

In simple words:

```text
Exception = Runtime Error
```

When an exception occurs, the program execution may stop abnormally.

---

## Examples of Exceptions

Common exceptions in Python:

* `ZeroDivisionError`
* `TypeError`
* `ValueError`
* `FileNotFoundError`
* `EOFError`

### Example

```python
print(10/0)
```

### Output

```text
ZeroDivisionError: division by zero
```

---

# Why Exception Handling is Required?

It is highly recommended to handle exceptions.

## Main Objectives

### 1. Graceful Termination

Program should not terminate abruptly.

### 2. Resource Protection

Resources should not remain blocked.

Examples:

* Files
* Database Connections
* Network Connections

### 3. Alternative Execution

If one operation fails, we should provide an alternative way to continue execution.

---

# Important Note

Exception handling does not mean:

```text
Fixing the error
```

It means:

```text
Providing an alternative solution
so the program can continue.
```

---

# Real-Time Example

Suppose a program needs to read a file from:

```text
London Server
```

If the server is unavailable:

```text
FileNotFoundError
```

Instead of stopping the application:

```text
Use local backup file
```

and continue execution.

This process is called:

```text
Exception Handling
```

---

## Example

```python
try:
    read file from London server
except FileNotFoundError:
    read local backup file
```

---

# Questions

### What is an Exception?

An unwanted event that interrupts normal execution of a program.

---

### What is Exception Handling?

Providing alternative code to continue execution when an exception occurs.

---

### What is the Purpose of Exception Handling?

* Prevent abnormal termination
* Continue execution
* Improve reliability

---

# Default Exception Handling in Python

## Important Points

### 1. Every Exception is an Object

In Python:

```text
Every Exception is an Object
```

---

### 2. Every Exception Has a Corresponding Class

Examples:

```text
ZeroDivisionError
TypeError
ValueError
```

are exception classes.

---

### 3. Python Creates Exception Objects Automatically

Whenever an exception occurs:

```text
Python creates exception object
```

and searches for handling code.

---

### 4. If Handling Code is Not Found

Python:

```text
Terminates Program Abnormally
```

and prints exception information.

---

# Example: Default Exception Handling

```python
print("Hello")

print(10/0)

print("Hi")
```

### Output

```text
Hello

Traceback (most recent call last):

ZeroDivisionError: division by zero
```

---

## Explanation

### Step 1

```python
print("Hello")
```

Output:

```text
Hello
```

---

### Step 2

```python
print(10/0)
```

Exception occurs:

```text
ZeroDivisionError
```

---

### Step 3

Program stops immediately.

Hence:

```python
print("Hi")
```

is never executed.

---

# Important Observation

When exception occurs:

```text
Remaining statements
will not execute.
```

This is called:

```text
Abnormal Termination
```

---

# Python Exception Hierarchy

All exceptions in Python follow a hierarchy.

<img width="757" height="562" alt="image" src="https://github.com/user-attachments/assets/d2d9d2f3-1ab3-4ea2-a0d9-12502faf6a50" />


Other important exceptions:

```text
SystemExit
GeneratorExit
KeyboardInterrupt
```

are directly derived from:

```text
BaseException
```

---

# Important Notes About Hierarchy

### Every Exception is a Class

Example:

```python
print(type(ZeroDivisionError))
```

Output:

```text
<class 'type'>
```

---

### BaseException is the Root Class

All exception classes are children of:

```text
BaseException
```

either directly or indirectly.

---

### Most Programmers Focus On

```text
Exception
```

and its child classes.

---

# Customized Exception Handling Using try-except

## Why Use try-except?

Some code may generate exceptions.

Such code is called:

```text
Risky Code
```

We place risky code inside:

```python
try
```

block.

---

### Syntax

```python
try:
    Risky Code

except ExceptionType:
    Handling Code
```

---

# Flow Diagram

```text
           try block
                |
        Exception?
           /     \
         Yes      No
          |        |
     except     Continue
          |
   Alternative Code
```

---

# Example Without try-except

```python
print("stmt-1")

print(10/0)

print("stmt-3")
```

### Output

```text
stmt-1

ZeroDivisionError: division by zero

Abnormal Termination
```

---

## Explanation

Execution:

```text
stmt-1
```

prints successfully.

---

Then:

```python
10/0
```

raises:

```text
ZeroDivisionError
```

Program terminates.

---

Hence:

```text
stmt-3
```

is not executed.

---

# Example With try-except

```python
print("stmt-1")

try:
    print(10/0)

except ZeroDivisionError:
    print(10/2)

print("stmt-3")
```

### Output

```text
stmt-1

5.0

stmt-3

Normal Termination
```

---

## Step-by-Step Execution

### Step 1

```python
print("stmt-1")
```

Output:

```text
stmt-1
```

---

### Step 2

Control enters:

```python
try
```

block.

---

### Step 3

```python
print(10/0)
```

raises:

```text
ZeroDivisionError
```

---

### Step 4

Python searches matching:

```python
except ZeroDivisionError
```

block.

---

### Step 5

Handling code executes:

```python
print(10/2)
```

Output:

```text
5.0
```

---

### Step 6

Program continues normally.

```python
print("stmt-3")
```

Output:

```text
stmt-3
```

---

### Result

Program terminates successfully.

```text
Graceful Termination
```

---

# Real-Time Analogy

Imagine driving a car.

Without exception handling:

```text
Road Block Found
→ Journey Ends
```

With exception handling:

```text
Road Block Found
→ Take Alternative Route
→ Reach Destination
```

The alternative route is similar to:

```python
except block
```

---

# Key Takeaways

* Exception = Runtime Error.
* Exceptions disturb normal execution.
* Every exception is an object.
* Every exception belongs to an exception class.
* `BaseException` is the root of all exception classes.
* Default exception handling causes abnormal termination.
* Remaining statements are not executed after an unhandled exception.
* `try` block contains risky code.
* `except` block contains handling code.
* Exception handling provides an alternative path for execution.
* Exception handling helps achieve graceful program termination.
* Exception handling does not fix errors; it handles them and allows the program to continue.
