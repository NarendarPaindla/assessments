# Object-Oriented Programming (OOP) — definitions, real-life analogies, and beginner-friendly Python practicals

---

# Classes & Objects

**Definition:**

* **Class:** a blueprint or template that defines attributes (data) and methods (functions) for objects.
* **Object (instance):** a concrete item created from a class.

**Real-world analogy:**
Class = blueprint for a `Car`. Object = your specific `Car` (a red Honda Civic).

**Practical (Python):**

```python
# classes_objects.py
class Car:
    """Class: blueprint for cars."""
    def __init__(self, make, model, year):
        self.make = make        # attribute
        self.model = model
        self.year = year

    def description(self):     # method
        return f"{self.year} {self.make} {self.model}"

# create (instantiate) objects
car1 = Car("Honda", "Civic", 2020)
car2 = Car("Toyota", "Corolla", 2022)

print(car1.description())  # 2020 Honda Civic
print(car2.description())  # 2022 Toyota Corolla
```

**Mini exercise:** Create a `Student` class with attributes `name`, `roll_no`, `branch` and a method `greet()` that prints a welcome message.

---

# Attributes & Methods

**Definition:**

* **Instance attributes:** data tied to a specific object (`self.x`).
* **Class attributes:** shared across all instances.
* **Instance methods:** operate on instance data.
* **Class methods:** operate on the class (`@classmethod`).
* **Static methods:** utility methods with no implicit `self` or `cls` (`@staticmethod`).

**Practical:**

```python
# attributes_methods.py
class Circle:
    pi = 3.14159           # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):            # instance method
        return Circle.pi * self.radius * self.radius

    @classmethod
    def unit_circle(cls):     # class method
        return cls(1)

    @staticmethod
    def info():               # static method
        return "Area = pi * r^2"

c = Circle(3)
print(c.area())             # 28.27431
u = Circle.unit_circle()
print(u.radius)             # 1
print(Circle.info())        # Area = pi * r^2
```

**Mini exercise:** Add a class attribute `count` to track how many `Circle` objects have been created.

---

# Encapsulation

**Definition:** Hiding internal object state and providing controlled access through methods (getters/setters). In Python we use name mangling (single/double underscore) and properties.

**Real-life analogy:** A TV remote has internal circuits (hidden); you control it with buttons.

**Practical:**

```python
# encapsulation.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # "private" attribute (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        raise ValueError("Insufficient funds")

    # getter using property
    @property
    def balance(self):
        return self.__balance

acct = BankAccount("Anita", 1000)
acct.deposit(500)
print(acct.balance)  # 1500
# acct.__balance  # AttributeError: private attribute
```

**Mini exercise:** Add a `transfer_to(other_account, amount)` method that withdraws from one account and deposits to another safely.

---

# Inheritance (types)

**Definition:** A class can derive (inherit) attributes and methods from another, enabling reuse.

**Real-world analogy:** `Vehicle` → `Car` and `Truck`.

We’ll show: single, multiple, multilevel, hierarchical, hybrid (combo).

**Practicals:**

```python
# inheritance_examples.py

# 1) Single inheritance
class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):   # single
    def speak(self):
        return "woof"

# 2) Multiple inheritance
class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer):  # multiple
    pass

# 3) Multilevel inheritance (A -> B -> C)
class LivingThing:
    pass

class Plant(LivingThing):
    pass

class Flower(Plant):
    def name(self):
        return "rose"

# 4) Hierarchical inheritance (one parent, many children)
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

# 5) Hybrid inheritance (combination example)
class A:
    def a(self): return "A"

class B(A):
    def b(self): return "B"

class C(A):
    def c(self): return "C"

class D(B, C):  # D inherits from B and C which both inherit A -> hybrid
    pass
```

**Mini exercise:** Make `Car` inherit from `Vehicle`, add `ElectricCar` inheriting from `Car` and override `refuel()` to `recharge()` (multilevel + overriding).

---

# Polymorphism

**Definition:** Same interface, different implementations.

* **Method overriding:** child class provides its own method implementation.
* **Operator overloading:** define what operators like `+`, `==` do for your objects.

**Practical (overriding + operator overloading):**

```python
# polymorphism.py
class Animal:
    def sound(self):
        return "?"

class Cat(Animal):
    def sound(self):
        return "meow"

class Dog(Animal):
    def sound(self):
        return "woof"

# operator overloading
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):  # overload +
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Point(4, 6)
```

**Mini exercise:** Implement `__eq__` in `Point` so two points compare equal when coordinates match.

---

# Abstraction

**Definition:** Hiding details and showing only essential features. Implemented with abstract base classes (ABC) to enforce methods in subclasses.

**Practical:**

```python
# abstraction.py
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def compute_pay(self):
        pass

class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def compute_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def compute_pay(self):
        return self.hours * self.rate

s = SalariedEmployee(3000)
h = HourlyEmployee(100, 20)
print(s.compute_pay(), h.compute_pay())  # 3000 2000
```

**Mini exercise:** Add a `get_details()` abstract method and implement in both subclasses.

---

# Decorators & Iterators

**Definitions:**

* **Decorator:** a function that takes and returns a function — used to add behavior (e.g., logging, timing).
* **Iterator:** an object implementing `__iter__()` and `__next__()` to produce a sequence of values.

**Practical — decorator:**

```python
# decorators.py
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def compute(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(compute(1000000))
```

**Practical — custom iterator:**

```python
# iterator.py
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for x in ReverseIterator([1,2,3,4]):
    print(x)  # 4 3 2 1
```

**Mini exercise:** Write a `PrimeIterator(n)` that yields primes up to `n`.

---

# Generators & Context Managers

**Definitions:**

* **Generator:** function using `yield` to produce values lazily.
* **Context manager:** object used with `with` statement to set up/tear down resources (implement `__enter__`/`__exit__` or use `contextlib`).

**Practical — generator:**

```python
# generator.py
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)  # 0 1 1 2 3 5 8
```

**Practical — context manager (class and decorator):**

```python
# context_manager.py
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc, tb):
        self.f.close()
        # return False  # re-raise any exception if True/False as needed

with FileOpener("test.txt", "w") as f:
    f.write("Hello")

# using contextlib
from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()

with open_file("test2.txt", "w") as f:
    f.write("Hi again")
```

**Mini exercise:** Create a generator `natural_numbers()` that yields natural numbers indefinitely; show how to take first 10.

---
---

---

Which of those would help you next?
