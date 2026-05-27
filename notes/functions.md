
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
