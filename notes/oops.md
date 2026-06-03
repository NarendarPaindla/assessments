# Object-Oriented Programming (OOP) in Python

# What is a Class?

In Python, everything is treated as an object. To create objects, we need a blueprint or model. This blueprint is called a **Class**.

A class is used to represent:

* Properties (Attributes/Data)
* Actions (Behavior/Methods)

### Real-Time Example

Consider a **Student**.

**Properties (Attributes):**

```text
Name
Roll Number
Marks
Age
```

**Actions (Methods):**

```text
Study
Write Exam
Display Details
```

A class combines both attributes and methods.

---

# How to Define a Class?

We use the `class` keyword to define a class.

## Syntax

```python
class ClassName:
    """Documentation String"""

    # Variables

    # Methods
```

---

# Documentation String (Doc String)

A documentation string is used to describe the purpose of a class.

### Accessing Documentation String

#### Method 1

```python
print(ClassName.__doc__)
```

#### Method 2

```python
help(ClassName)
```

---

## Example

```python
class Student:
    """
    This class stores student information
    """

print(Student.__doc__)

help(Student)
```

---

# Components of a Class

A class can contain:

## Variables

Used to represent data.

### Types of Variables

1. Instance Variables (Object Level Variables)
2. Static Variables (Class Level Variables)
3. Local Variables (Method Level Variables)

---

## Methods

Used to represent operations.

### Types of Methods

1. Instance Methods
2. Class Methods
3. Static Methods

---

# Example Class

```python
class Student:

    """
    Student information class
    """

    def __init__(self):

        self.name = "Rahul"
        self.age = 20
        self.marks = 85

    def display(self):

        print("My Name is:", self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)
```

---

# What is an Object?

An object is the physical existence of a class.

A class is just a blueprint.

An object is the actual implementation of that blueprint.

### Example

Blueprint:

```text
House Plan
```

Actual House:

```text
Constructed House
```

Similarly,

```text
Class → Blueprint
Object → Real Entity
```

---

# Creating an Object

## Syntax

```python
referenceVariable = ClassName()
```

---

## Example

```python
s = Student()
```

Here:

```python
Student()
```

creates an object.

---

# What is a Reference Variable?

A reference variable is used to refer to an object.

Using a reference variable, we can access:

* Instance Variables
* Instance Methods

---

## Example

```python
s = Student()
```

Here:

```python
s
```

is the reference variable.

---

# Program: Create Student Class and Object

```python
class Student:

    def __init__(self, name, rollno, marks):

        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):

        print("My Name is:", self.name)
        print("My Roll Number is:", self.rollno)
        print("My Marks are:", self.marks)


s1 = Student("Rahul", 101, 85)

s1.display()
```

---

## Output

```text
My Name is: Rahul
My Roll Number is: 101
My Marks are: 85
```

---

# Self Variable

## What is self?

`self` is a default variable that always points to the current object.

It is similar to:

```java
this
```

keyword in Java.

---

## Uses of self

Using `self`, we can access:

* Instance Variables
* Instance Methods

---

## Important Rules

### Rule 1

Inside Constructor:

```python
def __init__(self):
```

`self` must be the first parameter.

---

### Rule 2

Inside Instance Methods:

```python
def display(self):
```

`self` must be the first parameter.

---

## Example

```python
class Student:

    def display(self):

        print("Instance Method")
```

---

# Constructor Concept

## What is a Constructor?

A constructor is a special method used to initialize object data.

---

## Constructor Name

In Python:

```python
__init__()
```

is the constructor.

---

## Characteristics of Constructor

### 1. Special Method

Constructor is a special method in Python.

---

### 2. Automatically Executed

Constructor executes automatically when an object is created.

---

### 3. Used for Initialization

Main purpose:

```text
Initialize Instance Variables
```

---

### 4. Executed Once Per Object

Every object creation triggers constructor execution once.

---

### 5. Can Take Arguments

Constructor can accept parameters.

---

### 6. Optional

If we do not define a constructor, Python automatically provides a default constructor.

---

# Constructor Example

```python
class Student:

    def __init__(self, name, rollno, marks):

        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):

        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Marks:", self.marks)


s1 = Student("Rahul", 101, 85)

s1.display()
```

---

## Execution Flow

### Step 1

Python sees:

```python
s1 = Student("Rahul",101,85)
```

---

### Step 2

Object gets created.

---

### Step 3

Constructor automatically executes.

```python
__init__()
```

---

### Step 4

Values assigned:

```python
self.name = "Rahul"
self.rollno = 101
self.marks = 85
```

---

### Step 5

Object becomes ready for use.

---

# Visual Representation

```text
                Student Class
                       |
                       |
             -------------------
             |                 |
             |                 |
            s1               s2
        (Object)         (Object)

       Rahul            Priya
        101              102
         85               90
```

---

# Class vs Object

| Class                          | Object            |
| ------------------------------ | ----------------- |
| Blueprint                      | Real Entity       |
| Logical Entity                 | Physical Entity   |
| Created Once                   | Can Create Many   |
| No Memory Until Object Created | Occupies Memory   |
| Defines Structure              | Holds Actual Data |

---

# Key Takeaways

* A class is a blueprint for creating objects.
* A class contains:

  * Variables (Data)
  * Methods (Behavior)
* Objects are instances of a class.
* Objects are created using:

```python
obj = ClassName()
```

* Reference variables point to objects.
* `self` always refers to the current object.
* `self` must be the first parameter of:

  * Constructors
  * Instance Methods
* Constructor in Python is:

```python
__init__()
```

* Constructor is automatically executed during object creation.
* Constructor is mainly used to initialize instance variables.
* One class can create multiple objects with different data.
