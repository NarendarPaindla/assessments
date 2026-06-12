# DOM Manipulation

DOM Manipulation starts with **selecting elements** from the HTML page. Before changing content, styles, attributes, or handling events, we must first get a reference to the element.

Think of the DOM as a tree:

```html
<body>
    <h1 id="title">Welcome</h1>

    <p class="info">Paragraph 1</p>
    <p class="info">Paragraph 2</p>

    <button>Click Me</button>
</body>
```

JavaScript must first locate an element before doing anything with it.

---

# 1. getElementById()

Most commonly used selector.

Selects an element using its unique ID.

## HTML

```html
<h1 id="title">Welcome to JavaScript</h1>
```

## JavaScript

```javascript
let element = document.getElementById("title");

console.log(element);
```

## Output

```html
<h1 id="title">Welcome to JavaScript</h1>
```

---

## Changing Content

```javascript
let element = document.getElementById("title");

element.innerText = "DOM Manipulation";
```

### Before

```html
Welcome to JavaScript
```

### After

```html
DOM Manipulation
```

---

## Changing Style

```javascript
let element = document.getElementById("title");

element.style.color = "red";
element.style.fontSize = "40px";
```

---

## Complete Example

```html
<!DOCTYPE html>
<html>
<body>

<h1 id="title">Hello</h1>

<button onclick="changeText()">
    Change Text
</button>

<script>

function changeText()
{
    let heading =
    document.getElementById("title");

    heading.innerText =
    "Text Changed Successfully";
}

</script>

</body>
</html>
```

---

# 2. getElementsByClassName()

Selects all elements having the same class.

## HTML

```html
<p class="info">Java</p>
<p class="info">Python</p>
<p class="info">JavaScript</p>
```

## JavaScript

```javascript
let elements =
document.getElementsByClassName("info");

console.log(elements);
```

Returns:

```javascript
HTMLCollection(3)
```

---

## Access Individual Element

```javascript
let elements =
document.getElementsByClassName("info");

console.log(elements[0]);
console.log(elements[1]);
console.log(elements[2]);
```

Output:

```html
<p>Java</p>
<p>Python</p>
<p>JavaScript</p>
```

---

## Change First Element

```javascript
elements[0].innerText =
"Spring Boot";
```

---

## Change All Elements

```javascript
let elements =
document.getElementsByClassName("info");

for(let i=0;i<elements.length;i++)
{
    elements[i].style.color = "blue";
}
```

---

## Complete Example

```html
<!DOCTYPE html>
<html>
<body>

<p class="info">Java</p>
<p class="info">Python</p>
<p class="info">JavaScript</p>

<button onclick="changeColor()">
Change Color
</button>

<script>

function changeColor()
{
    let elements =
    document.getElementsByClassName("info");

    for(let i=0;i<elements.length;i++)
    {
        elements[i].style.color="red";
    }
}

</script>

</body>
</html>
```

---

# 3. getElementsByTagName()

Selects elements by tag name.

## HTML

```html
<h2>Heading 1</h2>
<h2>Heading 2</h2>
<h2>Heading 3</h2>
```

## JavaScript

```javascript
let headings =
document.getElementsByTagName("h2");

console.log(headings);
```

Returns:

```javascript
HTMLCollection(3)
```

---

## Access Elements

```javascript
console.log(headings[0]);
console.log(headings[1]);
console.log(headings[2]);
```

---

## Change All Headings

```javascript
let headings =
document.getElementsByTagName("h2");

for(let i=0;i<headings.length;i++)
{
    headings[i].style.color="green";
}
```

---

## Example

```html
<h2>HTML</h2>
<h2>CSS</h2>
<h2>JS</h2>
```

```javascript
let h =
document.getElementsByTagName("h2");

for(let i=0;i<h.length;i++)
{
    h[i].innerText =
    "Frontend Technology";
}
```

Result:

```html
Frontend Technology
Frontend Technology
Frontend Technology
```

---

# Difference Between These Three

| Method                   | Selects           | Returns        |
| ------------------------ | ----------------- | -------------- |
| getElementById()         | Single Element    | Element        |
| getElementsByClassName() | Multiple Elements | HTMLCollection |
| getElementsByTagName()   | Multiple Elements | HTMLCollection |

---

# Important Interview Question

## What is HTMLCollection?

When using:

```javascript
document.getElementsByClassName()
```

or

```javascript
document.getElementsByTagName()
```

JavaScript returns:

```javascript
HTMLCollection
```

Example:

```javascript
let items =
document.getElementsByClassName("info");

console.log(items);
```

Output:

```javascript
HTMLCollection(3)
```

Access using index:

```javascript
items[0]
items[1]
items[2]
```

Loop through:

```javascript
for(let i=0;i<items.length;i++)
{
    console.log(items[i]);
}
```

---

# Real Project Example

Suppose you have a student list:

```html
<ul>
    <li class="student">Narendar</li>
    <li class="student">Rahul</li>
    <li class="student">Kiran</li>
</ul>
```

Select all students:

```javascript
let students =
document.getElementsByClassName("student");

for(let i=0;i<students.length;i++)
{
    students[i].style.background =
    "yellow";
}
```

Result:

```html
Narendar → Yellow
Rahul → Yellow
Kiran → Yellow
```

---


These are the selectors used in React, Angular, Vue, and modern JavaScript applications.
