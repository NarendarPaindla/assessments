# Python `typing` Module

# What is the typing Module?

The **typing** module provides support for **Type Hints** in Python.

It helps developers specify the expected types of:

* Variables
* Function Parameters
* Return Values
* Collections
* Classes
* Generators
* Decorators

The typing module was introduced in Python 3.5.

---

# Why Use typing Module?

Without type hints:

```python
def add(a, b):
    return a + b
```

We don't know:

```text
What is a?
What is b?
What is returned?
```

With typing:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Everything becomes clear.

---

# Importing typing Module

```python
from typing import *
```

Or import specific types:

```python
from typing import List, Tuple, Dict
```

---

# 1) List

Used to specify list element types.

## Syntax

```python
from typing import List

numbers: List[int]
```

---

## Example

```python
from typing import List

marks: List[int] = [90, 80, 70]

print(marks)
```

Output:

```text
[90, 80, 70]
```

---

# 2) Tuple

Used to specify tuple types.

## Syntax

```python
from typing import Tuple

student: Tuple[str, int]
```

---

## Example

```python
from typing import Tuple

student: Tuple[str, int] = ("Rahul", 101)

print(student)
```

Output:

```text
('Rahul', 101)
```

---

# 3) Dict

Used to specify dictionary key and value types.

## Syntax

```python
from typing import Dict

data: Dict[str, int]
```

---

## Example

```python
from typing import Dict

marks: Dict[str, int] = {
    "Math": 90,
    "Science": 95
}

print(marks)
```

Output:

```text
{'Math': 90, 'Science': 95}
```

---

# 4) Set

Used to specify set element types.

## Syntax

```python
from typing import Set

numbers: Set[int]
```

---

## Example

```python
from typing import Set

numbers: Set[int] = {10, 20, 30}

print(numbers)
```

---

# 5) FrozenSet

Represents immutable sets.

## Example

```python
from typing import FrozenSet

data: FrozenSet[int] = frozenset([1, 2, 3])

print(data)
```

---

# 6) Union

Allows multiple types.

## Syntax

```python
Union[type1, type2]
```

---

## Example

```python
from typing import Union

data: Union[int, str]

data = 100
data = "Python"
```

---

## Function Example

```python
from typing import Union

def display(value: Union[int, str]):
    print(value)

display(10)
display("Hello")
```

---

# 7) Optional

Represents a value or None.

## Syntax

```python
Optional[str]
```

Equivalent to:

```python
Union[str, None]
```

---

## Example

```python
from typing import Optional

name: Optional[str] = None

print(name)
```

---

# 8) Any

Accepts any data type.

## Example

```python
from typing import Any

data: Any

data = 100
data = "Python"
data = [1, 2, 3]
```

---

# 9) Callable

Used for functions.

## Syntax

```python
Callable[[arguments], return_type]
```

---

## Example

```python
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

operation: Callable[[int, int], int] = add

print(operation(10, 20))
```

Output:

```text
30
```

---

# 10) Generator

Used for generator functions.

## Example

```python
from typing import Generator

def countdown(n: int) -> Generator[int, None, None]:

    while n > 0:
        yield n
        n -= 1
```

---

# 11) Iterator

Represents objects that support iteration.

## Example

```python
from typing import Iterator

def numbers() -> Iterator[int]:

    yield 1
    yield 2
    yield 3
```

---

# 12) Iterable

Represents objects that can be iterated.

Examples:

```text
List
Tuple
Set
String
Dictionary
```

---

## Example

```python
from typing import Iterable

def display(items: Iterable[int]):

    for item in items:
        print(item)
```

---

# 13) Sequence

Represents ordered collections.

Examples:

```text
List
Tuple
String
```

---

## Example

```python
from typing import Sequence

def first_element(data: Sequence):

    print(data[0])
```

---

# 14) Mapping

Represents key-value collections.

Example:

```python
from typing import Mapping

def show(data: Mapping):

    print(data)
```

---

# 15) Type

Represents class types.

## Example

```python
from typing import Type

class Student:
    pass

def create_object(cls: Type):

    return cls()

obj = create_object(Student)
```

---

# 16) Literal

Restricts values to specific constants.

## Example

```python
from typing import Literal

def set_mode(mode: Literal["light", "dark"]):

    print(mode)

set_mode("dark")
```

Valid:

```text
light
dark
```

Invalid:

```text
blue
```

---

# 17) Final

Indicates a variable should not be reassigned.

## Example

```python
from typing import Final

PI: Final = 3.14
```

---

# 18) ClassVar

Used for static variables.

## Example

```python
from typing import ClassVar

class Student:

    college: ClassVar[str] = "ABC College"
```

---

# 19) TypeAlias

Used to create custom type aliases.

## Example

```python
from typing import TypeAlias

StudentId: TypeAlias = int

sid: StudentId = 101
```

---

# 20) NewType

Creates a distinct type.

## Example

```python
from typing import NewType

StudentId = NewType("StudentId", int)

sid = StudentId(101)
```

---

# Type Hints in Classes

```python
class Student:

    name: str
    marks: float

    def __init__(
            self,
            name: str,
            marks: float):

        self.name = name
        self.marks = marks
```

---

# Type Hints with *args

```python
from typing import Tuple

def add(*nums: int):

    return sum(nums)
```

---

# Type Hints with **kwargs

```python
from typing import Any

def details(**kwargs: Any):

    print(kwargs)
```

---

# Modern Python (3.10+)

Instead of:

```python
from typing import Union

name: Union[str, None]
```

Use:

```python
name: str | None
```

---

Instead of:

```python
Union[int, str]
```

Use:

```python
int | str
```

---

# Most Commonly Used Types

| Type      | Purpose               |
| --------- | --------------------- |
| List      | Lists                 |
| Tuple     | Tuples                |
| Dict      | Dictionaries          |
| Set       | Sets                  |
| Union     | Multiple Types        |
| Optional  | Value or None         |
| Any       | Any Type              |
| Callable  | Functions             |
| Generator | Generators            |
| Iterator  | Iterators             |
| Iterable  | Iterable Objects      |
| Sequence  | Ordered Collections   |
| Mapping   | Key-Value Collections |

---

# Real-Time Example

```python
from typing import List, Dict

def get_average(
        marks: List[int]) -> float:

    return sum(marks) / len(marks)


students: Dict[str, List[int]] = {
    "Rahul": [90, 80, 70],
    "Priya": [95, 85, 90]
}

print(get_average(students["Rahul"]))
```

Output:

```text
80.0
```

---

# Key Takeaways

* The `typing` module provides support for type hints.
* It improves readability and maintainability.
* Common types include:

  * `List`
  * `Tuple`
  * `Dict`
  * `Set`
  * `Union`
  * `Optional`
  * `Any`
  * `Callable`
  * `Generator`
* Type hints are not enforced at runtime.
* They help IDEs and tools like `mypy` detect type-related issues.
* Modern Python supports shorthand syntax like `int | str` instead of `Union[int, str]`.
