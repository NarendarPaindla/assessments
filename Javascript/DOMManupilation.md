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


# Modern Selectors

In modern JavaScript, developers mostly use:

```javascript
querySelector()
querySelectorAll()
```

Because they can select elements using **CSS selectors**, making them very powerful and flexible.

---

# 4. querySelector()

Selects the **first matching element only**.

### Syntax

```javascript
document.querySelector("css-selector")
```

Returns:

```javascript
Single Element
```

---

# Selecting by ID

## HTML

```html
<h1 id="title">Welcome</h1>
```

## JavaScript

```javascript
let heading =
document.querySelector("#title");

console.log(heading);
```

### Output

```html
<h1 id="title">Welcome</h1>
```

Notice:

```javascript
# → ID selector
```

Just like CSS:

```css
#title{
    color:red;
}
```

---

## Change Text

```javascript
let heading =
document.querySelector("#title");

heading.innerText =
"DOM Manipulation";
```

---

# Selecting by Class

## HTML

```html
<p class="info">Java</p>
```

## JavaScript

```javascript
let element =
document.querySelector(".info");

console.log(element);
```

Output:

```html
<p class="info">Java</p>
```

Notice:

```javascript
. → class selector
```

---

# Selecting by Tag

## HTML

```html
<h2>Hello</h2>
```

## JavaScript

```javascript
let heading =
document.querySelector("h2");
```

---

# Example

```html
<h2>HTML</h2>
<h2>CSS</h2>
<h2>JS</h2>
```

```javascript
let heading =
document.querySelector("h2");

heading.style.color="red";
```

Only first element changes:

```html
HTML ← Red
CSS
JS
```

Because querySelector selects:

```javascript
FIRST MATCH ONLY
```

---

# Real Project Example

```html
<input id="username">
```

```javascript
let input =
document.querySelector("#username");

input.value="Narendar";
```

Result:

```html
Narendar
```

---

# 5. querySelectorAll()

Selects ALL matching elements.

### Syntax

```javascript
document.querySelectorAll("css-selector")
```

Returns:

```javascript
NodeList
```

---

## HTML

```html
<p class="info">Java</p>
<p class="info">Python</p>
<p class="info">JS</p>
```

## JavaScript

```javascript
let elements =
document.querySelectorAll(".info");

console.log(elements);
```

Output:

```javascript
NodeList(3)
```

---

# Access Elements

```javascript
console.log(elements[0]);
console.log(elements[1]);
console.log(elements[2]);
```

---

# Change All Elements

```javascript
let elements =
document.querySelectorAll(".info");

for(let i=0;i<elements.length;i++)
{
    elements[i].style.color="blue";
}
```

Result:

```html
Java      ← Blue
Python    ← Blue
JS        ← Blue
```

---

# forEach() With querySelectorAll()

Very common in projects.

```javascript
let elements =
document.querySelectorAll(".info");

elements.forEach(function(item)
{
    item.style.color="green";
});
```

Modern version:

```javascript
elements.forEach(item =>
{
    item.style.color="green";
});
```

---

# Difference

## querySelector()

```javascript
document.querySelector(".info")
```

Returns:

```javascript
FIRST MATCH
```

---

## querySelectorAll()

```javascript
document.querySelectorAll(".info")
```

Returns:

```javascript
ALL MATCHES
```

---

# CSS Selectors Inside JavaScript

The biggest advantage of querySelector and querySelectorAll.

---

# 1. ID Selector

HTML

```html
<h1 id="title">Hello</h1>
```

JavaScript

```javascript
document.querySelector("#title");
```

---

# 2. Class Selector

HTML

```html
<p class="info">Java</p>
```

JavaScript

```javascript
document.querySelector(".info");
```

---

# 3. Tag Selector

HTML

```html
<h2>Hello</h2>
```

JavaScript

```javascript
document.querySelector("h2");
```

---

# 4. Multiple Classes

HTML

```html
<p class="info active">
    Java
</p>
```

JavaScript

```javascript
document.querySelector(".info.active");
```

Meaning:

```javascript
Must contain BOTH classes
```

---

# 5. Select All Buttons

HTML

```html
<button>Save</button>
<button>Edit</button>
<button>Delete</button>
```

JavaScript

```javascript
let buttons =
document.querySelectorAll("button");
```

---

# 6. Select All Inputs

HTML

```html
<input>
<input>
<input>
```

JavaScript

```javascript
let inputs =
document.querySelectorAll("input");
```

---

# Example Project

```html
<input type="text">
<input type="email">
<input type="password">
```

```javascript
let inputs =
document.querySelectorAll("input");

inputs.forEach(input =>
{
    input.style.border =
    "2px solid green";
});
```

---

# Descendant Selector

Select element inside another element.

HTML

```html
<div class="container">

    <h1>Title</h1>

</div>
```

JavaScript

```javascript
document.querySelector(
".container h1"
);
```

Meaning:

```javascript
Select h1 inside container
```

Equivalent CSS:

```css
.container h1
```

---

# Example

```html
<div class="card">
    <h2>Product</h2>
</div>
```

```javascript
let heading =
document.querySelector(".card h2");
```

---

# Child Selector (>)

Select direct child only.

HTML

```html
<div class="parent">

    <h1>Direct Child</h1>

</div>
```

JavaScript

```javascript
document.querySelector(
".parent > h1"
);
```

Meaning:

```javascript
Direct child only
```

---

# Summary

| Selector           | Description           |
| ------------------ | --------------------- |
| #id                | Select by ID          |
| .class             | Select by Class       |
| tag                | Select by Tag         |
| parent child       | Descendant Selector   |
| parent > child     | Direct Child Selector |
| querySelector()    | First Match           |
| querySelectorAll() | All Matches           |

---

### Most Used Selectors in Real Projects

```javascript
document.querySelector("#id")

document.querySelector(".class")

document.querySelector("input")

document.querySelectorAll(".card")

document.querySelector(".container button")

document.querySelector(".form input")
```


