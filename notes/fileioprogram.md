# File I/O in Python (Complete Notes with All Modes and Programs)

## What is File I/O?

**File I/O** means reading data from a file and writing data to a file.

### Real-Time Example

Suppose you are building a:

* Student Management System
* Banking Application
* Employee Management System

If the application closes, data stored in variables is lost.

To save data permanently, we store it in files.

```text
Student Name: Narendar
Marks: 95
```

Stored in:

```text
student.txt
```

---

# open() Function

Python uses the `open()` function to open a file.

### Syntax

```python
file_object = open("filename", "mode")
```

Example:

```python
f = open("student.txt", "r")
```

---

# File Modes in Python

| Mode | Meaning         |
| ---- | --------------- |
| r    | Read            |
| w    | Write           |
| a    | Append          |
| x    | Create New File |
| r+   | Read and Write  |
| w+   | Write and Read  |
| a+   | Append and Read |
| rb   | Read Binary     |
| wb   | Write Binary    |
| ab   | Append Binary   |

---

# 1. Read Mode (r)

Used to read existing files.

### File

student.txt

```text
Narendar
Ravi
Sai
```

### Program

```python
f = open("student.txt", "r")

data = f.read()

print(data)

f.close()
```

### Output

```text
Narendar
Ravi
Sai
```

### Explanation

```python
read()
```

Reads entire file content.

---

# 2. Write Mode (w)

Creates a new file.

If file exists → old content deleted.

### Program

```python
f = open("student.txt", "w")

f.write("Python Training")

f.close()
```

### Output File

```text
Python Training
```

### Explanation

Old data removed.

New data written.

---

# 3. Append Mode (a)

Adds data at end of file.

### Existing File

```text
Python Training
```

### Program

```python
f = open("student.txt", "a")

f.write("\nJava Training")

f.close()
```

### Output File

```text
Python Training
Java Training
```

### Explanation

Existing data remains.

New data added at end.

---

# 4. Create Mode (x)

Creates new file only.

### Program

```python
f = open("newfile.txt", "x")

f.write("Hello")

f.close()
```

### Output

```text
newfile.txt created
```

### Important

If file already exists:

```text
FileExistsError
```

---

# 5. Read + Write Mode (r+)

Read and modify existing file.

### File

```text
Python
```

### Program

```python
f = open("student.txt", "r+")

print(f.read())

f.write("\nJava")

f.close()
```

### Output File

```text
Python
Java
```

---

# 6. Write + Read Mode (w+)

Creates file.

Old data deleted.

Can read and write.

### Program

```python
f = open("student.txt", "w+")

f.write("Python")

f.seek(0)

print(f.read())

f.close()
```

### Output

```text
Python
```

---

# 7. Append + Read Mode (a+)

Append and read.

### Program

```python
f = open("student.txt", "a+")

f.write("\nDjango")

f.seek(0)

print(f.read())

f.close()
```

### Output

```text
Python
Java
Django
```

---

# Binary Files

Used for:

* Images
* Videos
* PDFs
* Audio

---

# 8. Binary Read Mode (rb)

### Program

```python
f = open("photo.jpg", "rb")

data = f.read()

print(data)

f.close()
```

### Output

```text
b'\xff\xd8\xff\xe0...'
```

Binary data displayed.

---

# 9. Binary Write Mode (wb)

Copy image.

### Program

```python
source = open("photo.jpg", "rb")

data = source.read()

target = open("copy.jpg", "wb")

target.write(data)

source.close()
target.close()
```

### Output

```text
copy.jpg created
```

---

# 10. Binary Append Mode (ab)

Used for appending binary data.

### Program

```python
f = open("sample.bin", "ab")

f.write(b"Hello")

f.close()
```

---

# Important File Methods

---

## read()

Reads entire file.

```python
f = open("student.txt","r")

print(f.read())

f.close()
```

---

## readline()

Reads one line.

### File

```text
Python
Java
Django
```

### Program

```python
f = open("student.txt","r")

print(f.readline())

f.close()
```

### Output

```text
Python
```

---

## readlines()

Reads all lines as list.

### Program

```python
f = open("student.txt","r")

print(f.readlines())

f.close()
```

### Output

```python
['Python\n', 'Java\n', 'Django']
```

---

## write()

Writes string.

```python
f = open("demo.txt","w")

f.write("Hello Python")

f.close()
```

---

## writelines()

Writes multiple lines.

```python
f = open("demo.txt","w")

lines = [
    "Python\n",
    "Java\n",
    "Django\n"
]

f.writelines(lines)

f.close()
```

### Output File

```text
Python
Java
Django
```

---

## seek()

Moves cursor position.

### Program

```python
f = open("student.txt","r")

f.seek(3)

print(f.read())

f.close()
```

### File

```text
Python
```

### Output

```text
hon
```

Cursor starts from index 3.

---

## tell()

Returns current cursor position.

### Program

```python
f = open("student.txt","r")

print(f.tell())

f.read(3)

print(f.tell())

f.close()
```

### Output

```text
0
3
```

---

# Best Practice (with Statement)

Instead of:

```python
f = open("student.txt","r")

print(f.read())

f.close()
```

Use:

```python
with open("student.txt","r") as f:
    print(f.read())
```

### Advantage

Automatically closes file.

No need:

```python
f.close()
```

---

# Interview Questions

### 1. Difference between w and a?

| w                     | a                 |
| --------------------- | ----------------- |
| Deletes old content   | Keeps old content |
| Starts from beginning | Adds at end       |

---

### 2. Difference between read(), readline(), readlines()?

| Method      | Purpose           |
| ----------- | ----------------- |
| read()      | Entire file       |
| readline()  | Single line       |
| readlines() | All lines as list |

---

### 3. What does seek() do?

Moves file cursor to a specific position.

---

### 4. What does tell() do?

Returns current cursor position.

---

### 5. Why use `with open()`?

Automatically closes the file and prevents resource leaks.

---

# Placement Practice Programs

### Program 1: Count Characters in File

```python
with open("student.txt","r") as f:
    data = f.read()
    print(len(data))
```

---

### Program 2: Count Words

```python
with open("student.txt","r") as f:
    data = f.read()
    print(len(data.split()))
```

---

### Program 3: Count Lines

```python
with open("student.txt","r") as f:
    print(len(f.readlines()))
```

---

### Program 4: Copy One File to Another

```python
with open("source.txt","r") as source:
    data = source.read()

with open("target.txt","w") as target:
    target.write(data)
```

---

### Program 5: Find Number of Vowels in File

```python
with open("student.txt","r") as f:
    data = f.read().lower()

count = 0

for ch in data:
    if ch in "aeiou":
        count += 1

print(count)
```
