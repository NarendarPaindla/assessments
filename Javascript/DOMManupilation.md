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

---

# 1. innerText

Used to get or set the visible text of an element.

## HTML

```html
<h1 id="heading">
    Welcome to JavaScript
</h1>
```

## JavaScript

### Read Text

```javascript
let heading =
document.getElementById("heading");

console.log(heading.innerText);
```

Output:

```text
Welcome to JavaScript
```

---

### Change Text

```javascript
heading.innerText =
"DOM Manipulation";
```

Result:

```html
<h1>DOM Manipulation</h1>
```

---

## Complete Example

```html
<!DOCTYPE html>
<html>
<body>

<h1 id="title">Hello User</h1>

<button onclick="changeText()">
Change Text
</button>

<script>

function changeText()
{
    document.getElementById("title")
    .innerText =
    "Welcome Narendar";
}

</script>

</body>
</html>
```

---

# 2. textContent

Very similar to innerText.

Difference:

```javascript
innerText
```

Returns only visible text.

```javascript
textContent
```

Returns all text including hidden text.

---

## HTML

```html
<div id="box">
    Hello
    <span style="display:none">
        Hidden
    </span>
</div>
```

---

### innerText

```javascript
console.log(
document.getElementById("box")
.innerText
);
```

Output:

```text
Hello
```

---

### textContent

```javascript
console.log(
document.getElementById("box")
.textContent
);
```

Output:

```text
Hello Hidden
```

---

# Interview Question

### innerText vs textContent

| innerText         | textContent |
| ----------------- | ----------- |
| Visible text only | All text    |
| Slower            | Faster      |
| Considers CSS     | Ignores CSS |

---

# 3. innerHTML

Most powerful and dangerous.

Allows adding HTML tags dynamically.

---

## HTML

```html
<div id="content"></div>
```

---

## JavaScript

```javascript
document.getElementById("content")
.innerHTML =
"<h1>Hello</h1>";
```

Result:

```html
<div>
    <h1>Hello</h1>
</div>
```

Browser renders actual HTML.

---

## Example

```javascript
document.getElementById("content")
.innerHTML =
`
<h2>Java</h2>
<p>Programming Language</p>
`;
```

Output:

```html
Java
Programming Language
```

---

# innerText vs innerHTML

### innerText

```javascript
element.innerText =
"<h1>Hello</h1>";
```

Output:

```text
<h1>Hello</h1>
```

Displays plain text.

---

### innerHTML

```javascript
element.innerHTML =
"<h1>Hello</h1>";
```

Output:

```html
Hello
```

Creates actual HTML.

---

# Example

```html
<!DOCTYPE html>
<html>
<body>

<div id="box"></div>

<button onclick="loadContent()">
Load
</button>

<script>

function loadContent()
{
    document.getElementById("box")
    .innerHTML =
    `
    <h2>JavaScript</h2>
    <p>Learning DOM</p>
    `;
}

</script>

</body>
</html>
```

---

# 4. outerHTML

Replaces entire element.

---

## HTML

```html
<h1 id="heading">
Welcome
</h1>
```

---

## JavaScript

```javascript
document.getElementById("heading")
.outerHTML =
"<p>Hello User</p>";
```

Result:

```html
<p>Hello User</p>
```

Original h1 completely removed.

---

# Example

Before:

```html
<h1>Welcome</h1>
```

After:

```html
<p>Hello</p>
```

---

# 5. value Property

Used with:

```html
input
textarea
select
```

---

## HTML

```html
<input id="username">
```

---

### Read Value

```javascript
let value =
document.getElementById("username")
.value;

console.log(value);
```

---

### Set Value

```javascript
document.getElementById("username")
.value =
"Narendar";
```

---

## Complete Example

```html
<input id="name">

<button onclick="showName()">
Show
</button>

<script>

function showName()
{
    let name =
    document.getElementById("name")
    .value;

    alert(name);
}

</script>
```

---

# 6. setAttribute()

Used to add/update attributes.

---

## HTML

```html
<img id="image">
```

---

## JavaScript

```javascript
document.getElementById("image")
.setAttribute(
"src",
"image.jpg"
);
```

Result:

```html
<img src="image.jpg">
```

---

# Multiple Examples

```javascript
element.setAttribute(
"class",
"active"
);

element.setAttribute(
"href",
"https://google.com"
);

element.setAttribute(
"placeholder",
"Enter Name"
);
```

---

# 7. getAttribute()

Gets attribute value.

---

## HTML

```html
<a
id="link"
href="https://google.com">
Google
</a>
```

---

## JavaScript

```javascript
let url =
document.getElementById("link")
.getAttribute("href");

console.log(url);
```

Output:

```text
https://google.com
```

---

# 8. removeAttribute()

Removes attribute.

---

## HTML

```html
<input
id="email"
required>
```

---

## JavaScript

```javascript
document.getElementById("email")
.removeAttribute(
"required"
);
```

Result:

```html
<input id="email">
```

---

# 9. style Property

Changes CSS using JavaScript.

---

## HTML

```html
<h1 id="title">
JavaScript
</h1>
```

---

## JavaScript

```javascript
let title =
document.getElementById("title");

title.style.color="red";

title.style.backgroundColor=
"yellow";

title.style.fontSize=
"40px";
```

---

# Example

```javascript
title.style.border =
"2px solid black";

title.style.padding =
"20px";
```

---

# 10. className

Replace class completely.

---

## HTML

```html
<h1 class="old">
Hello
</h1>
```

---

## JavaScript

```javascript
document.querySelector("h1")
.className =
"newClass";
```

Result:

```html
<h1 class="newClass">
Hello
</h1>
```

---

# 11. classList

Modern and most used approach.

---

## Add Class

```javascript
element.classList.add(
"active"
);
```

---

## Remove Class

```javascript
element.classList.remove(
"active"
);
```

---

## Toggle Class

```javascript
element.classList.toggle(
"active"
);
```

If class exists:

```javascript
active removed
```

If class doesn't exist:

```javascript
active added
```

---

## Check Class

```javascript
element.classList.contains(
"active"
);
```

Returns:

```javascript
true
false
```

---

# Real Project Example

## Dark Mode

### HTML

```html
<button id="themeBtn">
Toggle Theme
</button>
```

### CSS

```css
.dark
{
    background:black;
    color:white;
}
```

### JavaScript

```javascript
let btn =
document.getElementById("themeBtn");

btn.addEventListener(
"click",
function()
{
    document.body.classList
    .toggle("dark");
});
```

---




