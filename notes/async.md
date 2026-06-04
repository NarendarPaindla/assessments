# Introduction to Async Syntax in Python

## What is Asynchronous Programming?

Normally, Python executes code **one line after another**.

This is called:

```text
Synchronous Execution
```

Example:

```python
import time

print("Task 1 Started")
time.sleep(5)
print("Task 1 Completed")

print("Task 2 Started")
time.sleep(3)
print("Task 2 Completed")
```

### Output

```text
Task 1 Started
(wait 5 seconds)
Task 1 Completed

Task 2 Started
(wait 3 seconds)
Task 2 Completed
```

### Problem

While Task 1 is waiting:

```text
Task 2 cannot start.
```

CPU spends time waiting.

---

# Real-Time Example

Imagine you are ordering food online.

### Synchronous Way

```text
Place Order
Wait for Delivery
Eat Food
Then Start Watching Movie
```

Total time increases.

---

### Asynchronous Way

```text
Place Order
Start Watching Movie
Food Arrives
Eat Food
Continue Movie
```

Multiple tasks progress efficiently.

---

# What is Async Programming?

Async programming allows a program to:

```text
Start a Task
Pause while waiting
Do Other Work
Resume Later
```

without blocking the entire program.

---

# Async Keywords

Python provides two important keywords:

```python
async
await
```

---

# async Keyword

Used to define an asynchronous function.

## Syntax

```python
async def function_name():
    pass
```

Example:

```python
async def greet():
    print("Hello")
```

---

# Important Point

Calling an async function does NOT execute it immediately.

```python
async def greet():
    print("Hello")

greet()
```

Output:

```text
RuntimeWarning:
coroutine was never awaited
```

Because:

```text
greet()
```

returns a coroutine object.

---

# Coroutine

A coroutine is a special object returned by an async function.

Example:

```python
async def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
<coroutine object greet at 0x...>
```

---

# await Keyword

Used inside async functions.

It tells Python:

```text
Pause Here
Let Other Tasks Run
Resume Later
```

---

## Syntax

```python
await some_async_operation
```

---

# First Async Program

```python
import asyncio

async def greet():

    print("Hello")

asyncio.run(greet())
```

### Output

```text
Hello
```

---

# asyncio Module

Python provides:

```python
import asyncio
```

for asynchronous programming.

---

# asyncio.run()

Used to start the event loop and execute an async function.

```python
asyncio.run(function())
```

Example:

```python
import asyncio

async def display():
    print("Python Async")

asyncio.run(display())
```

Output:

```text
Python Async
```

---

# Simulating a Delay

Normal Delay:

```python
import time

time.sleep(3)
```

Blocks program execution.

---

Async Delay:

```python
import asyncio

await asyncio.sleep(3)
```

Does NOT block other async tasks.

---

# Example

```python
import asyncio

async def task():

    print("Started")

    await asyncio.sleep(3)

    print("Completed")

asyncio.run(task())
```

Output:

```text
Started
(wait 3 seconds)
Completed
```

---

# Understanding await

```python
await asyncio.sleep(3)
```

means:

```text
Pause this task
Allow other tasks to execute
Resume after 3 seconds
```

---

# Running Multiple Tasks

## Synchronous Version

```python
import time

def task1():

    print("Task1 Started")
    time.sleep(3)
    print("Task1 Completed")

def task2():

    print("Task2 Started")
    time.sleep(2)
    print("Task2 Completed")

task1()
task2()
```

Total Time:

```text
5 seconds
```

---

# Async Version

```python
import asyncio

async def task1():

    print("Task1 Started")

    await asyncio.sleep(3)

    print("Task1 Completed")

async def task2():

    print("Task2 Started")

    await asyncio.sleep(2)

    print("Task2 Completed")

async def main():

    await asyncio.gather(
        task1(),
        task2()
    )

asyncio.run(main())
```

Output:

```text
Task1 Started
Task2 Started

Task2 Completed
Task1 Completed
```

Total Time:

```text
3 seconds
```

instead of:

```text
5 seconds
```

---

# What is asyncio.gather()?

Used to run multiple async tasks concurrently.

## Syntax

```python
await asyncio.gather(
    task1(),
    task2(),
    task3()
)
```

---

# Visual Representation

### Synchronous

```text
Task1 ---> 3 sec

Task2 ---> 2 sec

Total = 5 sec
```

---

### Asynchronous

```text
Task1 ---> 3 sec
Task2 ---> 2 sec

Run Together

Total = 3 sec
```

---

# Async Function Calling Async Function

```python
import asyncio

async def greet():

    await asyncio.sleep(1)

    print("Hello")

async def main():

    await greet()

asyncio.run(main())
```

Output:

```text
Hello
```

---

# Async Example: Downloading Files

```python
async def download_file():

    await asyncio.sleep(5)

    print("File Downloaded")
```

While downloading:

```text
Other Tasks Can Run
```

---

# Event Loop

The Event Loop is the heart of AsyncIO.

It manages:

```text
Task Scheduling
Task Execution
Task Switching
```

---

## Flow

```text
Event Loop
     |
     |
     +---- Task 1
     |
     +---- Task 2
     |
     +---- Task 3
```

When one task waits:

```text
Event Loop switches
to another task.
```

---

# Async vs Sync

| Synchronous          | Asynchronous                     |
| -------------------- | -------------------------------- |
| One task at a time   | Multiple tasks progress together |
| Blocking             | Non-blocking                     |
| Slower for I/O tasks | Faster for I/O tasks             |
| Uses time.sleep()    | Uses asyncio.sleep()             |
| Simpler              | More powerful                    |

---

# When Should We Use Async?

Use async for:

### Network Requests

```text
API Calls
HTTP Requests
```

### File Operations

```text
Large File Reading
```

### Database Operations

```text
Queries
```

### Web Scraping

```text
Multiple Websites
```

### Chat Applications

```text
Real-Time Messaging
```

---

# When NOT to Use Async?

Avoid async for:

### Heavy CPU Calculations

```text
Image Processing
Machine Learning
Large Mathematical Computations
```

For these use:

```text
Multiprocessing
```

instead.

---

# Common AsyncIO Functions

| Function                | Purpose               |
| ----------------------- | --------------------- |
| `async def`             | Create async function |
| `await`                 | Pause and resume task |
| `asyncio.run()`         | Run async program     |
| `asyncio.sleep()`       | Non-blocking delay    |
| `asyncio.gather()`      | Run multiple tasks    |
| `asyncio.create_task()` | Schedule task         |
| `asyncio.wait()`        | Wait for tasks        |

---

# Interview Questions

## What is Async Programming?

A programming technique that allows tasks to pause and resume without blocking the entire program.

---

## What does async do?

Defines a coroutine function.

---

## What does await do?

Pauses current coroutine until awaited operation completes.

---

## What is a Coroutine?

A function defined using:

```python
async def
```

that can be paused and resumed.

---

## What is Event Loop?

The core component that schedules and manages asynchronous tasks.

---

# Key Takeaways

* Async programming is used for non-blocking execution.
* `async def` creates an asynchronous function.
* `await` pauses execution until a task completes.
* `asyncio` is Python's built-in async framework.
* `asyncio.run()` starts async execution.
* `asyncio.sleep()` is the async version of `time.sleep()`.
* `asyncio.gather()` runs multiple coroutines concurrently.
* Async is best for I/O-bound tasks such as APIs, databases, and networking.
* Event Loop manages all asynchronous tasks.
* Async improves performance when many tasks spend time waiting.
