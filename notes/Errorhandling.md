# Error Handling in Python

## Definition

**Error Handling** is the process of managing errors in a program so that the program **does not crash unexpectedly**.

In simple words:

```text id="k7m2xp"
Error handling helps a program
continue running even if an error occurs.
```

Python uses:

```text id="r4m9wx"
try
except
else
finally
```

for handling errors.

---

# Why Error Handling?

Suppose:

```python id="m2p7qx"
a = 10
b = 0

print(a / b)
```

### Output

```text id="t8m4wx"
ZeroDivisionError:
division by zero
```

Problem:

```text id="x5p1rx"
Program stops immediately
```

To prevent this, Python provides:

```text id="n9m3qx"
Error Handling
```

---

# Types of Errors in Python

Python mainly has **3 types of errors**:

1. Syntax Errors
2. Runtime Errors (Exceptions)
3. Logical Errors

---

# 1) Syntax Errors

## Definition

Syntax errors occur when Python rules are written incorrectly.

Example:

```python id="w3m8wx"
if True
    print("Hello")
```

### Output

```text id="p2m7qx"
SyntaxError:
invalid syntax
```

### Problem

Colon `:` is missing.

Correct Code:

```python id="r8m4wx"
if True:
    print("Hello")
```

---

# 2) Runtime Errors (Exceptions)

## Definition

Runtime errors occur during execution.

Example:

```python id="x1m9qx"
print(10 / 0)
```

### Output

```text id="g7p2rx"
ZeroDivisionError
```

---

## Common Runtime Errors

| Error Type          | Meaning                |
| ------------------- | ---------------------- |
| `ZeroDivisionError` | Divide by zero         |
| `NameError`         | Variable not found     |
| `TypeError`         | Wrong datatype         |
| `ValueError`        | Invalid value          |
| `IndexError`        | Invalid index          |
| `KeyError`          | Dictionary key missing |
| `FileNotFoundError` | File not found         |

---

### Example: `NameError`

```python id="t4m7wx"
print(name)
```

### Output

```text id="y2m8qx"
NameError:
name 'name' is not defined
```

---

### Example: `TypeError`

```python id="p1m9rx"
print(10 + "20")
```

### Output

```text id="g3m7wx"
TypeError
```

Reason:

```text id="n8p4rx"
Cannot add integer and string
```

---

### Example: `IndexError`

```python id="v5m2qx"
numbers = [10, 20, 30]

print(numbers[5])
```

### Output

```text id="q9m1wx"
IndexError
```

Reason:

```text id="r6p8rx"
Index 5 does not exist
```

---

# 3) Logical Errors

## Definition

Program runs successfully but gives wrong output.

Example:

```python id="m7p2qx"
a = 10
b = 20

print(a - b)
```

Expected:

```text id="j1m8wx"
30
```

Actual:

```text id="h4p7rx"
-10
```

Program runs, but logic is wrong.

---

# Exception Handling in Python

Python handles runtime errors using:

```text id="x8m3qx"
try
except
```

---

# `try` Block

## Definition

Code that may cause an error is written inside `try`.

Example:

```python id="w2m9wx"
try:
    print(10 / 0)
```

---

# `except` Block

## Definition

If error occurs, control goes to `except`.

Example:

```python id="k5m1qx"
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Output

```text id="p8m4rx"
Cannot divide by zero
```

---

## Step-by-Step Explanation

### Try Executes

```python id="g1m7wx"
print(10 / 0)
```

Error occurs:

```text id="x4p2rx"
ZeroDivisionError
```

Python jumps to:

```python id="r9m3qx"
except ZeroDivisionError:
```

Output:

```text id="m6p8wx"
Cannot divide by zero
```

Program does not crash.

---

# Syntax of Exception Handling

```python id="q2m7rx"
try:
    risky code

except ErrorType:
    handling code
```

---

# Example 1: Division Program

```python id="t5m9wx"
try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Multiple `except` Blocks

We can handle different errors separately.

Example:

```python id="v1m8qx"
try:
    a = int(input("Enter Number: "))
    print(10 / a)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input")
```

---

## Explanation

### Case 1

Input:

```text id="n3m7wx"
0
```

Output:

```text id="r8p2rx"
Cannot divide by zero
```

---

### Case 2

Input:

```text id="g4m9qx"
abc
```

Output:

```text id="t7p1rx"
Invalid Input
```

---

# Generic `except`

Handles any error.

Example:

```python id="p2m8wx"
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

### Output

```text id="m9p4rx"
division by zero
```

---

## Explanation

```python id="w6m2qx"
Exception as e
```

Stores error message in:

```text id="k1m7wx"
e
```

---

# `else` Block

## Definition

Runs only if **no exception occurs**.

Example:

```python id="x5p8rx"
try:
    num = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success")
```

### Output

```text id="q7m1wx"
Success
```

---

# `finally` Block

## Definition

Always executes whether error occurs or not.

Example:

```python id="r3m9qx"
try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Program Finished")
```

### Output

```text id="v8m2wx"
Error
Program Finished
```

---

# Complete Example

```python id="n4p7rx"
try:
    number = int(input("Enter Number: "))

    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid number")

else:
    print("Result:", result)

finally:
    print("Execution Completed")
```

---

# Flow Diagram

```text id="t2m8qx"
        try
          │
    Error Occurs?
       /      \
     Yes       No
      │         │
   except      else
      │         │
       \       /
         finally
```

---

# Real-Life Analogy

Imagine ATM withdrawal.

```text id="g9m4wx"
try → Withdraw money

except → Handle problems
          (wrong PIN, no balance)

else → Cash received

finally → Card returned
```

No matter what happens:

```text id="y1p7rx"
Card is returned
```

Similarly:

```text id="w5m2qx"
finally always executes
```

---

# Important Rules

### 1. `try` must have `except` or `finally`

Correct:

```python id="r2m9wx"
try:
    pass

except:
    pass
```

---

### 2. Multiple `except` allowed

Example:

```python id="x8m1qx"
except ValueError:
except TypeError:
```

---

### 3. `finally` always runs

Even if error occurs.

---

### 4. `else` runs only if no error

---

# `try`, `except`, `else`, `finally`

| Block     | Purpose          |
| --------- | ---------------- |
| `try`     | Risky code       |
| `except`  | Handle error     |
| `else`    | Runs if no error |
| `finally` | Always runs      |

---

# Common Interview Questions

### Q1: What is Error Handling?

**Answer:**
Error handling is the process of managing runtime errors to prevent program crashes.

---

### Q2: What is the purpose of `try` block?

**Answer:**
It contains code that may generate exceptions.

---

### Q3: When does `else` execute?

**Answer:**
Only if no exception occurs.

---

### Q4: Does `finally` always execute?

**Answer:**
Yes.

---

### Q5: Difference between Syntax Error and Runtime Error?

| Syntax Error            | Runtime Error           |
| ----------------------- | ----------------------- |
| Occurs before execution | Occurs during execution |
| Wrong syntax            | Unexpected issue        |

---

# Key Takeaways

* Errors are mainly:

  1. Syntax Errors
  2. Runtime Errors
  3. Logical Errors

* Runtime errors are called **Exceptions**.

* Python handles exceptions using:

```python id="q4m8rx"
try
except
else
finally
```

* `try` → risky code

* `except` → handles errors

* `else` → executes if no error

* `finally` → always executes

* Multiple exceptions can be handled separately.

* `Exception as e` helps display error messages.
