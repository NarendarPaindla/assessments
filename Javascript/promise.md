
# Promises in JavaScript (Part 1)

In the previous lesson, we saw Callback Hell:

```javascript
getUser(function(user){

    getOrders(user.id,function(orders){

        getPayment(orders[0],function(payment){

            sendEmail(payment,function(result){

                console.log(result);

            });

        });

    });

});
```

Problems:

❌ Difficult to Read

❌ Difficult to Maintain

❌ Difficult to Debug

To solve this problem, JavaScript introduced:

# Promise

A Promise is an object that represents the eventual completion or failure of an asynchronous operation.

Simple English:

> "I promise I will give you a result later."

Example:

```text
You order food
      ↓
Restaurant is preparing
      ↓
Food delivered OR delivery failed
```

While food is preparing, the promise is still pending.

---

# Real Life Example

Imagine your friend says:

```text
I will give you ₹100 tomorrow.
```

Three possibilities:

### 1. Waiting

```text
Promise Pending
```

Friend hasn't come yet.

---

### 2. Success

```text
Promise Fulfilled
```

Friend gives ₹100.

---

### 3. Failure

```text
Promise Rejected
```

Friend lost wallet.

---

# Promise States

Every Promise has 3 states:

```text
Pending
   ↓
Fulfilled
```

OR

```text
Pending
   ↓
Rejected
```

Visualization:

```text
          Pending
          /     \
         /       \
 Fulfilled      Rejected
```

---

# Creating a Promise

Syntax:

```javascript
const promise = new Promise((resolve, reject) => {

});
```

Two special functions are provided:

```javascript
resolve()
reject()
```

---

# What is resolve()?

Used when operation succeeds.

Example:

```javascript
const promise = new Promise((resolve, reject) => {

    resolve("Success");

});
```

---

# What is reject()?

Used when operation fails.

Example:

```javascript
const promise = new Promise((resolve, reject) => {

    reject("Failed");

});
```

---

# First Promise Example

```javascript
const myPromise = new Promise((resolve, reject) => {

    resolve("Data Loaded");

});

console.log(myPromise);
```

Output:

```javascript
Promise { 'Data Loaded' }
```

Internally:

```text
Pending
   ↓
Resolved
```

---

# Consuming a Promise

Creating promise alone is useless.

Need to receive result.

Use:

```javascript
.then()
```

---

# then()

Used when Promise succeeds.

Example:

```javascript
const myPromise = new Promise((resolve, reject) => {

    resolve("Data Loaded");

});

myPromise.then((data) => {

    console.log(data);

});
```

Output:

```javascript
Data Loaded
```

---

# Flow

```text
Promise Created
       ↓
resolve("Data Loaded")
       ↓
then() executes
       ↓
Data Loaded
```

---

# Another Example

```javascript
const promise = new Promise((resolve, reject) => {

    resolve(100);

});

promise.then((value) => {

    console.log(value);

});
```

Output:

```javascript
100
```

---

# Passing Objects

```javascript
const promise = new Promise((resolve, reject) => {

    resolve({
        id:1,
        name:"Narendar"
    });

});
```

Receiving:

```javascript
promise.then((user)=>{

    console.log(user);

});
```

Output:

```javascript
{
 id:1,
 name:"Narendar"
}
```

---

# Rejecting a Promise

Example:

```javascript
const promise = new Promise((resolve,reject)=>{

    reject("Server Error");

});
```

To handle rejection:

```javascript
.catch()
```

---

# catch()

Used when Promise fails.

Example:

```javascript
const promise = new Promise((resolve,reject)=>{

    reject("Server Error");

});

promise.catch((error)=>{

    console.log(error);

});
```

Output:

```javascript
Server Error
```

---

# Flow

```text
Promise Created
       ↓
reject()
       ↓
catch()
       ↓
Error Handled
```

---

# Success + Failure Together

Example:

```javascript
const isSuccess = true;

const promise = new Promise((resolve,reject)=>{

    if(isSuccess){
        resolve("Login Successful");
    }
    else{
        reject("Invalid Credentials");
    }

});
```

Handling:

```javascript
promise
.then((data)=>{
    console.log(data);
})
.catch((error)=>{
    console.log(error);
});
```

Output:

```javascript
Login Successful
```

or

```javascript
Invalid Credentials
```

depending on condition.

---

# Simulating API Calls

Real APIs take time.

Let's simulate with setTimeout.

```javascript
const promise = new Promise((resolve,reject)=>{

    setTimeout(()=>{

        resolve("Data Received");

    },2000);

});
```

Consume:

```javascript
promise.then((data)=>{

    console.log(data);

});
```

Output after 2 seconds:

```javascript
Data Received
```

---

# Visual Flow

```text
Promise Created
      ↓
Waiting 2 Seconds
      ↓
resolve()
      ↓
then()
      ↓
Data Received
```

---

# Simulated User API

```javascript
function fetchUser(){

    return new Promise((resolve,reject)=>{

        setTimeout(()=>{

            resolve({
                id:1,
                name:"Narendar"
            });

        },2000);

    });

}
```

Usage:

```javascript
fetchUser()
.then((user)=>{

    console.log(user);

});
```

Output:

```javascript
{
 id:1,
 name:"Narendar"
}
```

---

# Why Promise is Better than Callback

### Callback Version

```javascript
fetchUser(function(user){

    console.log(user);

});
```

### Promise Version

```javascript
fetchUser()
.then((user)=>{

    console.log(user);

});
```

Cleaner.

More maintainable.

---

# then() Receives Returned Value

Example:

```javascript
const promise = new Promise((resolve,reject)=>{

    resolve(10);

});

promise.then((value)=>{

    console.log(value);

});
```

Output:

```javascript
10
```

The value passed into `resolve()` automatically comes into `.then()`.

---

# Interview Question

### Is this correct?

```javascript
resolve();
```

Yes.

Example:

```javascript
const promise = new Promise((resolve,reject)=>{

    resolve();

});
```

Then:

```javascript
promise.then(()=>{
    console.log("Done");
});
```

Output:

```javascript
Done
```

---

# Practice Questions

### Q1

Predict output:

```javascript
const promise = new Promise((resolve,reject)=>{

    resolve("Hello");

});

promise.then((data)=>{
    console.log(data);
});
```

---

### Q2

Predict output:

```javascript
const promise = new Promise((resolve,reject)=>{

    reject("Error");

});

promise.catch((err)=>{
    console.log(err);
});
```

---

### Q3

Create a Promise that resolves after 5 seconds with:

```javascript
"Welcome Narendar"
```

and print it using `.then()`.

---


# Promise Chaining, Error Propagation, and finally()

In the previous lesson, we learned:

```javascript
const promise = new Promise((resolve, reject) => {
    resolve("Success");
});

promise.then((data) => {
    console.log(data);
});
```

Now let's learn the real power of Promises.

---

# What is Promise Chaining?

A Promise chain means:

```javascript
promise
.then()
.then()
.then()
.catch()
```

Each `.then()` receives the result from the previous `.then()`.

Think of it like a factory assembly line:

```text
Raw Material
      ↓
Process 1
      ↓
Process 2
      ↓
Process 3
      ↓
Finished Product
```

---

# Example 1: Simple Chaining

```javascript
Promise.resolve(10)
.then((value) => {
    return value + 5;
})
.then((value) => {
    return value * 2;
})
.then((value) => {
    console.log(value);
});
```

Output:

```javascript
30
```

---

## Step-by-Step Execution

### Step 1

```javascript
Promise.resolve(10)
```

Value:

```javascript
10
```

---

### Step 2

```javascript
.then((value) => {
    return value + 5;
})
```

Returns:

```javascript
15
```

---

### Step 3

```javascript
.then((value) => {
    return value * 2;
})
```

Returns:

```javascript
30
```

---

### Step 4

```javascript
.then((value) => {
    console.log(value);
})
```

Prints:

```javascript
30
```

---

# Visualization

```text
10
 ↓
+5
 ↓
15
 ↓
×2
 ↓
30
 ↓
Print
```

---

# Important Rule

Whatever you return from a `.then()`

becomes the input of the next `.then()`.

Example:

```javascript
Promise.resolve(5)
.then((num)=>{
    return num + 10;
})
.then((num)=>{
    console.log(num);
});
```

Output:

```javascript
15
```

---

# Example 2

```javascript
Promise.resolve("Hello")
.then((text)=>{
    return text + " Narendar";
})
.then((text)=>{
    return text.toUpperCase();
})
.then((text)=>{
    console.log(text);
});
```

Output:

```javascript
HELLO NARENDAR
```

---

# Returning Objects

```javascript
Promise.resolve({
    name:"Narendar"
})
.then((user)=>{
    return {
        ...user,
        age:25
    };
})
.then((user)=>{
    console.log(user);
});
```

Output:

```javascript
{
  name:"Narendar",
  age:25
}
```

---

# Real API Style Example

Imagine:

```text
Get User
    ↓
Get Orders
    ↓
Get Payment
```

---

## Step 1

```javascript
function getUser(){

    return Promise.resolve({
        id:1,
        name:"Narendar"
    });

}
```

---

## Step 2

```javascript
function getOrders(userId){

    return Promise.resolve([
        "Laptop",
        "Mobile"
    ]);

}
```

---

## Usage

```javascript
getUser()
.then((user)=>{

    console.log(user);

    return getOrders(user.id);

})
.then((orders)=>{

    console.log(orders);

});
```

Output:

```javascript
{ id:1, name:"Narendar" }

["Laptop","Mobile"]
```

---

# Why Return?

Wrong:

```javascript
getUser()
.then((user)=>{

    getOrders(user.id);

})
.then((orders)=>{

    console.log(orders);

});
```

Output:

```javascript
undefined
```

because:

```javascript
getOrders(user.id);
```

is not returned.

---

# Correct

```javascript
return getOrders(user.id);
```

Always remember:

```text
If next .then() needs data
↓
Return it
```

---

# Promise Returning Another Promise

Very important.

Example:

```javascript
Promise.resolve(10)
.then((value)=>{

    return Promise.resolve(value * 2);

})
.then((value)=>{

    console.log(value);

});
```

Output:

```javascript
20
```

JavaScript automatically unwraps the Promise.

---

# Error Handling

Suppose:

```javascript
const promise = new Promise((resolve,reject)=>{

    reject("Server Error");

});
```

Handle:

```javascript
promise.catch((error)=>{

    console.log(error);

});
```

Output:

```javascript
Server Error
```

---

# Error Propagation

Huge interview topic.

Example:

```javascript
Promise.resolve(10)
.then((value)=>{

    throw new Error("Something Wrong");

})
.catch((error)=>{

    console.log(error.message);

});
```

Output:

```javascript
Something Wrong
```

---

# Why Did catch Work?

Because:

```javascript
throw new Error()
```

automatically converts to:

```javascript
reject()
```

---

# Visualization

```text
then()
   ↓
Error Thrown
   ↓
catch()
```

---

# Multiple then() with Error

```javascript
Promise.resolve(10)
.then((value)=>{

    return value * 2;

})
.then((value)=>{

    throw new Error("Failed");

})
.then((value)=>{

    console.log(value);

})
.catch((error)=>{

    console.log(error.message);

});
```

Output:

```javascript
Failed
```

Notice:

```javascript
.then((value)=>{
    console.log(value);
});
```

never runs.

Because execution jumps directly to:

```javascript
catch()
```

---

# Error Anywhere in Chain

```javascript
Promise.resolve()
.then(()=>{
    throw new Error("Error 1");
})
.then(()=>{
    console.log("A");
})
.then(()=>{
    console.log("B");
})
.catch((error)=>{
    console.log(error.message);
});
```

Output:

```javascript
Error 1
```

Everything after error is skipped.

---

# finally()

Very important in real projects.

Runs whether success or failure.

Syntax:

```javascript
promise
.then(...)
.catch(...)
.finally(...);
```

---

# Success Example

```javascript
Promise.resolve("Success")
.then((data)=>{

    console.log(data);

})
.finally(()=>{

    console.log("Completed");

});
```

Output:

```javascript
Success
Completed
```

---

# Failure Example

```javascript
Promise.reject("Error")
.catch((error)=>{

    console.log(error);

})
.finally(()=>{

    console.log("Completed");

});
```

Output:

```javascript
Error
Completed
```

---

# Why Use finally()?

Suppose API call.

Show loader:

```javascript
showLoader();
```

API request:

```javascript
fetchData()
```

Hide loader:

```javascript
hideLoader();
```

Whether success or failure:

```javascript
fetchData()
.then(...)
.catch(...)
.finally(()=>{
    hideLoader();
});
```

This is extremely common in React applications.

---

# Converting Callback Hell to Promises

### Callback Hell

```javascript
getUser(function(user){

    getOrders(user.id,function(orders){

        getPayment(orders[0],function(payment){

            console.log(payment);

        });

    });

});
```

---

### Promise Version

```javascript
getUser()
.then((user)=>{

    return getOrders(user.id);

})
.then((orders)=>{

    return getPayment(orders[0]);

})
.then((payment)=>{

    console.log(payment);

})
.catch((error)=>{

    console.log(error);

});
```

Much cleaner.

---

# Interview Question

### Difference Between

```javascript
return value;
```

and

```javascript
console.log(value);
```

Inside `.then()`

### Example

```javascript
Promise.resolve(10)
.then((value)=>{
    console.log(value);
})
.then((value)=>{
    console.log(value);
});
```

Output:

```javascript
10
undefined
```

Why?

Because:

```javascript
console.log(value);
```

returns:

```javascript
undefined
```

---

Correct:

```javascript
Promise.resolve(10)
.then((value)=>{
    return value;
})
.then((value)=>{
    console.log(value);
});
```

Output:

```javascript
10
```

---

# Practice Questions

### Q1

Predict Output

```javascript
Promise.resolve(5)
.then((num)=>{
    return num * 2;
})
.then((num)=>{
    return num + 10;
})
.then((num)=>{
    console.log(num);
});
```

---

### Q2

Predict Output

```javascript
Promise.resolve()
.then(()=>{
    throw new Error("Oops");
})
.catch((err)=>{
    console.log(err.message);
});
```

---

### Q3

Predict Output

```javascript
Promise.resolve("Hello")
.finally(()=>{
    console.log("Done");
})
.then((data)=>{
    console.log(data);
});
```

---

