
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

===========================================================================================

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

===========================================================================================

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

=============================================================================================

# `**kwargs` in Python (Keyword Variable Length Arguments)

## Definition

`**kwargs` is used when we do not know **how many keyword arguments** will be passed to a function.

It allows a function to accept **multiple keyword arguments dynamically**.

`kwargs` stands for:

```text
Keyword Arguments
```

The `**` symbol is mandatory.

---

## Why `**kwargs`?

Normally:

```python
def student(name, course):
    print(name, course)

student("Rahul", "Python")
```

This function accepts only **fixed arguments**.

Problem:

```python
student(name="Rahul", course="Python", city="Hyderabad")
```

This gives an error because extra arguments are not allowed.

To solve this problem, Python provides:

```text
**kwargs
```

---

## Syntax

```python
def details(**data):
    print(data)

details(name="Rahul", city="Delhi")
```

### Output

```text
{'name': 'Rahul', 'city': 'Delhi'}
```

---

## Explanation

### Function Definition

```python
def details(**data):
```

Here:

```text
**data
```

collects all keyword arguments.

Python stores them as a **dictionary**.

---

### Function Call

```python
details(name="Rahul", city="Delhi")
```

Python stores:

```text
data = {
    'name': 'Rahul',
    'city': 'Delhi'
}
```

Output:

```text
{'name': 'Rahul', 'city': 'Delhi'}
```

---

# Example 1: Student Details

```python
def student_info(**student):
    print(student)

student_info(
    name="Aman",
    course="Python",
    city="Mumbai"
)
```

### Output

```text
{
 'name': 'Aman',
 'course': 'Python',
 'city': 'Mumbai'
}
```

---

## Step-by-Step Explanation

Python stores values like this:

```text
student = {
   'name': 'Aman',
   'course': 'Python',
   'city': 'Mumbai'
}
```

Since it is a dictionary:

* Keys → parameter names
* Values → actual values

---

# Example 2: Printing Keys and Values

```python
def employee_details(**emp):

    for key, value in emp.items():
        print(key, ":", value)

employee_details(
    name="Suresh",
    department="IT",
    salary=50000
)
```

### Output

```text
name : Suresh
department : IT
salary : 50000
```

---

## Explanation

### Stored as Dictionary

```text
emp = {
   'name': 'Suresh',
   'department': 'IT',
   'salary': 50000
}
```

### Loop Working

```python
for key, value in emp.items():
```

This accesses:

```text
Key → Value
```

Example:

```text
name → Suresh
department → IT
salary → 50000
```

---

# Example 3: Passing Any Number of Keyword Arguments

```python
def profile(**info):
    print(info)

profile()

profile(name="Kiran")

profile(
    name="Priya",
    city="Chennai",
    profession="Teacher"
)
```

### Output

```text
{}
{'name': 'Kiran'}
{
 'name': 'Priya',
 'city': 'Chennai',
 'profession': 'Teacher'
}
```

---

## Important Rules of `**kwargs`

### 1. Uses Double Asterisk `**`

Correct:

```python
def demo(**x):
    print(x)
```

Wrong:

```python
def demo(*x):
    print(x)
```

Because `*x` is for positional variable arguments.

---

### 2. Stores Data as Dictionary

Example:

```python
def show(**data):
    print(type(data))

show(a=10, b=20)
```

### Output

```text
<class 'dict'>
```

So:

```text
**kwargs → Dictionary
```

---

### 3. Accepts Unlimited Keyword Arguments

Example:

```python
def demo(**x):
    print(x)

demo()
demo(a=10)
demo(a=10, b=20)
demo(a=10, b=20, c=30)
```

All are valid.

---

### 4. Keys Must Be Unique

Wrong Example:

```python
demo(name="Rahul", name="Ravi")
```

This gives an error because dictionary keys cannot repeat.

---

# Difference Between `*args` and `**kwargs`

| Feature           | `*args`                   | `**kwargs`                        |
| ----------------- | ------------------------- | --------------------------------- |
| Full Form         | Variable Length Arguments | Keyword Variable Length Arguments |
| Stores Data As    | Tuple                     | Dictionary                        |
| Type of Arguments | Positional                | Keyword                           |
| Symbol Used       | `*`                       | `**`                              |

---

## Example Comparing Both

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(
    10,
    20,
    30,
    name="Ravi",
    city="Hyderabad"
)
```

### Output

```text
(10, 20, 30)

{
 'name': 'Ravi',
 'city': 'Hyderabad'
}
```

### Explanation

Python stores:

```text
args = (10, 20, 30)
```

Tuple because positional arguments.

And:

```text
kwargs = {
   'name': 'Ravi',
   'city': 'Hyderabad'
}
```

Dictionary because keyword arguments.

---

## Real-Life Analogy

Imagine a **job application form**.

Some fields are fixed:

```text
Name
Age
Department
```

But sometimes extra details may come:

```text
Skills
Experience
City
Salary Expectation
```

Since we don't know what extra fields users provide:

```text
**kwargs handles dynamic keyword data
```

---

## Text Diagram

```text
Function Call

employee(
   name="Ravi",
   salary=50000,
   city="Delhi"
)

          │
          ▼

     **kwargs collects

{
 'name': 'Ravi',
 'salary': 50000,
 'city': 'Delhi'
}
```

---

# Common Interview Questions

### Q1: What is `**kwargs`?

**Answer:**
`**kwargs` allows a function to accept any number of keyword arguments.

---

### Q2: In which datatype are `**kwargs` stored?

**Answer:**
They are stored as a **dictionary**.

---

### Q3: What is the difference between `*args` and `**kwargs`?

**Answer:**

```text
*args   → Tuple → Positional arguments

**kwargs → Dictionary → Keyword arguments
```

---

### Q4: Can we use `*args` and `**kwargs` together?

**Answer:**
Yes.

Example:

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

============================================================================

# Lambda Functions in Python

## Definition

A **Lambda Function** is a small anonymous function in Python.

It is a function **without a name** and is created using the `lambda` keyword.

In simple words:

```text id="qdbx9z"
A lambda function is a short way
to write a function in one line.
```

---

## Why Lambda Functions?

Normally, we create functions using `def`.

Example:

```python id="mo2xgj"
def square(n):
    return n * n

print(square(5))
```

### Output

```text id="p5ffkg"
25
```

But for small operations, writing a complete function becomes lengthy.

Python provides:

```text id="o9y2n0"
lambda
```

to write short functions in one line.

---

# Syntax of Lambda Function

```python id="jcz1vr"
lambda arguments : expression
```

### Components

| Part         | Meaning                           |
| ------------ | --------------------------------- |
| `lambda`     | Keyword to create lambda function |
| `arguments`  | Input values                      |
| `expression` | Logic or operation                |

---

## Basic Example

```python id="h5g9m3"
square = lambda x: x * x

print(square(5))
```

### Output

```text id="l6l8mq"
25
```

---

## Step-by-Step Explanation

### Lambda Creation

```python id="d28d56"
lambda x: x * x
```

Here:

```text id="73jqha"
x → Input

x * x → Expression
```

Equivalent Normal Function:

```python id="5r0gb8"
def square(x):
    return x * x
```

Both do the same work.

---

# Example 1: Addition

### Using Normal Function

```python id="zj0n6h"
def add(a, b):
    return a + b

print(add(10, 20))
```

### Using Lambda Function

```python id="a0w5gm"
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```text id="sivz9j"
30
```

---

## Explanation

```python id="w77oym"
lambda a, b: a + b
```

Meaning:

```text id="8g3n1v"
Take a and b

Return a + b
```

---

# Example 2: Even or Odd

```python id="0mjlwm"
check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(8))
print(check(7))
```

### Output

```text id="87gxru"
Even
Odd
```

---

## Explanation

Condition:

```python id="jvkk2v"
n % 2 == 0
```

If true:

```text id="vjlwmh"
Even
```

Else:

```text id="n7vmdn"
Odd
```

---

# Example 3: Largest Number

```python id="grb0px"
largest = lambda a, b: a if a > b else b

print(largest(50, 100))
```

### Output

```text id="txhmn9"
100
```

---

## Explanation

Condition:

```python id="3b9vij"
a > b
```

If true:

```text id="mjlwm6"
return a
```

Otherwise:

```text id="3tz9r4"
return b
```

---

# Multiple Arguments in Lambda

Lambda can take multiple arguments.

Example:

```python id="m6gnwz"
multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))
```

### Output

```text id="1c8d2w"
24
```

Calculation:

```text id="azqk4g"
2 × 3 × 4 = 24
```

---

# No Arguments in Lambda

Lambda can also work without arguments.

Example:

```python id="9u4e3p"
greet = lambda: "Welcome to Python"

print(greet())
```

### Output

```text id="vjlwm0"
Welcome to Python
```

---

# Lambda with `map()`

## Definition

`map()` applies a function to every item in a sequence.

Example:

```python id="1v08a2"
numbers = [1, 2, 3, 4]

square = list(map(lambda x: x * x, numbers))

print(square)
```

### Output

```text id="9ff0lk"
[1, 4, 9, 16]
```

---

## Explanation

Lambda runs on every element:

```text id="vovjlwm"
1 → 1×1 = 1
2 → 2×2 = 4
3 → 3×3 = 9
4 → 4×4 = 16
```

---

# Lambda with `filter()`

## Definition

`filter()` selects elements based on a condition.

Example:

```python id="18e2u9"
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

### Output

```text id="lbjlwm"
[2, 4, 6]
```

---

## Explanation

Condition:

```python id="rxtqzc"
x % 2 == 0
```

Check each number:

```text id="7a1h0x"
1 → False

2 → True

3 → False

4 → True

5 → False

6 → True
```

Selected values:

```text id="jlwm9m"
[2, 4, 6]
```

---

# Lambda with `sorted()`

Example:

```python id="fjlwm4"
students = [
    ("Ram", 70),
    ("Amit", 90),
    ("Kiran", 80)
]

result = sorted(students, key=lambda x: x[1])

print(result)
```

### Output

```text id="jlwmzb"
[
 ('Ram', 70),
 ('Kiran', 80),
 ('Amit', 90)
]
```

---

## Explanation

Lambda:

```python id="jlwmm0"
lambda x: x[1]
```

means:

```text id="jlwmg7"
Sort based on second value
(marks)
```

Sorted order:

```text id="jjlwm0"
70 → 80 → 90
```

---

# Important Rules of Lambda Functions

### 1. Lambda has no name

Example:

```python id="jlwm0y"
lambda x: x + 10
```

Anonymous function.

---

### 2. Lambda contains only one expression

Correct:

```python id="jlwmz1"
lambda x: x * x
```

Wrong:

```python id="jlwm4m"
lambda x:
    x = x + 1
    return x
```

Not allowed.

---

### 3. No `return` keyword

Wrong:

```python id="jlwmn8"
lambda x: return x * x
```

Correct:

```python id="wjgl0w"
lambda x: x * x
```

Lambda automatically returns the result.

---

### 4. Best for Small Functions

Good:

```python id="jlwmhy"
lambda x: x + 5
```

Not good for large logic.

---

# Lambda vs Normal Function

| Feature               | Normal Function | Lambda Function  |
| --------------------- | --------------- | ---------------- |
| Keyword Used          | `def`           | `lambda`         |
| Function Name         | Required        | Optional         |
| Number of Expressions | Multiple        | One              |
| Return Keyword        | Required        | Not Required     |
| Best For              | Large Logic     | Small Operations |

---

## Text Diagram

```text id="jlwmws"
Normal Function

def square(x):
    return x*x
```

```text id="jlwm2t"
Lambda Function

lambda x: x*x
```

Both do same work.

---

# Real-Life Analogy

Imagine a calculator.

For simple calculations:

```text id="0jlwmf"
2 + 3
5 × 5
```

You do not write steps.

You directly calculate.

Similarly:

```text id="tjlwm0"
Lambda = Quick One-Line Function
```

---

# Common Interview Questions

### Q1: What is a Lambda Function?

**Answer:**
A lambda function is an anonymous function written in one line using the `lambda` keyword.

---

### Q2: Why use Lambda Functions?

**Answer:**
Lambda functions are used for small and quick operations.

---

### Q3: Can lambda contain multiple statements?

**Answer:**
No. Lambda supports only one expression.

---

### Q4: Does lambda require `return` keyword?

**Answer:**
No. Lambda automatically returns the result.

---

### Q5: Where are lambda functions commonly used?

**Answer:**
They are commonly used with:

* `map()`
* `filter()`
* `sorted()`
* `reduce()`

---

# Key Takeaways

* Lambda is an **anonymous function**.
* Created using the `lambda` keyword.
* Used for **small one-line operations**.
* No function name is required.
* No `return` statement is needed.
* Lambda supports **only one expression**.

============================================================

# Higher-Order Functions in Python

## Definition

A **Higher-Order Function (HOF)** is a function that:

1. **Takes another function as an argument**, OR
2. **Returns a function as output**

In simple words:

```text id="z7d2mv"
A function that works with another function
is called a Higher-Order Function.
```

---

## Why Higher-Order Functions?

Normally, functions work with values.

Example:

```python id="vq24h1"
def add(a, b):
    return a + b

print(add(10, 20))
```

Here:

```text id="39m01n"
10 and 20 are values
```

But Python also allows:

```text id="4w4mq2"
Passing functions as arguments
```

This creates more reusable and flexible code.

---

# Condition for Higher-Order Function

A function becomes a **Higher-Order Function** if:

### 1. Function Accepts Another Function

OR

### 2. Function Returns Another Function

---

# Type 1: Function as an Argument

## Example 1

```python id="zjlwm1"
def square(x):
    return x * x

def cube(x):
    return x * x * x

def operation(fun, value):
    return fun(value)

print(operation(square, 5))
print(operation(cube, 5))
```

### Output

```text id="jlwm22"
25
125
```

---

## Step-by-Step Explanation

### Function Definitions

```python id="jlwm33"
def square(x):
```

Returns:

```text id="jlwm44"
x × x
```

---

```python id="jlwm55"
def cube(x):
```

Returns:

```text id="jlwm66"
x × x × x
```

---

### Higher-Order Function

```python id="jlwm77"
def operation(fun, value):
```

Here:

```text id="jlwm88"
fun → Function parameter
value → Normal value
```

---

### First Call

```python id="jlwm99"
operation(square, 5)
```

Python stores:

```text id="jlwm00"
fun = square
value = 5
```

Execution:

```text id="jlwm11"
square(5)

5 × 5 = 25
```

Output:

```text id="jlwm12"
25
```

---

### Second Call

```python id="jlwm13"
operation(cube, 5)
```

Python stores:

```text id="jlwm14"
fun = cube
value = 5
```

Execution:

```text id="jlwm15"
cube(5)

5 × 5 × 5 = 125
```

Output:

```text id="jlwm16"
125
```

---

# Example 2: Calculator Operation

```python id="jlwm17"
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 10, 20))
print(calculate(multiply, 10, 20))
```

### Output

```text id="jlwm18"
30
200
```

---

## Explanation

### First Call

```python id="jlwm19"
calculate(add, 10, 20)
```

Python performs:

```text id="jlwm20"
add(10, 20)

10 + 20 = 30
```

---

### Second Call

```python id="jlwm21"
calculate(multiply, 10, 20)
```

Python performs:

```text id="jlwm23"
multiply(10, 20)

10 × 20 = 200
```

---

# Type 2: Returning a Function

A Higher-Order Function can also **return another function**.

## Example

```python id="jlwm24"
def outer():

    def inner():
        return "Hello Python"

    return inner

result = outer()

print(result())
```

### Output

```text id="jlwm25"
Hello Python
```

---

## Explanation

### Outer Function Executes

```python id="jlwm26"
result = outer()
```

Python creates:

```text id="jlwm27"
inner()
```

and returns it.

---

### Calling Returned Function

```python id="jlwm28"
result()
```

Output:

```text id="jlwm29"
Hello Python
```

This is also a **Higher-Order Function** because:

```text id="jlwm30"
Function returned another function
```

---

# Built-in Higher-Order Functions in Python

Python provides several built-in Higher-Order Functions.

Common ones are:

1. `map()`
2. `filter()`
3. `sorted()`
4. `reduce()`

---

## Example: `map()`

```python id="jlwm31"
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x*x, numbers))

print(result)
```

### Output

```text id="jlwm32"
[1, 4, 9, 16]
```

Why HOF?

Because:

```text id="jlwm34"
map() accepts lambda function
as argument
```

---

## Example: `filter()`

```python id="jlwm35"
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

### Output

```text id="jlwm36"
[2, 4, 6]
```

Why HOF?

Because:

```text id="jlwm37"
filter() accepts function
as parameter
```

---

# Important Characteristics of Higher-Order Functions

### 1. Functions Are Treated as Objects

Python allows:

```text id="jlwm38"
Functions stored in variables
Functions passed as arguments
Functions returned from functions
```

---

### 2. Improves Code Reusability

Instead of writing separate logic:

```text id="jlwm39"
One Higher-Order Function
can work with multiple functions
```

---

### 3. Makes Code Flexible

Example:

```text id="jlwm40"
Same calculate() function

Works for:
Addition
Subtraction
Multiplication
Division
```

---

# Text Diagram

```text id="jlwm41"
Higher-Order Function

calculate(add, 10, 20)

        │
        ▼

Passes function

add(10,20)

        │
        ▼

Output = 30
```

---

# Real-Life Analogy

Imagine a **remote control**.

```text id="jlwm42"
Remote = Higher-Order Function

Buttons = Functions
```

Same remote can perform:

```text id="jlwm43"
TV ON
Volume UP
Channel Change
```

Similarly:

```text id="jlwm44"
Higher-Order Function works
with multiple functions
```

---

# Higher-Order Function vs Normal Function

| Feature                      | Normal Function | Higher-Order Function |
| ---------------------------- | --------------- | --------------------- |
| Accepts function as argument | No              | Yes                   |
| Returns function             | No              | Yes                   |
| Flexibility                  | Less            | More                  |
| Reusability                  | Limited         | High                  |

---

# Common Interview Questions

### Q1: What is a Higher-Order Function?

**Answer:**
A Higher-Order Function is a function that takes another function as input or returns a function as output.

---

### Q2: Give examples of Higher-Order Functions.

**Answer:**

* `map()`
* `filter()`
* `reduce()`
* `sorted()`

---

### Q3: Why are Higher-Order Functions used?

**Answer:**
They improve:

* Code reusability
* Flexibility
* Clean coding

---

### Q4: Is `map()` a Higher-Order Function?

**Answer:**
Yes, because it accepts another function as argument.

---

# Key Takeaways

* A **Higher-Order Function** works with other functions.
* It either:

  * Accepts a function as input
  * Returns a function as output
* Python treats functions like objects.
* Built-in Higher-Order Functions:

  * `map()`
  * `filter()`
  * `reduce()`
  * `sorted()`
* Higher-Order Functions improve:

  * Reusability
  * Flexibility
  * Cleaner code



