If you already know Python OOPS, the easiest way to learn JavaScript OOPS is by comparing both side-by-side.

# 1. Class and Object

## Python

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student("Narendar")
s1.display()
```

### Output

```text
Name: Narendar
```

---

## JavaScript

```javascript
class Student {
    constructor(name) {
        this.name = name;
    }

    display() {
        console.log("Name:", this.name);
    }
}

const s1 = new Student("Narendar");
s1.display();
```

### Output

```text
Name: Narendar
```

### Explanation

| Python        | JavaScript    |
| ------------- | ------------- |
| class Student | class Student |
| **init**()    | constructor() |
| self          | this          |
| print()       | console.log() |

---

# 2. Constructor

## Python

```python
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

e1 = Employee(101, "John")

print(e1.id)
print(e1.name)
```

### Output

```text
101
John
```

---

## JavaScript

```javascript
class Employee {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }
}

const e1 = new Employee(101, "John");

console.log(e1.id);
console.log(e1.name);
```

### Output

```text
101
John
```

---

# 3. Instance Methods

## Python

```python
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()

print(c.add(10, 20))
```

### Output

```text
30
```

---

## JavaScript

```javascript
class Calculator {
    add(a, b) {
        return a + b;
    }
}

const c = new Calculator();

console.log(c.add(10, 20));
```

### Output

```text
30
```

---

# 4. Encapsulation

## Python

```python
class Bank:
    def __init__(self):
        self.__balance = 1000

    def show(self):
        print(self.__balance)

b = Bank()
b.show()
```

### Output

```text
1000
```

---

## JavaScript

```javascript
class Bank {
    #balance = 1000;

    show() {
        console.log(this.#balance);
    }
}

const b = new Bank();
b.show();
```

### Output

```text
1000
```

### Explanation

```javascript
#balance
```

means private variable.

Cannot access:

```javascript
console.log(b.#balance);
```

Error:

```text
Private field '#balance' must be declared
```

---

# 5. Inheritance

## Python

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

### Output

```text
Animal Sound
```

---

## JavaScript

```javascript
class Animal {
    sound() {
        console.log("Animal Sound");
    }
}

class Dog extends Animal {
}

const d = new Dog();
d.sound();
```

### Output

```text
Animal Sound
```

### Explanation

| Python            | JavaScript               |
| ----------------- | ------------------------ |
| class Dog(Animal) | class Dog extends Animal |

---

# 6. Method Overriding

## Python

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```

### Output

```text
Bark
```

---

## JavaScript

```javascript
class Animal {
    sound() {
        console.log("Animal Sound");
    }
}

class Dog extends Animal {
    sound() {
        console.log("Bark");
    }
}

const d = new Dog();
d.sound();
```

### Output

```text
Bark
```

---

# 7. Parent Method Access

## Python

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

d = Dog()
d.sound()
```

### Output

```text
Animal Sound
Bark
```

---

## JavaScript

```javascript
class Animal {
    sound() {
        console.log("Animal Sound");
    }
}

class Dog extends Animal {
    sound() {
        super.sound();
        console.log("Bark");
    }
}

const d = new Dog();
d.sound();
```

### Output

```text
Animal Sound
Bark
```

---

# 8. Polymorphism

## Python

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()
```

### Output

```text
Bark
Meow
```

---

## JavaScript

```javascript
class Dog {
    sound() {
        console.log("Bark");
    }
}

class Cat {
    sound() {
        console.log("Meow");
    }
}

const animals = [new Dog(), new Cat()];

animals.forEach(a => a.sound());
```

### Output

```text
Bark
Meow
```

---

# 9. Static Methods

## Python

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))
```

### Output

```text
30
```

---

## JavaScript

```javascript
class MathUtil {
    static add(a, b) {
        return a + b;
    }
}

console.log(MathUtil.add(10, 20));
```

### Output

```text
30
```

---

# 10. Real-Time Example (Student Management)

```javascript
class Student {
    constructor(id, name, course) {
        this.id = id;
        this.name = name;
        this.course = course;
    }

    display() {
        console.log(
            `ID: ${this.id}, Name: ${this.name}, Course: ${this.course}`
        );
    }
}

const s1 = new Student(101, "John", "JavaScript");
const s2 = new Student(102, "Smith", "Python");

s1.display();
s2.display();
```

### Output

```text
ID: 101, Name: John, Course: JavaScript
ID: 102, Name: Smith, Course: Python
```

---

# JavaScript OOPS Cheat Sheet for Python Developers

| Python           | JavaScript      |      |
| ---------------- | --------------- | ---- |
| class            | class           |      |
| **init**()       | constructor()   |      |
| self             | this            |      |
| super()          | super()         |      |
| print()          | console.log()   |      |
| @staticmethod    | static          |      |
| Inheritance      | extends         |      |
| Object Creation  | new ClassName() |      |
| Private Variable | __var           | #var |

---

## Practice Task

Create a `Car` class:

### Requirements

1. Constructor should accept:

   * brand
   * model

2. Method:

   * display()

3. Create two objects:

   * Toyota Camry
   * Honda City

### Expected Output

```text
Brand: Toyota, Model: Camry
Brand: Honda, Model: City
```

