## What is Destructuring in JavaScript?

**Destructuring** is a JavaScript feature that lets you extract values from arrays or properties from objects into variables in a clean and readable way.

---

# 1. Array Destructuring

Instead of:

```js
const numbers = [10, 20, 30];

const first = numbers[0];
const second = numbers[1];
```

You can write:

```js
const numbers = [10, 20, 30];

const [first, second] = numbers;

console.log(first);  // 10
console.log(second); // 20
```

---

## Skipping Values

```js
const colors = ["red", "green", "blue"];

const [first, , third] = colors;

console.log(first); // red
console.log(third); // blue
```

---

## Default Values

```js
const [a = 5, b = 10] = [1];

console.log(a); // 1
console.log(b); // 10
```

---

## Rest Operator

```js
const [x, ...rest] = [1, 2, 3, 4];

console.log(x);    // 1
console.log(rest); // [2, 3, 4]
```

---

# 2. Object Destructuring

Instead of:

```js
const user = {
  name: "John",
  age: 25
};

const name = user.name;
const age = user.age;
```

You can write:

```js
const user = {
  name: "John",
  age: 25
};

const { name, age } = user;

console.log(name); // John
console.log(age);  // 25
```

---

## Renaming Variables

```js
const user = {
  name: "Alice",
  age: 22
};

const { name: userName, age: userAge } = user;

console.log(userName); // Alice
console.log(userAge);  // 22
```

---

## Default Values

```js
const { country = "USA" } = {};

console.log(country); // USA
```

---

# 3. Nested Destructuring

```js
const person = {
  name: "Tom",
  address: {
    city: "New York"
  }
};

const {
  address: { city }
} = person;

console.log(city); // New York
```

---

# 4. Destructuring in Function Parameters

```js
function displayUser({ name, age }) {
  console.log(`${name} is ${age} years old`);
}

displayUser({
  name: "Emma",
  age: 28
});
```

---

# Why Use Destructuring?

✅ Cleaner code
✅ Less repetition
✅ Easier to read
✅ Very useful with APIs and React props

---

# Real-World Example

```js
const response = {
  status: 200,
  data: {
    id: 1,
    title: "JavaScript Basics"
  }
};

const {
  data: { title }
} = response;

console.log(title); // JavaScript Basics
```

---

# Summary

| Type                 | Syntax                     |
| -------------------- | -------------------------- |
| Array Destructuring  | `const [a, b] = arr`       |
| Object Destructuring | `const {x, y} = obj`       |
| Rename Variable      | `const {x: newName} = obj` |
| Default Value        | `const {x = 10} = obj`     |
| Rest Operator        | `const [a, ...rest] = arr` |

Great question.

## Why Do We Need Destructuring?

Without destructuring, accessing data from arrays and objects becomes repetitive and harder to read.

---

# 1. Reduce Repetitive Code

### Without Destructuring

```js
const user = {
  name: "Narendar",
  age: 24,
  city: "Hyderabad"
};

const name = user.name;
const age = user.age;
const city = user.city;

console.log(name);
console.log(age);
console.log(city);
```

Here, we repeatedly write `user.`.

### With Destructuring

```js
const user = {
  name: "Narendar",
  age: 24,
  city: "Hyderabad"
};

const { name, age, city } = user;

console.log(name);
console.log(age);
console.log(city);
```

Less code and easier to read.

---

# 2. Easier to Work with Arrays

### Without Destructuring

```js
const colors = ["red", "green", "blue"];

const first = colors[0];
const second = colors[1];

console.log(first);
console.log(second);
```

### With Destructuring

```js
const colors = ["red", "green", "blue"];

const [first, second] = colors;

console.log(first);
console.log(second);
```

Much cleaner.

---

# 3. Useful in Function Parameters

Imagine a function receives an object.

### Without Destructuring

```js
function displayUser(user) {
  console.log(user.name);
  console.log(user.age);
}

displayUser({
  name: "John",
  age: 25
});
```

### With Destructuring

```js
function displayUser({ name, age }) {
  console.log(name);
  console.log(age);
}

displayUser({
  name: "John",
  age: 25
});
```

Direct access to the required properties.

---

# 4. Frequently Used in React

### Without Destructuring

```js
function User(props) {
  return <h1>{props.name}</h1>;
}
```

### With Destructuring

```js
function User({ name }) {
  return <h1>{name}</h1>;
}
```

Almost every React project uses destructuring.

---

# 5. Working with API Responses

Suppose an API returns:

```js
const response = {
  data: {
    id: 1,
    name: "Laptop",
    price: 50000
  }
};
```

### Without Destructuring

```js
console.log(response.data.name);
console.log(response.data.price);
```

### With Destructuring

```js
const {
  data: { name, price }
} = response;

console.log(name);
console.log(price);
```

Cleaner when handling large API responses.

---

# 6. Swapping Variables Easily

### Without Destructuring

```js
let a = 10;
let b = 20;

let temp = a;
a = b;
b = temp;

console.log(a, b);
```

### With Destructuring

```js
let a = 10;
let b = 20;

[a, b] = [b, a];

console.log(a, b);
```

Very concise.

---

# Real Reason

Destructuring was introduced because JavaScript applications deal with lots of:

* Objects
* Arrays
* API responses
* Function arguments
* React props
* Database records

Instead of writing:

```js
user.name
user.age
user.email
user.city
```

again and again, we can do:

```js
const { name, age, email, city } = user;
```

and use the variables directly.

---

## Interview Answer

**"Destructuring is used to extract values from arrays and properties from objects into separate variables in a concise and readable way. It reduces repetitive code, improves readability, and is commonly used when working with API responses, function parameters, and React props."**

