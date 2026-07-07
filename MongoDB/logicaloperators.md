Yes. Using the **same `students` collection** (30 documents) that we created earlier, here is a complete **hands-on practice** for **MongoDB Logical Operators** (`$and`, `$or`, `$not`, `$nor`) based on your uploaded notes. 

---

# 1. Implicit AND (Default)

### Find Active Python students

```javascript
db.students.find({
    course: "Python",
    status: "Active"
})
```

---

### Students from Hyderabad with marks greater than 80

```javascript
db.students.find({
    city: "Hyderabad",
    marks: {
        $gt: 80
    }
})
```

---

### Java students whose fees are less than 32000

```javascript
db.students.find({
    course: "Java",
    fees: {
        $lt: 32000
    }
})
```

---

# 2. Explicit $and

### Active Python students

```javascript
db.students.find({
    $and: [
        { course: "Python" },
        { status: "Active" }
    ]
})
```

---

### Students aged above 21 and below 25

```javascript
db.students.find({
    $and: [
        {
            age: {
                $gt: 21
            }
        },
        {
            age: {
                $lt: 25
            }
        }
    ]
})
```

---

### Students with marks above 80 and fees below 30000

```javascript
db.students.find({
    $and: [
        {
            marks: {
                $gt: 80
            }
        },
        {
            fees: {
                $lt: 30000
            }
        }
    ]
})
```

---

### Students from Hyderabad, Active, and marks above 85

```javascript
db.students.find({
    $and: [
        { city: "Hyderabad" },
        { status: "Active" },
        {
            marks: {
                $gt: 85
            }
        }
    ]
})
```

---

# 3. OR Operator

### Students studying Python OR Java

```javascript
db.students.find({
    $or: [
        { course: "Python" },
        { course: "Java" }
    ]
})
```

---

### Students from Hyderabad OR Bangalore

```javascript
db.students.find({
    $or: [
        { city: "Hyderabad" },
        { city: "Bangalore" }
    ]
})
```

---

### Students with marks greater than 90 OR fees less than 25000

```javascript
db.students.find({
    $or: [
        {
            marks: {
                $gt: 90
            }
        },
        {
            fees: {
                $lt: 25000
            }
        }
    ]
})
```

---

### Active students who are from Hyderabad OR Pune

```javascript
db.students.find({
    status: "Active",
    $or: [
        { city: "Hyderabad" },
        { city: "Pune" }
    ]
})
```

---

# 4. NOT Operator

### Students whose marks are NOT greater than 80

```javascript
db.students.find({
    marks: {
        $not: {
            $gt: 80
        }
    }
})
```

---

### Students whose fees are NOT less than 30000

```javascript
db.students.find({
    fees: {
        $not: {
            $lt: 30000
        }
    }
})
```

---

### Students whose age is NOT greater than 22

```javascript
db.students.find({
    age: {
        $not: {
            $gt: 22
        }
    }
})
```

---

# 5. NOR Operator

### Students who are neither Python nor Java students

```javascript
db.students.find({
    $nor: [
        { course: "Python" },
        { course: "Java" }
    ]
})
```

---

### Students who are neither from Hyderabad nor Bangalore

```javascript
db.students.find({
    $nor: [
        { city: "Hyderabad" },
        { city: "Bangalore" }
    ]
})
```

---

### Students who are neither Active nor Completed

```javascript
db.students.find({
    $nor: [
        { status: "Active" },
        { status: "Completed" }
    ]
})
```

---

# 6. AND + OR

### Active students studying Python OR Java

```javascript
db.students.find({
    status: "Active",
    $or: [
        { course: "Python" },
        { course: "Java" }
    ]
})
```

---

### Students from Hyderabad whose marks are above 90 OR fees below 25000

```javascript
db.students.find({
    city: "Hyderabad",
    $or: [
        {
            marks: {
                $gt: 90
            }
        },
        {
            fees: {
                $lt: 25000
            }
        }
    ]
})
```

---

# 7. AND + NOR

### Active students excluding Java and MERN

```javascript
db.students.find({
    status: "Active",
    $nor: [
        { course: "Java" },
        { course: "MERN" }
    ]
})
```

---

### Hyderabad students excluding marks below 80

```javascript
db.students.find({
    city: "Hyderabad",
    $nor: [
        {
            marks: {
                $lt: 80
            }
        }
    ]
})
```

---

# 8. OR + NOT

### Python students OR students whose marks are NOT greater than 90

```javascript
db.students.find({
    $or: [
        { course: "Python" },
        {
            marks: {
                $not: {
                    $gt: 90
                }
            }
        }
    ]
})
```

---

# 9. Complex Query

### Active students

* from Hyderabad or Bangalore
* marks above 80
* fees below 35000
* not studying React

```javascript
db.students.find({
    status: "Active",
    marks: {
        $gt: 80
    },
    fees: {
        $lt: 35000
    },
    $or: [
        { city: "Hyderabad" },
        { city: "Bangalore" }
    ],
    course: {
        $ne: "React"
    }
})
```

---

# 10. Advanced Query

### Find students

* Python OR Java
* Marks above 80
* Fees between 20,000 and 30,000
* Status Active
* Not from Delhi

```javascript
db.students.find({
    status: "Active",
    course: {
        $in: ["Python", "Java"]
    },
    marks: {
        $gt: 80
    },
    fees: {
        $gte: 20000,
        $lte: 30000
    },
    city: {
        $ne: "Delhi"
    }
})
```

---

# Practice Questions (15)

1. Find Active students studying MERN or React.
2. Find students from Hyderabad or Chennai.
3. Find students whose marks are not greater than 85.
4. Find students who are neither from Delhi nor Mumbai.
5. Find Python students with fees below ₹25,000.
6. Find students aged between 21 and 24 using `$and`.
7. Find students with marks above 90 or fees below ₹24,000.
8. Find Active students excluding Java.
9. Find students who are not from Hyderabad.
10. Find Completed students with marks above 85.
11. Find students studying Java or Data Science.
12. Find students whose fees are not less than ₹30,000.
13. Find students who are neither Active nor Inactive.
14. Find students from Pune or Bangalore with marks above 80.
15. Find Active students from Hyderabad excluding React and NodeJS.

These exercises cover all logical operators discussed in your uploaded notes: **implicit AND, `$and`, `$or`, `$not`, `$nor`, and combinations of logical operators with comparison operators**. 
