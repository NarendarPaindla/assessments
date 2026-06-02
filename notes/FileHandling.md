# File Handling in Python

## Why Do We Need Files?

* During program execution, data is stored in memory (RAM).
* RAM is temporary storage, so data is lost when the program stops.
* To store data permanently for future use, we use files.
* Files provide permanent storage for data.

### Real-Time Examples

* Student Records
* Employee Information
* Bank Transactions
* Product Details
* User Registration Data

---

# Types of Files

Python mainly supports two types of files:

## 1) Text Files

Text files store character data.

### Examples

```text
students.txt
employees.txt
data.csv
notes.txt
```

### Stored Data Example

```text
Narayan
Ravi
Kiran
```

---

## 2) Binary Files

Binary files store data in binary format (0s and 1s).

### Examples

* Images
* Videos
* Audio Files
* PDF Files
* Executable Files

### Example File Types

```text
photo.jpg
video.mp4
song.mp3
report.pdf
```

---

# Opening a File

Before performing any operation on a file, we must first open it.

Python provides the built-in function:

```python
open()
```

### Syntax

```python
file_object = open(filename, mode)
```

### Parameters

| Parameter | Description                 |
| --------- | --------------------------- |
| filename  | Name of the file            |
| mode      | Purpose of opening the file |

---

# File Opening Modes

## 1) Read Mode (`r`)

Used to read data from an existing file.

### Features

* File must already exist.
* File pointer starts at the beginning.
* Default mode.

### Example

```python
f = open("students.txt", "r")
```

### If File Doesn't Exist

```text
FileNotFoundError
```

---

## 2) Write Mode (`w`)

Used to write data into a file.

### Features

* Creates file if not present.
* If file already contains data, old data is deleted.
* New data replaces old data.

### Example

```python
f = open("students.txt", "w")
```

---

## 3) Append Mode (`a`)

Used to add data at the end of the file.

### Features

* Existing data remains unchanged.
* New data is added at the end.
* Creates file if not present.

### Example

```python
f = open("students.txt", "a")
```

---

## 4) Read and Write Mode (`r+`)

Used for both reading and writing.

### Features

* Existing data is not deleted.
* File pointer starts from beginning.

### Example

```python
f = open("students.txt", "r+")
```

---

## 5) Write and Read Mode (`w+`)

Used for writing and reading.

### Features

* Existing data is deleted.
* New file created if not present.

### Example

```python
f = open("students.txt", "w+")
```

---

## 6) Append and Read Mode (`a+`)

Used for appending and reading.

### Features

* Existing data is preserved.
* New data added at end.

### Example

```python
f = open("students.txt", "a+")
```

---

## 7) Exclusive Creation Mode (`x`)

Used to create a new file.

### Features

* Creates file only if file does not exist.
* If file already exists:

```text
FileExistsError
```

### Example

```python
f = open("students.txt", "x")
```

---

# Binary File Modes

All above modes are applicable for text files.

For binary files, add suffix:

```text
b
```

### Examples

```python
rb
wb
ab
r+b
w+b
a+b
xb
```

---

# Example

```python
f = open("sample.txt", "w")
```

Meaning:

```text
Open sample.txt for writing.
```

---

# Closing a File

After completing operations on a file, it is recommended to close it.

### Function

```python
f.close()
```

### Why Close?

* Releases system resources
* Saves memory
* Ensures proper data storage

---

# Various Properties of File Object

After opening a file, Python provides useful properties.

---

## 1) name

Returns file name.

### Example

```python
print(f.name)
```

---

## 2) mode

Returns opening mode.

### Example

```python
print(f.mode)
```

---

## 3) closed

Returns:

```python
True
```

if file is closed, otherwise:

```python
False
```

### Example

```python
print(f.closed)
```

---

## 4) readable()

Checks whether file can be read.

### Example

```python
print(f.readable())
```

### Returns

```python
True or False
```

---

## 5) writable()

Checks whether file can be written.

### Example

```python
print(f.writable())
```

### Returns

```python
True or False
```

---

# Example Program

```python
f = open("sample.txt", "w")

print("File Name:", f.name)
print("File Mode:", f.mode)
print("Is File Readable:", f.readable())
print("Is File Writable:", f.writable())
print("Is File Closed:", f.closed)

f.close()

print("Is File Closed:", f.closed)
```

### Output

```text
File Name: sample.txt
File Mode: w
Is File Readable: False
Is File Writable: True
Is File Closed: False
Is File Closed: True
```

---

# Writing Data to Text Files

Python provides two methods for writing data.

## Method 1: write()

Used to write a string.

### Syntax

```python
f.write(data)
```

---

## Example

```python
f = open("students.txt", "w")

f.write("Ramesh\n")
f.write("Suresh\n")
f.write("Mahesh\n")

print("Data written successfully")

f.close()
```

### students.txt

```text
Ramesh
Suresh
Mahesh
```

---

## Important Note

If the file is opened in:

```python
"w"
```

mode every time, previous data will be overwritten.

### Example

```python
f = open("students.txt", "a")
```

Using append mode preserves old data.

---

# Method 2: writelines()

Used to write multiple lines together.

### Syntax

```python
f.writelines(list_of_strings)
```

---

## Example

```python
f = open("students.txt", "w")

names = [
    "Anil\n",
    "Sunil\n",
    "Vinay\n",
    "Kiran\n"
]

f.writelines(names)

print("List written successfully")

f.close()
```

### students.txt

```text
Anil
Sunil
Vinay
Kiran
```

---

# Important Note About `write()`

When using:

```python
write()
```

you must manually provide line separator.

### Correct

```python
f.write("Anil\n")
```

### Wrong

```python
f.write("Anil")
f.write("Sunil")
```

Output:

```text
AnilSunil
```

---

# Comparison: write() vs writelines()

| write()                              | writelines()            |
| ------------------------------------ | ----------------------- |
| Writes one string at a time          | Writes multiple strings |
| Requires repeated calls              | Single call sufficient  |
| Suitable for small data              | Suitable for bulk data  |
| Returns number of characters written | Writes list of strings  |

---

# Real-Time Analogy

Imagine maintaining student attendance.

### write()

Teacher writes one student name at a time.

```text
Anil
Sunil
Kiran
```

---

### writelines()

Teacher receives a complete list and writes all names together.

```text
[Anil, Sunil, Kiran]
```

---

# Key Takeaways

* Files provide permanent storage.
* Two file types:

  * Text Files
  * Binary Files
* Open file using:

```python
open(filename, mode)
```

* Common modes:

  * `r`
  * `w`
  * `a`
  * `r+`
  * `w+`
  * `a+`
  * `x`

* Close file using:

```python
close()
```

* Important file properties:

  * `name`
  * `mode`
  * `closed`
  * `readable()`
  * `writable()`

* Data can be written using:

  * `write()`
  * `writelines()`

* `w` mode overwrites existing data.

* `a` mode appends data.

* Use `\n` for new lines while writing text files.
# Reading Character Data from Text Files

After writing data into a text file, we often need to read it back.

Python provides the following methods for reading character data from text files.

---

# Reading Methods

| Method        | Purpose                            |
| ------------- | ---------------------------------- |
| `read()`      | Reads entire file content          |
| `read(n)`     | Reads first `n` characters         |
| `readline()`  | Reads one line at a time           |
| `readlines()` | Reads all lines and returns a list |

---

# Sample File Content

Assume the file contains:

```text
sunny
bunny
chinny
vinny
```

---

# 1) read() Method

## Purpose

Reads the complete file content.

### Syntax

```python
file.read()
```

---

## Example

```python
f = open("students.txt", "r")

data = f.read()

print(data)

f.close()
```

### Output

```text
sunny
bunny
chinny
vinny
```

---

## Explanation

```python
f.read()
```

reads all characters from beginning to end.

File pointer reaches the end of file after reading.

---

# 2) read(n) Method

## Purpose

Reads only the first `n` characters.

### Syntax

```python
file.read(n)
```

---

## Example

```python
f = open("students.txt", "r")

data = f.read(10)

print(data)

f.close()
```

### Output

```text
sunny
bunn
```

---

## Explanation

Suppose file contains:

```text
sunny
bunny
chinny
vinny
```

First 10 characters are:

```text
s u n n y \n b u n n
```

Hence output:

```text
sunny
bunn
```

---

# 3) readline() Method

## Purpose

Reads one line at a time.

### Syntax

```python
file.readline()
```

---

## Example

```python
f = open("students.txt", "r")

line1 = f.readline()
print(line1, end="")

line2 = f.readline()
print(line2, end="")

line3 = f.readline()
print(line3, end="")

f.close()
```

### Output

```text
sunny
bunny
chinny
```

---

## Explanation

Every call to:

```python
readline()
```

reads only one line and moves file pointer to next line.

---

# 4) readlines() Method

## Purpose

Reads all lines and stores them inside a list.

### Syntax

```python
file.readlines()
```

---

## Example

```python
f = open("students.txt", "r")

lines = f.readlines()

for line in lines:
    print(line, end="")

f.close()
```

### Output

```text
sunny
bunny
chinny
vinny
```

---

## Explanation

`readlines()` returns:

```python
[
 'sunny\n',
 'bunny\n',
 'chinny\n',
 'vinny\n'
]
```

Each list element represents one line.

---

# Understanding File Pointer Movement

A very important concept in file handling is:

```text
File Pointer (Cursor)
```

Whenever data is read, the cursor automatically moves forward.

---

## Example

Assume file contains:

```text
sunny
bunny
chinny
vinny
```

### Program

```python
f = open("students.txt", "r")

print(f.read(3))

print(f.readline())

print(f.read(4))

print("Remaining Data")

print(f.read())

f.close()
```

---

### Output

```text
sun
ny

bunn

Remaining Data

y
chinny
vinny
```

---

## Explanation

### Step 1

```python
f.read(3)
```

Reads:

```text
sun
```

Cursor moves after `sun`.

---

### Step 2

```python
f.readline()
```

Reads remaining part of first line:

```text
ny
```

Cursor moves to next line.

---

### Step 3

```python
f.read(4)
```

Reads:

```text
bunn
```

Cursor moves further.

---

### Step 4

```python
f.read()
```

Reads all remaining content.

---

# Real-Time Analogy

Imagine reading a book.

When you finish page 1:

```text
You don't start again from page 1.
```

You continue from where you stopped.

Similarly:

```text
File Pointer remembers current position.
```

---

# The `with` Statement

## Problem

Normally we write:

```python
f = open("data.txt")
...
f.close()
```

If programmer forgets:

```python
close()
```

resources may not be released properly.

---

## Solution

Python provides:

```python
with
```

statement.

---

## Advantages

* Automatically closes file.
* Cleaner code.
* Safer programming.
* Works even if exception occurs.

---

## Syntax

```python
with open(filename, mode) as f:
    statements
```

---

## Example

```python
with open("students.txt", "w") as f:

    f.write("Ravi\n")
    f.write("Kiran\n")
    f.write("Anil\n")

    print("Is File Closed:", f.closed)

print("Is File Closed:", f.closed)
```

### Output

```text
Is File Closed: False
Is File Closed: True
```

---

## Explanation

Inside block:

```python
with
```

file remains open.

After block completes:

Python automatically executes:

```python
close()
```

---

# seek() and tell() Methods

These methods help us control and track file pointer position.

---

# tell() Method

## Purpose

Returns current cursor position.

### Syntax

```python
file.tell()
```

---

## Important Point

File position starts from:

```text
0
```

just like string indexing.

---

## Example File

```text
sunny
bunny
chinny
vinny
```

---

## Example Program

```python
f = open("students.txt", "r")

print(f.tell())

print(f.read(2))

print(f.tell())

print(f.read(3))

print(f.tell())

f.close()
```

---

### Output

```text
0
su
2
nny
5
```

---

## Explanation

Initially:

```python
f.tell()
```

returns:

```text
0
```

because cursor is at beginning.

---

After:

```python
f.read(2)
```

cursor moves to:

```text
2
```

---

After:

```python
f.read(3)
```

cursor moves to:

```text
5
```

---

# Visual Representation

Suppose file contains:

```text
s u n n y
0 1 2 3 4
```

Initially:

```text
Cursor → 0
```

After reading two characters:

```text
su
```

Cursor becomes:

```text
2
```

---

# Summary of Reading Methods

| Method        | Reads              |
| ------------- | ------------------ |
| `read()`      | Entire file        |
| `read(n)`     | First n characters |
| `readline()`  | One line           |
| `readlines()` | All lines as list  |

---

# Summary of File Pointer Methods

| Method   | Purpose                           |
| -------- | --------------------------------- |
| `tell()` | Current cursor position           |
| `seek()` | Move cursor to specified position |

(We will study `seek()` in detail in the next topic.)

---

# Key Takeaways

* `read()` reads entire file.
* `read(n)` reads first `n` characters.
* `readline()` reads one line.
* `readlines()` returns all lines as a list.
* File pointer automatically moves after reading.
* `with` statement automatically closes files.
* `tell()` returns current cursor position.
* File indexing starts from `0`.
* `with open(...)` is the recommended way to work with files in Python.
* Understanding file pointer movement is essential before learning `seek()`.


# The `seek()` Method

## What is `seek()`?

The `seek()` method is used to move the cursor (file pointer) to a specific position in the file.

### Real-Time Example

Imagine you are reading a book.

* Normally, you read page by page.
* But if someone asks you to go directly to page 50, you can jump there immediately.

Similarly:

```python
seek()
```

allows us to move directly to a required position in a file.

---

# Syntax

```python
file.seek(offset, fromwhere)
```

### Parameters

| Parameter | Description                 |
| --------- | --------------------------- |
| offset    | Number of positions to move |
| fromwhere | Starting point for movement |

---

# Values of `fromwhere`

| Value | Meaning                     |
| ----- | --------------------------- |
| 0     | Beginning of file (Default) |
| 1     | Current cursor position     |
| 2     | End of file                 |

### Note

Python 2 supports:

```text
0, 1, 2
```

Python 3 generally supports:

```text
0
```

for text files.

---

# Example

## Initial Data

```python
data = "All Students are STUPIDS"
```

---

## Program

```python
data = "All Students are STUPIDS"

f = open("abc.txt", "w")
f.write(data)
f.close()

with open("abc.txt", "r+") as f:

    text = f.read()
    print(text)

    print("Current Cursor Position:",
          f.tell())

    f.seek(17)

    print("Current Cursor Position:",
          f.tell())

    f.write("GEMS!!!")

    f.seek(0)

    text = f.read()

    print("Data After Modification:")
    print(text)
```

---

## Output

```text
All Students are STUPIDS

Current Cursor Position: 24

Current Cursor Position: 17

Data After Modification:

All Students are GEMS!!!
```

---

# Explanation

Initially:

```text
All Students are STUPIDS
```

After reading entire file:

```python
f.tell()
```

returns:

```text
24
```

because cursor reaches end of file.

---

Then:

```python
f.seek(17)
```

moves cursor to position:

```text
17
```

and writing:

```python
GEMS!!!
```

overwrites:

```text
STUPIDS
```

Result:

```text
All Students are GEMS!!!
```

---

# Visual Representation

```text
All Students are STUPIDS
                 ^
               17
```

After writing:

```text
All Students are GEMS!!!
```

---

# Checking Whether a File Exists or Not

Before opening a file, it is a good practice to verify whether it exists.

Python provides:

```python
os.path.isfile()
```

---

# Syntax

```python
os.path.isfile(filename)
```

### Returns

```python
True
```

if file exists.

```python
False
```

if file does not exist.

---

# Example Program

## Check File Existence and Print Content

```python
import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):

    print("File exists:", fname)

    f = open(fname, "r")

else:

    print("File does not exist:", fname)

    sys.exit(0)

print("The content of file is:")

data = f.read()

print(data)
```

---

## Execution 1

### Input

```text
Enter File Name: student.txt
```

### Output

```text
File does not exist: student.txt
```

Program terminates.

---

## Execution 2

### Input

```text
Enter File Name: abc.txt
```

### Output

```text
File exists: abc.txt

The content of file is:

All Students are GEMS!!!
```

---

# Explanation

### Step 1

Take file name from user.

### Step 2

Check existence using:

```python
os.path.isfile()
```

### Step 3

If file exists:

```python
open()
```

the file.

### Step 4

Otherwise:

```python
sys.exit()
```

terminate program.

---

# What is `sys.exit()`?

Used to terminate program execution immediately.

---

## Syntax

```python
sys.exit(status_code)
```

---

## Example

```python
sys.exit(0)
```

### Meaning

```text
Normal Program Termination
```

---

# Program to Count Lines, Words and Characters

This is one of the most important interview programs in File Handling.

---

# Problem Statement

Write a program to display:

1. Number of Lines
2. Number of Words
3. Number of Characters

present in a file.

---

# Program

```python
import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):

    print("File exists:", fname)

    f = open(fname, "r")

else:

    print("File does not exist:", fname)

    sys.exit(0)

lcount = 0
wcount = 0
ccount = 0

for line in f:

    lcount = lcount + 1

    ccount = ccount + len(line)

    words = line.split()

    wcount = wcount + len(words)

print("Number of Lines:", lcount)

print("Number of Words:", wcount)

print("Number of Characters:", ccount)
```

---

# Sample File

```text
Python is easy
Python is powerful
Python is popular
```

---

# Output

```text
Number of Lines: 3

Number of Words: 9

Number of Characters: 50
```

---

# Logic Behind Counting

## Counting Lines

Every iteration:

```python
for line in f:
```

reads one line.

So:

```python
lcount += 1
```

counts lines.

---

## Counting Characters

```python
len(line)
```

returns total characters in that line.

So:

```python
ccount += len(line)
```

counts total characters.

---

## Counting Words

Convert line into words using:

```python
line.split()
```

Example:

```python
"Python is easy".split()
```

returns:

```python
['Python', 'is', 'easy']
```

Number of words:

```python
len(words)
```

---

# Visual Understanding

Suppose file contains:

```text
Python is easy
I love coding
```

### Line Count

```text
2
```

---

### Word Count

```text
Python
is
easy
I
love
coding
```

Total:

```text
6
```

---

### Character Count

Characters include:

```text
Letters
Digits
Spaces
Special Characters
```

depending on how file content is stored.

---

# Summary of Important File Methods

| Method       | Purpose                 |
| ------------ | ----------------------- |
| open()       | Open file               |
| close()      | Close file              |
| read()       | Read complete file      |
| read(n)      | Read n characters       |
| readline()   | Read one line           |
| readlines()  | Read all lines          |
| write()      | Write string            |
| writelines() | Write list of strings   |
| tell()       | Current cursor position |
| seek()       | Move cursor             |
| readable()   | Check readability       |
| writable()   | Check writability       |

---

# Key Takeaways

* `seek()` moves cursor to a specific location.
* `tell()` returns current cursor position.
* `os.path.isfile()` checks file existence.
* `sys.exit(0)` terminates the program normally.
* `line.split()` is commonly used to count words.
* Important interview program:

  * Count Lines
  * Count Words
  * Count Characters
* Always check whether a file exists before opening it.
* `seek()` and `tell()` are used together for cursor management in files.
* File handling is widely used in:

  * Log Processing
  * Report Generation
  * Data Analysis
  * Configuration Management
  * Student/Employee Record Systems
# Handling Binary Data

## What is Binary Data?

So far, we have worked with text files that store character data.

In real-world applications, we also need to store and process:

* Images
* Videos
* Audio Files
* PDF Documents
* Executable Files

Such data is called **Binary Data**.

### Examples

```text
photo.jpg
logo.png
song.mp3
video.mp4
report.pdf
```

To handle binary data, we use binary file modes:

```python
rb   # Read Binary
wb   # Write Binary
ab   # Append Binary
```

---

# Program to Read an Image File and Write to a New Image File

This program creates a copy of an existing image.

## Program

```python
f1 = open("source.jpg", "rb")

f2 = open("copy.jpg", "wb")

data = f1.read()

f2.write(data)

print("New image created successfully")

f1.close()
f2.close()
```

---

## Explanation

### Step 1

```python
f1 = open("source.jpg", "rb")
```

Open image for reading.

---

### Step 2

```python
f2 = open("copy.jpg", "wb")
```

Create a new image file.

---

### Step 3

```python
data = f1.read()
```

Read all binary content.

---

### Step 4

```python
f2.write(data)
```

Write binary content into new image.

---

### Result

```text
source.jpg  --->  copy.jpg
```

Both images will contain the same content.

---

# Handling CSV Files

## What is CSV?

CSV stands for:

```text
Comma Separated Values
```

CSV files are commonly used for:

* Employee Records
* Student Records
* Sales Reports
* Excel Data Exchange

### Example CSV

```csv
ENO,ENAME,ESAL,EADDR
100,Ravi,5000,Hyderabad
200,Kiran,7000,Mumbai
300,Arjun,9000,Delhi
```

---

# Python CSV Module

Python provides a built-in module:

```python
import csv
```

to handle CSV files.

---

# Writing Data to a CSV File

## Program

```python
import csv

with open("employees.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow(
        ["ENO", "ENAME", "ESAL", "EADDR"]
    )

    n = int(input(
        "Enter Number of Employees: "
    ))

    for i in range(n):

        eno = input("Employee Number: ")
        ename = input("Employee Name: ")
        esal = input("Employee Salary: ")
        eaddr = input("Employee Address: ")

        writer.writerow(
            [eno, ename, esal, eaddr]
        )

print("Employee data written successfully")
```

---

# Explanation

### Create CSV Writer Object

```python
writer = csv.writer(f)
```

---

### Write Header

```python
writer.writerow(
    ["ENO","ENAME","ESAL","EADDR"]
)
```

---

### Write Employee Records

```python
writer.writerow(
    [eno,ename,esal,eaddr]
)
```

Each call writes one row.

---

# Why Use `newline=""`?

## Recommended

```python
with open("employees.csv",
          "w",
          newline="") as f:
```

### Reason

Without:

```python
newline=""
```

extra blank lines may appear in CSV files (especially on Windows systems).

---

# Reading Data from CSV File

## Program

```python
import csv

f = open("employees.csv", "r")

reader = csv.reader(f)

data = list(reader)

for row in data:

    for value in row:

        print(value, "\t", end="")

    print()

f.close()
```

---

## Sample Output

```text
ENO    ENAME    ESAL    EADDR

100    Ravi     5000    Hyderabad
200    Kiran    7000    Mumbai
300    Arjun    9000    Delhi
```

---

# Explanation

### Create Reader Object

```python
reader = csv.reader(f)
```

---

### Convert to List

```python
data = list(reader)
```

Result:

```python
[
 ['ENO','ENAME','ESAL','EADDR'],
 ['100','Ravi','5000','Hyderabad'],
 ['200','Kiran','7000','Mumbai']
]
```

---

# Zipping and Unzipping Files

## What is Zipping?

Zipping means compressing one or more files into a single file.

Example:

```text
report.doc
photo.jpg
data.csv

↓

files.zip
```

---

# Advantages of Zipping

## 1) Better Memory Utilization

Compressed files occupy less storage.

---

## 2) Faster Transfer

Smaller files transfer more quickly.

---

## 3) Better Performance

Less storage and faster movement of data.

---

# Python Zip Module

Python provides:

```python
zipfile
```

module.

Important class:

```python
ZipFile
```

---

# Creating a ZIP File

## Syntax

```python
ZipFile(
    zip_name,
    mode,
    ZIP_DEFLATED
)
```

### ZIP_DEFLATED

Represents compression mode.

---

## Example

```python
from zipfile import *

f = ZipFile(
    "files.zip",
    "w",
    ZIP_DEFLATED
)

f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")

f.close()

print("ZIP file created successfully")
```

---

# Visual Representation

```text
file1.txt
file2.txt
file3.txt

      ↓

   files.zip
```

---

# Unzipping Files

## Syntax

```python
ZipFile(
    "files.zip",
    "r",
    ZIP_STORED
)
```

### ZIP_STORED

Represents extraction/read operation.

This is the default value.

---

# Reading Contents of ZIP File

## Program

```python
from zipfile import *

f = ZipFile(
    "files.zip",
    "r",
    ZIP_STORED
)

names = f.namelist()

for name in names:

    print("File Name:", name)

    print("Content:")

    f1 = open(name, "r")

    print(f1.read())

    print()
```

---

# Explanation

### Get All File Names

```python
names = f.namelist()
```

Returns:

```python
[
 'file1.txt',
 'file2.txt',
 'file3.txt'
]
```

---

### Read Individual Files

```python
for name in names:
```

Read each extracted file.

---

# Working with Directories

## What is a Directory?

A directory is another name for a folder.

Examples:

```text
Documents
Downloads
Projects
PythonNotes
```

---

# Common Directory Operations

### 1. Find Current Working Directory

```text
Where am I currently working?
```

---

### 2. Create New Directory

```text
Create a new folder.
```

---

### 3. Delete Directory

```text
Remove a folder.
```

---

### 4. Rename Directory

```text
Change folder name.
```

---

### 5. List Directory Contents

```text
Display all files and folders.
```

---

# Python Module for Directory Operations

Python provides:

```python
import os
```

The `os` module contains functions for performing directory-related operations.

---

# Real-Time Example

Suppose a company stores files as:

```text
CompanyData/
│
├── Employees.csv
├── Salary.csv
├── Reports/
│     ├── Jan.pdf
│     ├── Feb.pdf
│
└── Images/
      ├── logo.png
      ├── banner.jpg
```

Using the `os` module, we can:

* Create folders
* Rename folders
* Delete folders
* List files
* Navigate directories

---

# Key Takeaways

* Binary files store non-text data such as images, audio, and videos.
* Use:

  * `rb` → Read Binary
  * `wb` → Write Binary
  * `ab` → Append Binary
* CSV stands for Comma Separated Values.
* Python provides the `csv` module for CSV handling.
* `csv.writer()` writes records.
* `csv.reader()` reads records.
* Use `newline=""` while writing CSV files.
* Python provides the `zipfile` module for compression.
* `ZipFile` class is used for zipping and unzipping files.
* `ZIP_DEFLATED` performs compression.
* `namelist()` returns all file names inside a ZIP file.
* Directories are folders used to organize files.
* The `os` module is used for directory-related operations.
* Common directory tasks include:

  * Create
  * Rename
  * Delete
  * Navigate
  * List contents
