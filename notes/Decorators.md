# Decorators in Python

## What is a Decorator?

A **Decorator** is a function that takes another function as an argument, adds extra functionality to it, and returns a modified function.

### Definition

A decorator allows us to extend the behavior of an existing function **without modifying its original source code**.

---

## Basic Idea

```text
Original Function
        |
        v
    Decorator
        |
        v
Modified Function
(Extra Functionality Added)
```

---

## Real-Life Analogy

Imagine you buy a plain pizza.

```text
Pizza
```

Now you add:

```text
Extra Cheese
Olives
Sauces
```

The original pizza is still there, but its functionality (taste/features) has been enhanced.

Similarly:

```text
Function + Decorator = Enhanced Function
```

---

# Why Do We Need Decorators?

Suppose we already have a function:

```python
def greet(name):
    print("Hello", name, "Good Morning")
```

Output:

```text
Hello Rahul Good Morning
Hello Priya Good Morning
Hello Arjun Good Morning
```

Now assume a special rule:

```text
If name is "Arjun"
display a different message.
```

Instead of modifying the original function, we can use a decorator.

---

# Example 1: Basic Decorator

```python
def decor(func):

    def inner(name):

        if name == "Arjun":
            print("Hello Arjun Bad Morning")

        else:
            func(name)

    return inner


@decor
def greet(name):
    print("Hello", name, "Good Morning")


greet("Rahul")
greet("Priya")
greet("Arjun")
```

---

## Output

```text
Hello Rahul Good Morning
Hello Priya Good Morning
Hello Arjun Bad Morning
```

---

## How It Works

### Original Function

```python
greet()
```

---

### Decorator

```python
decor(greet)
```

---

### Python Internally Converts

```python
greet = decor(greet)
```

Now whenever:

```python
greet()
```

is called,

```python
inner()
```

executes first.

---

# Calling a Function With and Without Decorator

Sometimes we may want both versions.

---

## Program

```python
def decor(func):

    def inner(name):

        if name == "Arjun":
            print("Hello Arjun Bad Morning")

        else:
            func(name)

    return inner


def greet(name):
    print("Hello", name, "Good Morning")


decorated_function = decor(greet)

greet("Rahul")
greet("Arjun")

decorated_function("Rahul")
decorated_function("Arjun")
```

---

## Output

```text
Hello Rahul Good Morning
Hello Arjun Good Morning

Hello Rahul Good Morning
Hello Arjun Bad Morning
```

---

## Explanation

Without decorator:

```python
greet("Arjun")
```

Normal function executes.

With decorator:

```python
decorated_function("Arjun")
```

Decorator logic executes.

---

# Example 2: Smart Division Using Decorator

Problem:

```python
20 / 2  -> Works
20 / 0  -> Error
```

Decorator can prevent the error.

---

## Program

```python
def smart_division(func):

    def inner(a, b):

        print("We are dividing", a, "with", b)

        if b == 0:
            print("Oops... Cannot Divide")
            return

        return func(a, b)

    return inner


@smart_division
def division(a, b):
    return a / b


print(division(20, 2))
print(division(20, 0))
```

---

## Output

```text
We are dividing 20 with 2
10.0

We are dividing 20 with 0
Oops... Cannot Divide
None
```

---

## Without Decorator

```python
def division(a,b):
    return a/b

print(division(20,0))
```

Output:

```text
ZeroDivisionError: division by zero
```

---

## Benefit

Decorator adds safety checks without changing original function code.

---

# Example 3: Decoration Example

```python
def marriage_decorator(func):

    def inner():

        print("Hair Decoration")
        print("Face Decoration")
        print("Premium Makeup")

        func()

    return inner


def get_ready():
    print("Ready for the Function")


decorated_ready = marriage_decorator(get_ready)

decorated_ready()
```

---

## Output

```text
Hair Decoration
Face Decoration
Premium Makeup
Ready for the Function
```

---

## Execution Flow

```text
get_ready()
        |
Decorator Added
        |
Hair Decoration
Face Decoration
Premium Makeup
        |
Ready for the Function
```

---

# Decorator Chaining

We can apply multiple decorators to the same function.

This process is called:

```text
Decorator Chaining
```

---

## Syntax

```python
@decorator1
@decorator2
def function():
    pass
```

---

## Important Rule

Execution happens from:

```text
Inner Decorator
       ->
Outer Decorator
```

---

# Example

```python
def square_decorator(func):

    def inner():

        x = func()

        return x * x

    return inner


def double_decorator(func):

    def inner():

        x = func()

        return 2 * x

    return inner


@square_decorator
@double_decorator
def num():

    return 10


print(num())
```

---

## Understanding the Flow

### Step 1

```python
num()
```

returns:

```python
10
```

---

### Step 2

Inner decorator executes:

```python
2 * 10
```

Result:

```python
20
```

---

### Step 3

Outer decorator executes:

```python
20 * 20
```

Result:

```python
400
```

---

## Output

```text
400
```

---

# Decorator Chaining Diagram

```text
num()
  |
  v
double_decorator
  |
  v
20
  |
  v
square_decorator
  |
  v
400
```

---

# Advantages of Decorators

1. Code Reusability
2. Cleaner Code
3. Separation of Concerns
4. Easy Logging
5. Easy Authentication
6. Validation Handling
7. Performance Monitoring
8. Error Handling

---

# Common Real-World Uses

| Use Case       | Purpose                |
| -------------- | ---------------------- |
| Authentication | Check user login       |
| Authorization  | Check permissions      |
| Logging        | Record function calls  |
| Validation     | Validate inputs        |
| Error Handling | Handle exceptions      |
| Timing         | Measure execution time |
| Caching        | Improve performance    |

---

# Key Takeaways

* A decorator is a function that takes another function as input.
* Decorators add functionality without modifying the original function.
* `@decorator_name` syntax is used to apply decorators.
* Python internally converts:

```python
@decor
def func():
    pass
```

into:

```python
func = decor(func)
```

* Decorators are commonly used for:

  * Validation
  * Authentication
  * Logging
  * Exception Handling
  * Performance Monitoring
* Multiple decorators can be applied to the same function.
* When multiple decorators are used, the inner decorator executes first and then the outer decorator.
* Decorators help write clean, reusable, and maintainable code.
