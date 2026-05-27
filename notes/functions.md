
---

## 🧩 What is a Function?
A **function** is like a reusable "mini-program" inside your code.  
- It groups instructions together.  
- You can "call" it whenever you need it.  
- It saves time because you don’t have to repeat the same code again and again.

Think of it like a **microwave oven**:  
- You put food inside, press a button, and it does its job.  
- You don’t need to know all the details of how it works inside.  
- You just use it when needed.

---

## 📝 Basic Python Function Example

```python
# Defining a function
def greet(name):
    print("Hello", name, "Welcome to Python!")

# Calling the function
greet("Rahul")
greet("Anita")
```

### 🔍 Explanation:
- `def greet(name):` → This defines a function called **greet** that takes one input (`name`).
- `print("Hello", name, "Welcome to Python!")` → This is what the function does.
- `greet("Rahul")` → Calls the function with "Rahul".
- `greet("Anita")` → Calls the function with "Anita".

Output:
```
Hello Rahul Welcome to Python!
Hello Anita Welcome to Python!
```

---

## 🍕 Real-World Example: Pizza Order Function

Imagine you run a pizza shop. Instead of writing the same steps every time someone orders, you can use a function:

```python
def order_pizza(size, topping):
    print("You ordered a", size, "pizza with", topping)

# Calling the function
order_pizza("Large", "Cheese")
order_pizza("Medium", "Paneer")
```

Output:
```
You ordered a Large pizza with Cheese
You ordered a Medium pizza with Paneer
```

---

## 🎯 Why Functions Are Useful
- **Reusability**: Write once, use many times.
- **Organization**: Code looks cleaner and easier to read.
- **Flexibility**: Functions can take inputs and give outputs.
- **Debugging**: Easier to find and fix errors.

---


---

## 🔑 Types of Functions in Python

### 1. **Built-in Functions**
These are already provided by Python. You don’t need to write them yourself.

Example:
```python
print("Hello World")   # prints text
len("Python")          # gives length of string
max(10, 20, 30)        # finds maximum number
```

Output:
```
Hello World
6
30
```

---

### 2. **User-defined Functions**
These are functions you create yourself to perform specific tasks.

Example:
```python
def greet(name):
    print("Hello", name)

greet("Rahul")
greet("Anita")
```

Output:
```
Hello Rahul
Hello Anita
```

---

### 3. **Functions with Parameters**
These take inputs (arguments) to work with.

Example:
```python
def add_numbers(a, b):
    print("Sum is:", a + b)

add_numbers(5, 3)
add_numbers(10, 20)
```

Output:
```
Sum is: 8
Sum is: 30
```

---

### 4. **Functions with Return Values**
Instead of just printing, they return a result that can be stored or used later.

Example:
```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Result is:", result)
```

Output:
```
Result is: 20
```

---

### 5. **Lambda Functions**
These are small, anonymous functions written in one line.

Example:
```python
square = lambda x: x * x
print(square(6))
```

Output:
```
36
```

---

### 6. **Recursive Functions**
A function that calls itself to solve problems like factorial or Fibonacci.

Example (factorial):
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
```

Output:
```
120
```

---

## 📊 Summary Table

| **Type of Function** | **Example** | **Use Case** |
|-----------------------|-------------|--------------|
| **Built-in** | `print()`, `len()` | Ready-made tools |
| **User-defined** | `def greet()` | Custom tasks |
| **With Parameters** | `def add(a,b)` | Input flexibility |
| **With Return** | `def multiply()` | Store/use results |
| **Lambda** | `lambda x: x*x` | Quick one-liners |
| **Recursive** | `def factorial()` | Problems with repetition |

---

# Types of Arguments in Python

## What are Arguments?

Arguments are values passed to a function when calling it.

Example:

```python
def f1(a, b):
    print(a + b)

f1(10, 20)
```

### Understanding the Terms

| Term                          | Meaning                               | Example    |
| ----------------------------- | ------------------------------------- | ---------- |
| Formal Arguments (Parameters) | Variables used in function definition | `a`, `b`   |
| Actual Arguments              | Real values passed to function        | `10`, `20` |

In the above example:

* `a` and `b` are **formal arguments (parameters)**
* `10` and `20` are **actual arguments**

### Real-Life Analogy

Think of a function like ordering food in a restaurant.

```text
Function = Restaurant Order Form
Parameters = Empty food slots
Arguments = Actual food items you order
```

Example:

```python
def order(food, drink):
    print(food, drink)

order("Burger", "Coke")
```

Here:

* `food`, `drink` → Parameters
* `"Burger"`, `"Coke"` → Arguments

---

## Types of Arguments in Python

Python allows **4 types of arguments**:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable Length Arguments

---

# 1) Positional Arguments

## Definition

These are arguments passed to a function **in the correct order (position)**.

The position matters.

### Syntax

```python
def sub(a, b):
    print(a - b)

sub(100, 200)
sub(200, 100)
```

### Output

```text
-100
100
```

## Explanation

### First Function Call

```python
sub(100, 200)
```

Mapping:

```text
a = 100
b = 200
```

Calculation:

```text
100 - 200 = -100
```

---

### Second Function Call

```python
sub(200, 100)
```

Mapping:

```text
a = 200
b = 100
```

Calculation:

```text
200 - 100 = 100
```

### Important Rules

1. **Order must match**

   * Arguments should be passed in the correct position.

2. **Changing position changes output**

Example:

```python
sub(10, 5)   # Output: 5
sub(5, 10)   # Output: -5
```

3. **Number of arguments must match**

Wrong Example:

```python
def add(a, b):
    print(a + b)

add(10)
```

### Error

```text
TypeError: missing 1 required positional argument
```

---

### Real-Life Analogy

Imagine a train reservation form:

```text
Passenger Name → First box
Age → Second box
```

Correct:

```text
("Narendar", 23)
```

Wrong order:

```text
(23, "Narendar")
```

This creates confusion because the position matters.

---

# 2) Keyword Arguments

## Definition

We can pass argument values using **parameter names (keywords)**.

In keyword arguments, **order does not matter**.

### Syntax

```python
def wish(name, msg):
    print("Hello", name, msg)

wish(name="Durga", msg="Good Morning")
wish(msg="Good Morning", name="Durga")
```

### Output

```text
Hello Durga Good Morning
Hello Durga Good Morning
```

## Explanation

### First Call

```python
wish(name="Durga", msg="Good Morning")
```

Mapping:

```text
name = "Durga"
msg = "Good Morning"
```

Output:

```text
Hello Durga Good Morning
```

---

### Second Call

```python
wish(msg="Good Morning", name="Durga")
```

Even though the order changed:

```text
msg first
name second
```

Python understands using keyword names.

So output remains the same.

---

## Why Use Keyword Arguments?

Keyword arguments improve:

* Readability
* Flexibility
* Code clarity

Example:

Without keyword arguments:

```python
student("Narendar", 81.8, "CSE")
```

Hard to understand what each value means.

With keyword arguments:

```python
student(
    name="Narendar",
    percentage=81.8,
    branch="CSE"
)
```

Much clearer.

---

## Positional vs Keyword Arguments

| Feature                 | Positional Arguments | Keyword Arguments |
| ----------------------- | -------------------- | ----------------- |
| Order matters           | Yes                  | No                |
| Parameter name required | No                   | Yes               |
| Readability             | Less                 | More              |
| Flexible                | No                   | Yes               |

---

## Text Diagram

```text
Positional Arguments

sub(100, 200)

a = 100
b = 200

Position matters
```

```text
Keyword Arguments

wish(name="Durga", msg="Good Morning")

name = Durga
msg = Good Morning

Position does not matter
```

---

# Common Interview Question

### Q1: What happens if positional arguments are passed in the wrong order?

Answer:
The output changes because values are assigned based on position.

Example:

```python
def div(a, b):
    print(a / b)

div(10, 2)   # Output: 5.0
div(2, 10)   # Output: 0.2
```

---

### Q2: Can we change the order in keyword arguments?

Answer:

Yes, because values are assigned using parameter names.

Example:

```python
wish(msg="Hi", name="Ravi")
```

Still works correctly.

---

# Key Takeaways

* **Arguments** are values passed to a function.
* **Parameters/Formal Arguments** are variables in function definition.
* **Actual Arguments** are real values passed during function call.
* Python supports **4 types of arguments**:

  1. Positional Arguments
  2. Keyword Arguments
  3. Default Arguments
  4. Variable Length Arguments
* In **Positional Arguments**, order matters.
* In **Keyword Arguments**, order does not matter.
* The **number of arguments should match** the number of parameters unless special techniques are used.
* Keyword arguments make code **more readable and understandable** for developers and students.

