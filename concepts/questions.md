# Project: Student Grade Management System

### Problem Statement

Create a Python program to manage student marks using **Encapsulation**.

### Requirements

1. Create a class named `Student`.
2. Make the following attributes private:

   * Student ID
   * Student Name
   * Marks
3. Create methods:

   * `set_marks(marks)` → Update marks (0–100 only).
   * `get_marks()` → Return marks.
   * `calculate_grade()` → Return grade based on marks.
   * `display_details()` → Display student information.
4. Do not allow direct access to the marks variable.
5. Validate that marks cannot be less than 0 or greater than 100.

### Grade Criteria

| Marks    | Grade |
| -------- | ----- |
| 90-100   | A     |
| 75-89    | B     |
| 60-74    | C     |
| 40-59    | D     |
| Below 40 | F     |

### Sample Input

```text
Student ID: S101
Name: Ravi
Marks: 85
```

### Expected Output

```text
Student Details
---------------
ID: S101
Name: Ravi
Marks: 85
Grade: B
```

### Concepts Covered

* Encapsulation
* Private Attributes (`__marks`)
* Getter and Setter Methods
* Validation
* Object-Oriented Programming

### Challenge Extension

Add:

* Multiple subjects
* Average calculation
* Percentage calculation
* Pass/Fail status

```python
class Student:
    def __init__(self,sid,sname,marks):
        self.__sid=sid
        self.__sname=sname
        self.__marks=marks
    def set_marks(self,marks):
        if 0<=self.__marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks! marks should be between 0 and 100")
            
    def get_marks(self):
        return self.__marks
        
    def calculate_grade(self):
        if 90<=self.__marks<=100:
                return "A"
        elif 75<=self.__marks<=89:
                return "B"
        elif 60<=self.__marks<=74:
                return "C"
        elif 40<=self.__marks<=59:
                return "D"
        else:
                return "F"
    def display_details(self):
        print("Student Details")
        print("---------------")
        print(f"ID: {self.__sid}\n Name: {self.__sname}\n Marks: {self.__marks}\n Grade: {self.calculate_grade()}")
s1=Student("s101","Ravi",85)
s1.display_details()
s1.set_marks(71)
s1.display_details()
```
