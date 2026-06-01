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

# Control Flow in `try-except`

Understanding the flow of execution in a `try-except` block is very important.

## General Structure

```python
try:
    stmt1
    stmt2
    stmt3

except ExceptionType:
    stmt4

stmt5
```

---

## Case 1: No Exception Occurs

### Flow

```text
stmt1 → stmt2 → stmt3 → stmt5
```

### Execution Order

```text
1, 2, 3, 5
```

### Result

```text
Normal Termination
```

---

## Case 2: Exception Occurs and Matching `except` Found

Suppose exception occurs in:

```text
stmt2
```

and corresponding `except` block is available.

### Flow

```text
stmt1
↓
Exception at stmt2
↓
except block (stmt4)
↓
stmt5
```

### Execution Order

```text
1, 4, 5
```

### Result

```text
Normal Termination
```

---

## Case 3: Exception Occurs but No Matching `except`

Suppose exception occurs in:

```text
stmt2
```

but matching exception handler is not available.

### Flow

```text
stmt1
↓
Exception at stmt2
↓
Program Terminates
```

### Execution Order

```text
1
```

### Result

```text
Abnormal Termination
```

---

## Case 4: Exception Occurs Inside `except` or After It

Suppose exception occurs in:

```text
stmt4
```

or

```text
stmt5
```

### Result

```text
Abnormal Termination
```

unless another try-except block handles it.

---

# Important Conclusions

## Conclusion 1

If an exception occurs anywhere inside the `try` block:

```text
Remaining statements inside try block
will not execute
```

Example:

```python
try:
    print("A")
    print(10/0)
    print("B")
except ZeroDivisionError:
    print("Handled")
```

### Output

```text
A
Handled
```

`print("B")` is never executed.

---

## Conclusion 2

Only risky code should be written inside `try`.

### Wrong Approach

```python
try:
    500 lines of code
```

### Correct Approach

```python
try:
    risky statement only
```

This improves:

* Readability
* Performance
* Debugging

---

## Conclusion 3

Exceptions may occur inside:

```text
except block
```

also.

Example:

```python
try:
    print(10/0)

except ZeroDivisionError:
    print(10/"A")
```

### Output

```text
TypeError
```

---

## Conclusion 4

Any exception outside try-except results in:

```text
Abnormal Termination
```

---

# How to Print Exception Information

Sometimes we want to know:

* What exception occurred?
* What message was generated?

Python allows us to capture the exception object.

---

## Syntax

```python
try:
    risky code

except ExceptionType as msg:
    print(msg)
```

---

## Example

```python
try:
    print(10/0)

except ZeroDivisionError as msg:
    print(
        "Exception raised and its description is:",
        msg
    )
```

### Output

```text
Exception raised and its description is:
division by zero
```

---

## Explanation

Python creates exception object:

```text
division by zero
```

and stores it inside:

```python
msg
```

---

# `try` with Multiple `except` Blocks

Different exceptions require different handling logic.

Therefore:

```text
Multiple except blocks
are recommended
```

---

## General Syntax

```python
try:
    risky code

except ZeroDivisionError:
    handling code

except FileNotFoundError:
    handling code

except ValueError:
    handling code
```

---

## Real-Time Example

```python
try:
    read remote file

except FileNotFoundError:
    use local file

except PermissionError:
    request permission
```

---

# Example Program

```python
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    print(x / y)

except ZeroDivisionError:
    print("Can't Divide with Zero")

except ValueError:
    print("Please provide integer values only")
```

---

## Execution 1

### Input

```text
10
2
```

### Output

```text
5.0
```

---

## Execution 2

### Input

```text
10
0
```

### Output

```text
Can't Divide with Zero
```

---

## Execution 3

### Input

```text
10
ten
```

### Output

```text
Please provide integer values only
```

---

# Order of Multiple `except` Blocks

The order of exception handlers is important.

Python always checks:

```text
Top → Bottom
```

until a matching handler is found.

---

## Example

```python
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    print(x / y)

except ArithmeticError:
    print("ArithmeticError")

except ZeroDivisionError:
    print("ZeroDivisionError")
```

---

### Input

```text
10
0
```

### Output

```text
ArithmeticError
```

---

## Why?

Because:

```text
ZeroDivisionError
```

is a child of:

```text
ArithmeticError
```

Python finds:

```text
ArithmeticError
```

first and executes it.

---

# Exception Hierarchy Diagram

```text
BaseException
      |
  Exception
      |
ArithmeticError
      |
ZeroDivisionError
```

---

# Rule for Ordering

Always write:

```text
Child Exceptions First
Parent Exceptions Later
```

### Correct

```python
except ZeroDivisionError:
    pass

except ArithmeticError:
    pass
```

---

### Wrong

```python
except ArithmeticError:
    pass

except ZeroDivisionError:
    pass
```

The second block becomes unreachable.

---

# Single `except` Block Handling Multiple Exceptions

Sometimes different exceptions need the same handling code.

Instead of writing multiple `except` blocks:

```python
except Exception1:
    code

except Exception2:
    code
```

we can combine them.

---

## Syntax

```python
except (
    Exception1,
    Exception2,
    Exception3
):
    handling code
```

OR

```python
except (
    Exception1,
    Exception2,
    Exception3
) as msg:
    handling code
```

---

## Important Note

Parentheses are:

```text
Mandatory
```

The exceptions are internally treated as a tuple.

---

# Example

```python
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    print(x / y)

except (
    ZeroDivisionError,
    ValueError
) as msg:

    print(
        "Please provide valid input.",
        "Problem is:",
        msg
    )
```

---

## Execution 1

### Input

```text
10
0
```

### Output

```text
Please provide valid input.
Problem is: division by zero
```

---

## Execution 2

### Input

```text
10
ten
```

### Output

```text
Please provide valid input.
Problem is:
invalid literal for int()
with base 10: 'ten'
```

---

# Comparison: Multiple `except` vs Single `except`

| Multiple `except`                     | Single `except`                  |
| ------------------------------------- | -------------------------------- |
| Different handling for each exception | Same handling for all exceptions |
| More detailed                         | More compact                     |
| Better control                        | Less code                        |

---

# Real-Time Analogy

Imagine a customer support system.

### Multiple `except`

```text
Billing Issue
    ↓
Billing Team

Technical Issue
    ↓
Technical Team

Delivery Issue
    ↓
Logistics Team
```

Each problem has separate handling.

---

### Single `except`

```text
All Issues
      ↓
General Support Team
```

Same handling for all issues.

---

# Key Takeaways

* If no exception occurs:

  * `try` executes completely.
  * `except` is skipped.

* If exception occurs:

  * Remaining statements in `try` block are skipped.

* Only risky code should be placed inside `try`.

* Exception details can be captured using:

```python
except ExceptionType as msg
```

* Multiple `except` blocks can handle different exceptions.

* Python checks exception handlers from:

```text
Top to Bottom
```

* Always write:

```text
Child Exception First
Parent Exception Later
```

* A single `except` block can handle multiple exception types.

* Parentheses are mandatory when specifying multiple exceptions in one `except` block.

