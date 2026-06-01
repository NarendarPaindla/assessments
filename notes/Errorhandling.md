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


# Default `except` Block

## What is a Default `except` Block?

A **default `except` block** can handle:

```text
Any type of exception
```

when no specific exception handler matches.

It acts as a:

```text
Fallback Exception Handler
```

---

## Syntax

```python
try:
    risky code

except:
    handling code
```

---

## Example

```python
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    print(x / y)

except ZeroDivisionError:
    print(
        "ZeroDivisionError: Can't divide by zero"
    )

except:
    print(
        "Default Except: Please provide valid input only"
    )
```

---

## Execution 1

### Input

```text
Enter First Number: 10
Enter Second Number: 0
```

### Output

```text
ZeroDivisionError:
Can't divide by zero
```

---

### Explanation

Exception Raised:

```text
ZeroDivisionError
```

Matching handler found:

```python
except ZeroDivisionError:
```

So this block executes.

---

## Execution 2

### Input

```text
Enter First Number: 10
Enter Second Number: ten
```

### Output

```text
Default Except:
Please provide valid input only
```

---

### Explanation

Exception Raised:

```text
ValueError
```

No specific handler available.

Therefore:

```python
except:
```

handles it.

---

# Important Rule

When multiple exception handlers are present:

```text
Default except block
must always be the last block
```

Otherwise:

```text
SyntaxError
```

occurs.

---

## Wrong Example

```python
try:
    print(10/0)

except:
    print("Default Except")

except ZeroDivisionError:
    print("ZeroDivisionError")
```

### Output

```text
SyntaxError:
default 'except:' must be last
```

---

## Why?

Because:

```text
Default except can catch every exception.
```

If it appears first:

```text
Other except blocks become unreachable.
```

---

# Valid Forms of `except` Block

Python supports several forms.

---

## 1. Specific Exception

```python
except ZeroDivisionError:
```

Handles only:

```text
ZeroDivisionError
```

---

## 2. Specific Exception with Message

```python
except ZeroDivisionError as msg:
```

Handles exception and stores error description in:

```python
msg
```

---

## 3. Multiple Exceptions

```python
except (
    ZeroDivisionError,
    ValueError
):
```

Handles both exceptions.

---

## 4. Multiple Exceptions with Message

```python
except (
    ZeroDivisionError,
    ValueError
) as msg:
```

Stores exception description in:

```python
msg
```

---

## 5. Default Exception Handler

```python
except:
```

Handles any exception.

---

# Finally Block

## What is a Finally Block?

The **finally block** is used for:

```text
Cleanup Code
```

or

```text
Resource Release Code
```

---

## Why Not Put Cleanup Code Inside try?

Not all statements inside:

```python
try
```

are guaranteed to execute.

An exception may interrupt execution.

---

## Why Not Put Cleanup Code Inside except?

If no exception occurs:

```python
except
```

will not execute.

---

## Solution

Python provides:

```python
finally
```

block.

---

## Main Purpose of Finally Block

Used to write:

* File closing code
* Database connection closing code
* Network connection release code
* Memory cleanup code

---

## General Structure

```python
try:
    Risky Code

except:
    Handling Code

finally:
    Cleanup Code
```

---

# Special Property of Finally Block

The `finally` block executes:

```text
Always
```

regardless of:

* Exception raised or not
* Exception handled or not
* Program terminates normally or abnormally

---

# Case 1: No Exception

## Program

```python
try:
    print("try")

except:
    print("except")

finally:
    print("finally")
```

### Output

```text
try
finally
```

---

## Flow

```text
try
 ↓
finally
```

---

# Case 2: Exception Raised and Handled

## Program

```python
try:
    print("try")
    print(10/0)

except ZeroDivisionError:
    print("except")

finally:
    print("finally")
```

### Output

```text
try
except
finally
```

---

## Flow

```text
try
 ↓
Exception
 ↓
except
 ↓
finally
```

---

# Case 3: Exception Raised but Not Handled

## Program

```python
try:
    print("try")
    print(10/0)

except NameError:
    print("except")

finally:
    print("finally")
```

### Output

```text
try
finally

ZeroDivisionError:
division by zero
```

---

## Explanation

Exception:

```text
ZeroDivisionError
```

No matching handler found.

Still:

```python
finally
```

executes before program terminates.

---

## Flow

```text
try
 ↓
Exception
 ↓
finally
 ↓
Abnormal Termination
```

---

# Real-Time Example

## File Handling

```python
file = open("data.txt")

try:
    process file

except:
    handle errors

finally:
    file.close()
```

### Why?

Whether:

* Processing succeeds
* Processing fails

the file must be closed.

---

# Important Note

There is only **one situation** where `finally` block may not execute.

---

## Using `os._exit()`

When:

```python
os._exit()
```

is called,

Python Virtual Machine (PVM) immediately shuts down.

Therefore:

```text
finally block is skipped
```

---

## Example

```python
import os

try:
    print("try")

    os._exit(0)

except NameError:
    print("except")

finally:
    print("finally")
```

### Output

```text
try
```

---

## Explanation

Execution reaches:

```python
os._exit(0)
```

Python Virtual Machine stops immediately.

Hence:

```python
finally
```

never executes.

---

# Control Flow of try-except-finally

```text
            try
             |
      Exception ?
       /        \
     No          Yes
     |            |
 Continue      Matching
     |          except
     |            |
      \          /
        finally
           |
       Program End
```

---

# Comparison: try vs except vs finally

| Block          | Purpose          | Executes When                   |
| -------------- | ---------------- | ------------------------------- |
| try            | Risky code       | Always                          |
| except         | Handling code    | Only when exception occurs      |
| finally        | Cleanup code     | Always                          |
| default except | Generic handling | When no matching handler exists |

---

# Key Takeaways

* `except:` without exception type is called:

```text
Default Exception Handler
```

* Default except should always be:

```text
Last except block
```

* `finally` is mainly used for:

```text
Cleanup code
```

* `finally` executes whether:

  * Exception occurs
  * Exception does not occur
  * Exception is handled
  * Exception is not handled

* Typical cleanup tasks:

  * Closing files
  * Closing database connections
  * Releasing network resources

* Only exceptional case where finally may not execute:

```python
os._exit()
```

* `try` → Risky code
* `except` → Error handling
* `finally` → Cleanup code always executed
# Control Flow in `try-except-finally`

## General Structure

```python
try:
    stmt1
    stmt2
    stmt3

except ExceptionType:
    stmt4

finally:
    stmt5
    stmt6
```

---

# Important Note About `os._exit(0)`

```python
os._exit(0)
```

### Meaning

* `0` represents status code.
* Status code `0` indicates:

```text
Normal Program Termination
```

Different status codes can be used to indicate different termination conditions.

---

# Case 1: No Exception

### Execution Flow

```text
stmt1 → stmt2 → stmt3 → stmt5 → stmt6
```

### Execution Order

```text
1, 2, 3, 5, 6
```

### Result

```text
Normal Termination
```

---

# Case 2: Exception Raised and Matching Except Found

Suppose exception occurs at:

```text
stmt2
```

and matching handler exists.

### Execution Flow

```text
stmt1
↓
Exception
↓
stmt4
↓
stmt5
↓
stmt6
```

### Execution Order

```text
1, 4, 5, 6
```

### Result

```text
Normal Termination
```

---

# Case 3: Exception Raised but Matching Except Not Found

Suppose exception occurs at:

```text
stmt2
```

and no matching handler exists.

### Execution Flow

```text
stmt1
↓
Exception
↓
finally
↓
Program Terminates
```

### Execution Order

```text
1, 5
```

### Result

```text
Abnormal Termination
```

---

# Case 4: Exception Raised Inside `except`

Suppose exception occurs at:

```text
stmt4
```

inside the except block.

### Execution Flow

```text
try
↓
except
↓
Exception
↓
finally
↓
Program Terminates
```

### Result

```text
Abnormal Termination
```

But before termination:

```text
finally block executes
```

---

# Case 5: Exception Raised Inside `finally`

Suppose exception occurs at:

```text
stmt5
```

or

```text
stmt6
```

### Result

```text
Abnormal Termination
```

because exception occurred inside finally block itself.

---

# Summary Diagram

```text
                try
                 |
           Exception ?
          /          \
        No            Yes
        |             |
      except?       Matching?
        |          /       \
        |        Yes       No
        |         |         |
        |      except    skip
        |         |         |
        +---------+---------+
                  |
              finally
                  |
          Program End
```

---

# Nested try-except-finally Blocks

## Definition

Placing one:

```text
try-except-finally
```

block inside another:

```text
try-except-finally
```

block is called:

```text
Nested Exception Handling
```

---

## General Structure

```python
try:

    statements

    try:
        statements

    except:
        statements

    finally:
        statements

except:
    statements

finally:
    statements
```

---

# Why Nested Exception Handling?

Sometimes:

* Program contains multiple risky operations.
* Different levels require different handling.
* Inner block handles local exceptions.
* Outer block acts as backup handler.

---

# Rule

### Outer Try Block

Contains:

```text
General Risky Code
```

### Inner Try Block

Contains:

```text
Highly Risky Code
```

---

# Exception Handling Priority

```text
Inner Handler
      ↓
Outer Handler
```

Python always tries:

```text
Nearest Handler First
```

---

# Example

```python
try:

    print("Outer try block")

    try:

        print("Inner try block")

        print(10/0)

    except ZeroDivisionError:

        print("Inner except block")

    finally:

        print("Inner finally block")

except:

    print("Outer except block")

finally:

    print("Outer finally block")
```

---

## Output

```text
Outer try block

Inner try block

Inner except block

Inner finally block

Outer finally block
```

---

# Explanation

### Step 1

Outer try executes.

```text
Outer try block
```

printed.

---

### Step 2

Inner try executes.

```text
Inner try block
```

printed.

---

### Step 3

Exception occurs.

```python
10/0
```

raises:

```text
ZeroDivisionError
```

---

### Step 4

Python searches nearest handler.

Found:

```python
except ZeroDivisionError
```

inside inner block.

---

### Step 5

Inner handler executes.

```text
Inner except block
```

printed.

---

### Step 6

Inner finally executes.

```text
Inner finally block
```

printed.

---

### Step 7

Control returns to outer block.

Outer finally executes.

```text
Outer finally block
```

printed.

---

# Control Flow in Nested try-except-finally

## Structure

```python
try:
    stmt1
    stmt2
    stmt3

    try:
        stmt4
        stmt5
        stmt6

    except X:
        stmt7

    finally:
        stmt8
        stmt9

except Y:
    stmt10

finally:
    stmt11
    stmt12
```

---

# Case 1: No Exception

### Execution Order

```text
1,2,3,4,5,6,8,9,11,12
```

### Result

```text
Normal Termination
```

---

# Case 2: Exception at stmt2 and Outer Handler Matches

### Execution Order

```text
1,10,11,12
```

### Result

```text
Normal Termination
```

---

# Case 3: Exception at stmt2 and Outer Handler Does Not Match

### Execution Order

```text
1,11
```

### Result

```text
Abnormal Termination
```

---

# Case 4: Exception at stmt5 and Inner Handler Matches

### Execution Order

```text
1,2,3,4,7,8,9,11,12
```

### Result

```text
Normal Termination
```

---

# Case 5: Exception at stmt5

Inner handler does not match.

Outer handler matches.

### Execution Order

```text
1,2,3,4,8,10,11,12
```

### Result

```text
Normal Termination
```

---

# Case 6: Exception at stmt5

Neither inner nor outer handler matches.

### Execution Order

```text
1,2,3,4,8,11
```

### Result

```text
Abnormal Termination
```

---

# Case 7: Exception at stmt7 and Outer Handler Matches

### Execution Order

```text
1,2,3,...,8,10,11,12
```

### Result

```text
Normal Termination
```

---

# Case 8: Exception at stmt7 and Outer Handler Does Not Match

### Execution Order

```text
1,2,3,...,8,11
```

### Result

```text
Abnormal Termination
```

---

# Case 9: Exception at stmt8 and Outer Handler Matches

### Execution Order

```text
1,2,3,...,10,11,12
```

### Result

```text
Normal Termination
```

---

# Case 10: Exception at stmt8 and Outer Handler Does Not Match

### Execution Order

```text
1,2,3,...,11
```

### Result

```text
Abnormal Termination
```

---

# Real-Time Analogy

Imagine a company hierarchy:

```text
Employee
   ↓
Team Lead
   ↓
Manager
```

If Employee cannot solve a problem:

```text
Escalate to Team Lead
```

If Team Lead cannot solve it:

```text
Escalate to Manager
```

Similarly:

```text
Inner Handler
      ↓
Outer Handler
```

This is exactly how nested exception handling works.

---

# Key Takeaways

* `finally` executes whether exception occurs or not.
* `finally` executes before abnormal termination.
* Nested try-except-finally blocks are allowed.
* Python always searches for the nearest exception handler first.
* Inner exception handlers get higher priority.
* If inner handler cannot handle exception, it propagates to outer handler.
* Both inner and outer finally blocks execute when control passes through them.
* Nested exception handling is useful for large applications with multiple risky operations.
* `os._exit(0)` is a special case where finally block may not execute.

# Control Flow in Nested `try-except-finally` (Continued)

Consider the structure:

```python
try:
    stmt1
    stmt2
    stmt3

    try:
        stmt4
        stmt5
        stmt6

    except X:
        stmt7

    finally:
        stmt8
        stmt9

except Y:
    stmt10

finally:
    stmt11
    stmt12
```

---

# Case 11: Exception Raised at `stmt9` and Matching Outer `except` Found

Suppose:

```text
Exception occurs at stmt9
```

and outer exception handler matches.

### Execution Order

```text
1,2,3,....,8,10,11,12
```

### Result

```text
Normal Termination
```

---

## Explanation

Flow:

```text
Inner finally executes
      ↓
Exception at stmt9
      ↓
Outer except handles it
      ↓
Outer finally executes
      ↓
Program ends normally
```

---

# Case 12: Exception Raised at `stmt9` and Outer `except` Does Not Match

### Execution Order

```text
1,2,3,....,8,11
```

### Result

```text
Abnormal Termination
```

---

## Explanation

Flow:

```text
Exception in stmt9
      ↓
Outer except cannot handle
      ↓
Outer finally executes
      ↓
Program terminates
```

---

# Case 13: Exception Raised at `stmt10`

Suppose exception occurs inside:

```text
Outer except block
```

at:

```text
stmt10
```

### Result

```text
Abnormal Termination
```

However:

```text
stmt11 (finally)
```

will execute before termination.

---

## Flow

```text
Outer except
      ↓
Exception
      ↓
Outer finally
      ↓
Abnormal Termination
```

---

# Case 14: Exception Raised at `stmt11` or `stmt12`

Suppose exception occurs inside:

```text
Outer finally block
```

### Result

```text
Abnormal Termination
```

because exception occurred inside the final cleanup code itself.

---

# Important Note About Finally Block

## Rule 1

If control enters a:

```python
try
```

block,

then:

```python
finally
```

block will definitely execute.

---

## Rule 2

If control never enters:

```python
try
```

block,

then:

```python
finally
```

block will not execute.

---

# `else` Block with `try-except-finally`

Python also supports:

```python
else
```

with exception handling.

---

# Purpose of `else`

The `else` block executes:

```text
Only when no exception occurs
inside try block.
```

---

# Structure

```python
try:
    Risky Code

except:
    Handling Code

else:
    No Exception Code

finally:
    Cleanup Code
```

---

# Responsibilities of Each Block

| Block   | Purpose                           |
| ------- | --------------------------------- |
| try     | Risky code                        |
| except  | Executes when exception occurs    |
| else    | Executes when no exception occurs |
| finally | Executes always                   |

---

# Flow Diagram

```text
                 try
                   |
            Exception ?
            /       \
          Yes        No
          |           |
       except       else
          \           /
           \         /
             finally
                 |
               End
```

---

# Example

```python
try:

    print("try")

    print(10/0)

except:

    print("except")

else:

    print("else")

finally:

    print("finally")
```

---

## Output

```text
try
except
finally
```

---

## Why `else` Not Executed?

Because:

```python
print(10/0)
```

raised:

```text
ZeroDivisionError
```

Hence:

```text
else block skipped
```

---

# Example Without Exception

```python
try:

    print("try")

    print(10/2)

except:

    print("except")

else:

    print("else")

finally:

    print("finally")
```

### Output

```text
try
5.0
else
finally
```

---

## Why?

No exception occurred.

Hence:

```text
else block executed
```

---

# Comparison

| Situation             | try | except  | else | finally |
| --------------------- | --- | ------- | ---- | ------- |
| No Exception          | Yes | No      | Yes  | Yes     |
| Exception Handled     | Yes | Yes     | No   | Yes     |
| Exception Not Handled | Yes | Partial | No   | Yes     |

---

# Various Possible Combinations of try-except-else-finally

---

## Rule 1

Whenever we write:

```python
try
```

block,

we must write at least one of:

```python
except
```

or

```python
finally
```

---

### Invalid

```python
try:
    print("Hello")
```

### Result

```text
Syntax Error
```

---

## Rule 2

Whenever we write:

```python
except
```

block,

corresponding:

```python
try
```

block is mandatory.

---

### Invalid

```python
except:
    print("Hello")
```

### Result

```text
Syntax Error
```

---

## Rule 3

Whenever we write:

```python
finally
```

block,

corresponding:

```python
try
```

block is mandatory.

---

### Invalid

```python
finally:
    print("Hello")
```

### Result

```text
Syntax Error
```

---

## Rule 4

We can write:

```text
Multiple except blocks
```

for a single try block.

---

### Valid

```python
try:
    pass

except ValueError:
    pass

except ZeroDivisionError:
    pass
```

---

## Rule 5

We cannot write:

```text
Multiple finally blocks
```

for the same try.

---

### Invalid

```python
try:
    pass

finally:
    pass

finally:
    pass
```

### Result

```text
Syntax Error
```

---

## Rule 6

If we write:

```python
else
```

then:

```python
except
```

must also be present.

---

### Invalid

```python
try:
    pass

else:
    pass
```

### Result

```text
Syntax Error
```

---

### Valid

```python
try:
    pass

except:
    pass

else:
    pass
```

---

## Rule 7

Order of Blocks is Important

Correct order:

```python
try
except
else
finally
```

---

### Valid

```python
try:
    pass

except:
    pass

else:
    pass

finally:
    pass
```

---

### Invalid

```python
try:
    pass

finally:
    pass

except:
    pass
```

### Result

```text
Syntax Error
```

---

## Rule 8

Nesting is Possible

We can define:

```text
try
except
else
finally
```

inside:

* try block
* except block
* else block
* finally block

---

### Example

```python
try:

    try:
        pass

    except:
        pass

finally:
    pass
```

Valid.

---

# Valid and Invalid Combinations

## Invalid

### Only try

```python
try:
    print("try")
```

Not allowed.

---

## Invalid

### Only except

```python
except:
    print("Hello")
```

Not allowed.

---

## Invalid

### Only else

```python
else:
    print("Hello")
```

Not allowed.

---

## Invalid

### Only finally

```python
finally:
    print("Hello")
```

Not allowed.

---

## Valid

### try + except

```python
try:
    print("try")

except:
    print("except")
```

Allowed.

---

## Valid

### try + finally

```python
try:
    print("try")

finally:
    print("finally")
```

Allowed.

---

# Real-Time Analogy

Imagine an online payment system.

### try

```text
Process Payment
```

### except

```text
Handle Failure
```

### else

```text
Send Success Message
```

### finally

```text
Close Connection
Release Resources
```

Whether payment succeeds or fails:

```text
Connection must be closed
```

which is exactly the purpose of:

```python
finally
```

---

# Key Takeaways

* `else` executes only when no exception occurs.
* `finally` executes whether exception occurs or not.
* `try` must be followed by `except` or `finally`.
* `except` cannot exist without `try`.
* `finally` cannot exist without `try`.
* Multiple `except` blocks are allowed.
* Multiple `finally` blocks are not allowed.
* `else` requires an `except` block.
* Correct order:

```text
try → except → else → finally
```

* Nested try-except-else-finally blocks are fully supported.
* If control enters `try`, corresponding `finally` will execute (except special cases like `os._exit()`).
# Types of Exceptions in Python

In Python, exceptions are broadly classified into:

1. Predefined Exceptions
2. User Defined Exceptions (Customized Exceptions)

---

# 1) Predefined Exceptions

## Definition

Predefined exceptions are also called:

```text
Built-in Exceptions
```

These exceptions are automatically raised by Python Virtual Machine (PVM) whenever a specific error condition occurs.

---

## Example 1: ZeroDivisionError

When we divide a number by zero:

```python
print(10/0)
```

### Output

```text
ZeroDivisionError: division by zero
```

Python automatically raises:

```text
ZeroDivisionError
```

---

## Example 2: ValueError

When input cannot be converted to required datatype.

```python
x = int("ten")
```

### Output

```text
ValueError:
invalid literal for int()
```

Python automatically raises:

```text
ValueError
```

---

## Common Predefined Exceptions

| Exception         | Description                |
| ----------------- | -------------------------- |
| ZeroDivisionError | Division by zero           |
| ValueError        | Invalid value supplied     |
| TypeError         | Invalid datatype operation |
| IndexError        | Invalid index              |
| KeyError          | Invalid dictionary key     |
| FileNotFoundError | File not found             |
| NameError         | Variable not defined       |

---

# 2) User Defined Exceptions

## Definition

User Defined Exceptions are also called:

```text
Customized Exceptions
```

or

```text
Programmatic Exceptions
```

These exceptions are created by programmers according to business requirements.

Python does not know when these exceptions should occur.

Therefore:

```text
Programmer must explicitly define
and raise them.
```

---

## Why User Defined Exceptions?

Sometimes predefined exceptions are not enough.

Business rules may require special validations.

### Examples

```text
InsufficientFundsException

InvalidInputException

TooYoungException

TooOldException

InvalidAgeException

LowAttendanceException
```

These exceptions are not available in Python by default.

We must create them ourselves.

---

# Real-Time Example

Consider an Online Banking System.

### Rule

Customer can withdraw money only if:

```text
Balance >= Withdrawal Amount
```

If balance is insufficient:

```text
InsufficientFundsException
```

should be raised.

Python does not know this rule.

Programmer must implement it.

---

# How to Define Customized Exceptions?

Every exception in Python is a class.

Custom exceptions should inherit from:

```python
Exception
```

class directly or indirectly.

---

## Syntax

```python
class CustomException(Exception):

    def __init__(self, arg):
        self.msg = arg
```

---

## Explanation

### CustomException

Name of user-defined exception.

---

### Exception

Parent class.

---

### self.msg

Stores custom error message.

---

# Example: TooYoungException

```python
class TooYoungException(Exception):

    def __init__(self, arg):
        self.msg = arg
```

---

## Class Diagram

```text
BaseException
      |
  Exception
      |
TooYoungException
```

---

## Raising Exception

Custom exceptions are raised using:

```python
raise
```

keyword.

### Syntax

```python
raise ExceptionName("Message")
```

---

## Example

```python
raise TooYoungException(
    "Age is too low"
)
```

---

# Example: Marriage Eligibility System

## Requirement

### Rule 1

If age is less than 18:

```text
TooYoungException
```

---

### Rule 2

If age is greater than 60:

```text
TooOldException
```

---

### Rule 3

Otherwise:

```text
Eligible
```

---

## Program

```python
class TooYoungException(Exception):

    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):

    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter Age: "))

if age < 18:

    raise TooYoungException(
        "Please wait some more time."
    )

elif age > 60:

    raise TooOldException(
        "Age crossed eligibility limit."
    )

else:

    print(
        "You will get match details soon."
    )
```

---

# Execution 1

### Input

```text
Enter Age: 12
```

### Output

```text
TooYoungException:
Please wait some more time.
```

---

## Explanation

Condition:

```python
age < 18
```

became:

```text
True
```

Therefore:

```python
raise TooYoungException(...)
```

executed.

---

# Execution 2

### Input

```text
Enter Age: 90
```

### Output

```text
TooOldException:
Age crossed eligibility limit.
```

---

## Explanation

Condition:

```python
age > 60
```

became:

```text
True
```

Therefore:

```python
raise TooOldException(...)
```

executed.

---

# Execution 3

### Input

```text
Enter Age: 27
```

### Output

```text
You will get match details soon.
```

---

## Explanation

Age satisfies:

```text
18 ≤ Age ≤ 60
```

Therefore:

No exception raised.

---

# How `raise` Works

The `raise` keyword is used to:

```text
Explicitly create
and throw an exception
```

---

## General Syntax

```python
raise ExceptionType(
    "Error Message"
)
```

---

## Example

```python
raise ValueError(
    "Invalid Marks"
)
```

---

## Example

```python
raise Exception(
    "Something Went Wrong"
)
```

---

# Real-Time Analogy

Imagine a security guard at a company entrance.

### Valid Employee

```text
Allow Entry
```

---

### Unauthorized Person

```text
Raise Alarm
```

The alarm is similar to:

```python
raise Exception()
```

---

# Important Note

The `raise` keyword is mainly useful for:

```text
User Defined Exceptions
```

because Python does not know when they should occur.

---

### For Predefined Exceptions

Python generally raises them automatically.

Example:

```python
10 / 0
```

Python automatically raises:

```text
ZeroDivisionError
```

No need to use:

```python
raise ZeroDivisionError
```

manually in most situations.

---

# Exception Creation Flow

```text
Business Rule
      |
      v
Condition Check
      |
      v
Condition Failed?
   /        \
 No          Yes
 |            |
 Continue    raise Exception
                |
                v
         Exception Object Created
                |
                v
          Program Terminated
          (unless handled)
```

---

# Comparison: Predefined vs User Defined Exceptions

| Predefined Exceptions      | User Defined Exceptions          |
| -------------------------- | -------------------------------- |
| Built into Python          | Created by Programmer            |
| Raised automatically       | Raised manually using `raise`    |
| Common runtime errors      | Business-rule validations        |
| Example: ZeroDivisionError | Example: TooYoungException       |
| Python knows when to raise | Programmer decides when to raise |

---

# Key Takeaways

* Python supports:

  * Predefined Exceptions
  * User Defined Exceptions

* Predefined exceptions are automatically raised by Python.

* User defined exceptions are created by programmers.

* Custom exceptions should inherit from:

```python
Exception
```

* Exceptions are raised using:

```python
raise
```

keyword.

* Syntax:

```python
raise CustomException("message")
```

* Custom exceptions help implement business rules.

* Examples:

  * InsufficientFundsException
  * InvalidInputException
  * TooYoungException
  * TooOldException

* `raise` is especially useful for customized exceptions where Python has no built-in knowledge of the application's rules.

<img width="342" height="282" alt="image" src="https://github.com/user-attachments/assets/1748e0d0-f19f-4aa1-a81a-c994f8d21fe5" />
<img width="366" height="698" alt="image" src="https://github.com/user-attachments/assets/0d71b355-c9f2-49aa-9af8-1badf66d65c4" />
<img width="353" height="692" alt="image" src="https://github.com/user-attachments/assets/422bbde8-2e56-405e-be23-14f7bc213027" />
<img width="346" height="707" alt="image" src="https://github.com/user-attachments/assets/ad727f8a-1007-433f-9f67-5d74c00603c8" />
<img width="343" height="262" alt="image" src="https://github.com/user-attachments/assets/16c74004-c013-49d4-9af8-8e0440c2b3bb" />




