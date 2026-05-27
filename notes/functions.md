
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
("rohit", 43)
```

Wrong order:

```text
(43, "rohit")
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
student("rohit", 81.8, "CSE")
```

Hard to understand what each value means.

With keyword arguments:

```python
student(
    name="rohit",
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

# Types of Arguments in Python (Continued)

Previously, we learned:

1. Positional Arguments
2. Keyword Arguments

Now let us learn the remaining two types:

3. Default Arguments
4. Variable Length Arguments

---

# 3) Default Arguments

## Definition

A **Default Argument** is an argument that already has a value assigned in the function definition.

If the user does not pass a value, Python uses the **default value automatically**.

### Syntax

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ravi")
```

### Output

```text
Hello Student
Hello Ravi
```

---

## Explanation

### Function Definition

```python
def greet(name="Student"):
```

Here:

```text
name = "Student"
```

is the **default value**.

---

### First Function Call

```python
greet()
```

No argument is passed.

So Python automatically uses:

```text
name = "Student"
```

Output:

```text
Hello Student
```

---

### Second Function Call

```python
greet("Ravi")
```

Now Python replaces the default value.

Mapping:

```text
name = "Ravi"
```

Output:

```text
Hello Ravi
```

---

## Example 2

```python
def power(base, exponent=2):
    print(base ** exponent)

power(5)
power(5, 3)
```

### Output

```text
25
125
```

### Explanation

### First Call

```python
power(5)
```

Since exponent is not passed:

```text
exponent = 2
```

Calculation:

```text
5² = 25
```

---

### Second Call

```python
power(5, 3)
```

Now:

```text
base = 5
exponent = 3
```

Calculation:

```text
5³ = 125
```

---

## Important Rules of Default Arguments

### 1. Default value is used if no value is passed

Example:

```python
def city(name="Hyderabad"):
    print(name)

city()
```

Output:

```text
Hyderabad
```

---

### 2. Passed value overrides default value

Example:

```python
city("Chennai")
```

Output:

```text
Chennai
```

---

### 3. Default arguments should come after normal arguments

Correct:

```python
def student(name, course="Python"):
    print(name, course)
```

Wrong:

```python
def student(course="Python", name):
    print(name, course)
```

This gives an error.

---

## Real-Life Analogy

Think of a food order.

```text
Default Drink = Water
```

If customer does not mention a drink:

```text
Food → Biryani
Drink → Water
```

If customer selects:

```text
Food → Biryani
Drink → Coke
```

Then Coke replaces Water.

Same concept in Python.

---

## Text Diagram

```text
Default Argument

def greet(name="Student")

      No Value Passed
              │
              ▼
     Uses Default Value

      Value Passed
              │
              ▼
     Replaces Default Value
```

---

# 4) Variable Length Arguments

## Definition

Sometimes we do not know **how many arguments** will be passed.

In such cases, Python uses **Variable Length Arguments**.

We use:

```text
*args
```

to accept multiple values.

---

## Why Variable Length Arguments?

Normally:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This accepts only **2 arguments**.

Problem:

```python
add(10, 20, 30)
```

Error occurs.

To solve this, Python provides:

```text
*args
```

---

## Syntax

```python
def sum_numbers(*numbers):
    print(numbers)

sum_numbers(10, 20)
sum_numbers(10, 20, 30, 40)
```

### Output

```text
(10, 20)
(10, 20, 30, 40)
```

---

## Explanation

### Function Definition

```python
def sum_numbers(*numbers):
```

`*numbers` collects all values into a **tuple**.

---

### First Function Call

```python
sum_numbers(10, 20)
```

Python stores:

```text
numbers = (10, 20)
```

---

### Second Function Call

```python
sum_numbers(10, 20, 30, 40)
```

Python stores:

```text
numbers = (10, 20, 30, 40)
```

---

## Example 2: Addition Program

```python
def add(*nums):
    total = 0

    for i in nums:
        total = total + i

    print(total)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
```

### Output

```text
30
60
100
```

---

## Step-by-Step Explanation

### First Call

```python
add(10, 20)
```

Stored as:

```text
nums = (10, 20)
```

Calculation:

```text
10 + 20 = 30
```

---

### Second Call

```python
add(10, 20, 30)
```

Stored as:

```text
nums = (10, 20, 30)
```

Calculation:

```text
10 + 20 + 30 = 60
```

---

### Third Call

```python
add(10, 20, 30, 40)
```

Stored as:

```text
nums = (10, 20, 30, 40)
```

Calculation:

```text
10 + 20 + 30 + 40 = 100
```

---

## Important Rules of Variable Length Arguments

### 1. We use `*` symbol

Example:

```python
def demo(*x):
    print(x)
```

---

### 2. It stores values as a tuple

Example:

```python
demo(1, 2, 3)
```

Stored as:

```text
x = (1, 2, 3)
```

---

### 3. It accepts any number of arguments

Example:

```python
demo()
demo(10)
demo(10, 20)
demo(10, 20, 30)
```

All are valid.

---

## Real-Life Analogy

Think of a school attendance register.

Teacher does not know how many students will come today.

```text
Student1
Student2
Student3
Student4
...
```

Any number of students can attend.

Similarly:

```text
*args accepts any number of values
```

---

## Text Diagram

```text
Variable Length Argument

add(10,20,30,40)

            │
            ▼

      *nums collects all

    nums = (10,20,30,40)
```

---

# Comparison of All Argument Types

| Argument Type             | Order Matters | Number of Arguments Fixed | Uses Parameter Name |
| ------------------------- | ------------: | ------------------------: | ------------------: |
| Positional Arguments      |           Yes |                       Yes |                  No |
| Keyword Arguments         |            No |                       Yes |                 Yes |
| Default Arguments         |            No |                     Fixed |            Optional |
| Variable Length Arguments |            No |                        No |                  No |

---

# Common Interview Questions

### Q1: What is a Default Argument?

**Answer:**
A default argument is an argument that already has a predefined value in the function definition.

---

### Q2: What happens if we do not pass a value to a default argument?

**Answer:**
Python automatically uses the default value.

---

### Q3: What is a Variable Length Argument?

**Answer:**
A variable length argument allows a function to accept multiple arguments using `*args`.

---

### Q4: In which data type are variable length arguments stored?

**Answer:**
They are stored in a **tuple**.

---

# Key Takeaways

* Python supports **4 types of arguments**:

  1. Positional Arguments
  2. Keyword Arguments
  3. Default Arguments
  4. Variable Length Arguments

* **Default Arguments**

  * Have predefined values
  * Used when no value is passed
  * Passed value overrides default value

* **Variable Length Arguments**

  * Use `*args`
  * Accept unlimited arguments
  * Store values in a tuple

* Use **Default Arguments** when common values repeat.

* Use **Variable Length Arguments** when the number of inputs is unknown.


# Types of Variables in Python

## What are Variables?

A **variable** is a name used to store data in memory.

Example:

```python
a = 10
name = "Narendar"
```

Here:

* `a` stores the value `10`
* `name` stores the value `"Narendar"`

---

## Types of Variables in Python

Python supports **2 types of variables**:

1. Global Variables
2. Local Variables

---

# 1) Global Variables

## Definition

Variables declared **outside a function** are called **Global Variables**.

These variables can be accessed from **any function in the program (module)**.

### Syntax

```python
a = 10   # Global Variable

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()
```

### Output

```text
10
10
```

---

## Explanation

### Step 1: Variable Creation

```python
a = 10
```

Since `a` is declared **outside** all functions, it becomes a **global variable**.

---

### Step 2: First Function

```python
def f1():
    print(a)
```

Python searches for `a`.

Since `a` is not inside `f1()`, Python checks outside the function and finds:

```python
a = 10
```

So output is:

```text
10
```

---

### Step 3: Second Function

```python
def f2():
    print(a)
```

Again, Python finds the same global variable.

Output:

```text
10
```

---

## Important Points About Global Variables

### 1. Declared Outside Functions

Global variables are always declared **outside** the function.

Example:

```python
x = 100
```

---

### 2. Accessible Everywhere

They can be used inside multiple functions.

Example:

```python
college = "GITAM"

def student1():
    print(college)

def student2():
    print(college)

student1()
student2()
```

### Output

```text
GITAM
GITAM
```

---

## Real-Life Analogy

Think of a **Wi-Fi password in a college**.

```text
Wi-Fi Password = Global Variable

Anyone in the college can use it
(All departments can access it)
```

Similarly:

```text
Global Variable

Accessible by all functions
```

---

## Text Diagram

```text
Global Variable

a = 10

        ┌───────────┐
        │  f1()     │ ───► Can Access
        └───────────┘

        ┌───────────┐
        │  f2()     │ ───► Can Access
        └───────────┘
```

---

# 2) Local Variables

## Definition

Variables declared **inside a function** are called **Local Variables**.

These variables are available **only inside that function**.

We **cannot access them outside the function**.

### Syntax

```python
def f1():
    a = 10
    print(a)   # Valid

def f2():
    print(a)   # Invalid

f1()
f2()
```

### Output

```text
10
NameError: name 'a' is not defined
```

---

## Explanation

### Step 1: Local Variable Creation

Inside `f1()`:

```python
a = 10
```

Since `a` is created **inside the function**, it becomes a **local variable**.

---

### Step 2: Access Inside Same Function

```python
print(a)
```

Inside `f1()`, `a` exists.

So output:

```text
10
```

---

### Step 3: Access From Another Function

```python
def f2():
    print(a)
```

Here Python searches for `a`.

But:

* `a` is not inside `f2()`
* `a` is not global

So Python throws an error:

```text
NameError: name 'a' is not defined
```

---

## Important Points About Local Variables

### 1. Created Inside Functions

Example:

```python
def demo():
    x = 50
```

Here `x` is local.

---

### 2. Accessible Only in Same Function

Correct Example:

```python
def show():
    msg = "Hello"
    print(msg)
```

Wrong Example:

```python
def show():
    msg = "Hello"

print(msg)
```

### Error

```text
NameError: name 'msg' is not defined
```

---

## Real-Life Analogy

Think of a **teacher's classroom marker**.

```text
Local Variable = Classroom Marker

Only that classroom teacher can use it.
Other classrooms cannot access it.
```

Similarly:

```text
Local Variable

Accessible only inside that function
```

---

## Text Diagram

```text
Local Variable

def f1():
    a = 10

        ┌───────────┐
        │  f1()     │ ───► Can Access
        └───────────┘

        ┌───────────┐
        │  f2()     │ ───► Cannot Access
        └───────────┘
```

---

# Global Variable vs Local Variable

| Feature                       | Global Variable        | Local Variable          |
| ----------------------------- | ---------------------- | ----------------------- |
| Declaration Place             | Outside function       | Inside function         |
| Scope                         | Entire program/module  | Only inside function    |
| Accessible in other functions | Yes                    | No                      |
| Lifetime                      | Till program execution | Till function execution |

---

## Example Comparing Both

```python
x = 100   # Global Variable

def test():
    y = 50    # Local Variable
    print(x)
    print(y)

test()

print(x)
print(y)
```

### Output

```text
100
50
100
NameError: name 'y' is not defined
```

### Why Error?

Because:

```text
x → Global → Accessible everywhere

y → Local → Accessible only inside test()
```

---

# Common Interview Questions

### Q1: What is a Global Variable?

**Answer:**
A variable declared outside the function and accessible throughout the program is called a **Global Variable**.

---

### Q2: What is a Local Variable?

**Answer:**
A variable declared inside a function and accessible only within that function is called a **Local Variable**.

---

### Q3: Can a local variable be accessed outside a function?

**Answer:**
No. It will give a **NameError**.

---

### Q4: Which variable is accessible to all functions?

**Answer:**
**Global Variable**

---

# Key Takeaways

* Python supports **2 types of variables**:

  1. Global Variables
  2. Local Variables

* **Global Variables**

  * Declared outside functions
  * Accessible in all functions
  * Available throughout the program

* **Local Variables**

  * Declared inside functions
  * Accessible only within the same function
  * Cannot be accessed outside

* Trying to access a local variable outside its function gives:

```text
NameError: name 'variable_name' is not defined
```

* Use **Global Variables** when multiple functions need the same data.
* Use **Local Variables** when data is needed only inside one function.


