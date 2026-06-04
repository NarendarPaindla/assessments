# Type Hints in Python

# What are Type Hints?

Type Hints are used to specify the expected data type of variables, function parameters, and return values.

They improve:

* Code readability
* Code maintenance
* IDE support (VS Code, PyCharm)
* Static type checking

Type hints do **not enforce types at runtime**. They are only hints for developers and tools.

---

# Why Type Hints?

Without type hints:

```python
def add(a, b):
    return a + b
```

We don't know:

* Is `a` an integer?
* Is `b` a float?
* Is it expecting strings?

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Now it is clear that:

```text
a → int
b → int
return → int
```

---

# Function Parameter Type Hints

## Syntax

```python
def function_name(parameter: datatype):
    pass
```

---

## Example

```python
def greet(name: str):
    print("Hello", name)

greet("Rahul")
```

---

# Return Type Hints

## Syntax

```python
def function_name() -> datatype:
    pass
```

---

## Example

```python
def square(n: int) -> int:
    return n * n

print(square(5))
```

### Output

```text
25
```

---

# Multiple Parameters

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
```

### Output

```text
30
```

---

# Different Data Types

## Integer

```python
age: int = 25
```

---

## Float

```python
salary: float = 50000.50
```

---

## String

```python
name: str = "Rahul"
```

---

## Boolean

```python
is_active: bool = True
```

---

# Variable Type Hints

Type hints can also be applied to variables.

```python
name: str = "Rahul"
age: int = 21
marks: float = 85.5

print(name)
print(age)
print(marks)
```

---

# List Type Hints

Using the `typing` module:

```python
from typing import List

numbers: List[int] = [10, 20, 30]
```

---

## Example

```python
from typing import List

def total(nums: List[int]) -> int:
    return sum(nums)

print(total([10, 20, 30]))
```

### Output

```text
60
```

---

# Tuple Type Hints

```python
from typing import Tuple

student: Tuple[str, int] = ("Rahul", 101)
```

---

## Example

```python
from typing import Tuple

def get_student() -> Tuple[str, int]:
    return ("Rahul", 101)

print(get_student())
```

### Output

```text
('Rahul', 101)
```

---

# Dictionary Type Hints

```python
from typing import Dict

student: Dict[str, int] = {
    "Math": 90,
    "Science": 95
}
```

---

## Example

```python
from typing import Dict

def get_marks() -> Dict[str, int]:
    return {
        "Math": 90,
        "Science": 95
    }

print(get_marks())
```

---

# Set Type Hints

```python
from typing import Set

numbers: Set[int] = {10, 20, 30}
```

---

# Optional Type

Sometimes a value may be present or may be `None`.

```python
from typing import Optional

name: Optional[str] = None
```

Equivalent to:

```python
str | None
```

---

## Example

```python
from typing import Optional

def get_name(flag: bool) -> Optional[str]:

    if flag:
        return "Rahul"

    return None
```

---

# Union Type

A variable can hold multiple types.

```python
from typing import Union

data: Union[int, str]
```

---

## Example

```python
from typing import Union

def process(value: Union[int, str]):

    print(value)

process(10)
process("Python")
```

---

# Modern Python (3.10+)

Instead of:

```python
Union[int, str]
```

Use:

```python
int | str
```

Example:

```python
def process(value: int | str):
    print(value)
```

---

# Any Type

If a variable can accept any type:

```python
from typing import Any

value: Any
```

---

## Example

```python
from typing import Any

def display(data: Any):
    print(data)

display(10)
display("Python")
display([1, 2, 3])
```

---

# Callable Type

Represents a function.

```python
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

operation: Callable[[int, int], int] = add
```

---

# Type Hints with Lambda

```python
square: callable = lambda x: x * x

print(square(5))
```

### Output

```text
25
```

---

# Type Hints in Classes

```python
class Student:

    def __init__(self,
                 name: str,
                 rollno: int):

        self.name = name
        self.rollno = rollno
```

---

# Example

```python
class Student:

    def __init__(
            self,
            name: str,
            marks: float):

        self.name = name
        self.marks = marks

    def display(self) -> None:

        print(self.name)
        print(self.marks)


s = Student("Rahul", 85.5)

s.display()
```

---

# Type Hints with Generators

```python
from typing import Generator

def countdown(n: int) -> Generator[int, None, None]:

    while n > 0:
        yield n
        n -= 1
```

---

# Type Hints with Decorators

```python
from typing import Callable

def decorator(func: Callable) -> Callable:

    def inner():
        print("Before")

        func()

        print("After")

    return inner
```

---

# Type Checking Using mypy

Install:

```bash
pip install mypy
```

Check file:

```bash
mypy app.py
```

---

## Example

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))
```

mypy reports:

```text
Argument 1 has incompatible type "str"
Argument 2 has incompatible type "str"
```

---

# Common Types in typing Module

| Type      | Purpose          |
| --------- | ---------------- |
| List      | List Collection  |
| Tuple     | Tuple Collection |
| Dict      | Dictionary       |
| Set       | Set Collection   |
| Union     | Multiple Types   |
| Optional  | Value or None    |
| Any       | Any Type         |
| Callable  | Functions        |
| Generator | Generators       |
| Iterator  | Iterators        |

---

# Real-Time Example

Without Type Hints:

```python
def calculate(a, b):
    return a + b
```

Difficult to understand.

---

With Type Hints:

```python
def calculate(
        a: float,
        b: float) -> float:

    return a + b
```

Now developers instantly know:

```text
Input → float, float
Output → float
```

---

# Advantages of Type Hints

1. Better Readability
2. Better IDE Suggestions
3. Easier Debugging
4. Improved Code Maintenance
5. Static Type Checking
6. Better Team Collaboration
7. Self-Documenting Code

---

# Key Takeaways

* Type hints specify expected data types.
* They improve readability and maintainability.
* Use `:` for parameter/variable types.
* Use `->` for return types.
* Type hints do not enforce types at runtime.
* The `typing` module provides advanced type support.
* Common types include `List`, `Tuple`, `Dict`, `Set`, `Union`, and `Optional`.
* Tools like `mypy` can validate type hints.
* Type hints are widely used in professional Python projects.
