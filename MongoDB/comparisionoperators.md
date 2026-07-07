Based on the uploaded topic, which covers **MongoDB Comparison Operators** (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`) , the best way to learn is with a realistic dataset and hands-on exercises.

---

# Step 1: Create Database

```javascript
use StudentDB
```

---

# Step 2: Create Collection

```javascript
db.createCollection("students")
```

---

# Step 3: Insert 30 Student Documents

```javascript
db.students.insertMany([
{name:"Rahul",age:21,course:"Python",fees:25000,city:"Hyderabad",status:"Active",marks:85},
{name:"Priya",age:22,course:"Java",fees:30000,city:"Bangalore",status:"Inactive",marks:90},
{name:"Arjun",age:20,course:"MERN",fees:35000,city:"Chennai",status:"Active",marks:76},
{name:"Sneha",age:23,course:"Python",fees:25000,city:"Delhi",status:"Completed",marks:95},
{name:"Vikram",age:24,course:"Java",fees:28000,city:"Mumbai",status:"Active",marks:82},
{name:"Anjali",age:19,course:"Data Science",fees:40000,city:"Hyderabad",status:"Active",marks:88},
{name:"Kiran",age:25,course:"Python",fees:22000,city:"Pune",status:"Inactive",marks:72},
{name:"Ravi",age:22,course:"MERN",fees:36000,city:"Chennai",status:"Completed",marks:91},
{name:"Meena",age:21,course:"Java",fees:31000,city:"Delhi",status:"Active",marks:79},
{name:"Suresh",age:26,course:"Python",fees:26000,city:"Hyderabad",status:"Completed",marks:84},
{name:"Divya",age:20,course:"React",fees:27000,city:"Mumbai",status:"Active",marks:87},
{name:"Tarun",age:24,course:"NodeJS",fees:33000,city:"Bangalore",status:"Inactive",marks:68},
{name:"Pooja",age:23,course:"Python",fees:24000,city:"Hyderabad",status:"Active",marks:92},
{name:"Harish",age:22,course:"Java",fees:29000,city:"Chennai",status:"Completed",marks:81},
{name:"Lakshmi",age:21,course:"MERN",fees:35000,city:"Pune",status:"Active",marks:74},
{name:"Naveen",age:27,course:"Python",fees:23000,city:"Delhi",status:"Inactive",marks:66},
{name:"Keerthi",age:20,course:"Java",fees:31000,city:"Hyderabad",status:"Completed",marks:94},
{name:"Gopi",age:24,course:"Data Science",fees:45000,city:"Mumbai",status:"Active",marks:89},
{name:"Bhavana",age:23,course:"Python",fees:26000,city:"Bangalore",status:"Active",marks:78},
{name:"Sai",age:22,course:"React",fees:28000,city:"Hyderabad",status:"Completed",marks:83},
{name:"Lokesh",age:21,course:"NodeJS",fees:32000,city:"Delhi",status:"Inactive",marks:71},
{name:"Chaitra",age:24,course:"Python",fees:24000,city:"Pune",status:"Active",marks:96},
{name:"Manoj",age:25,course:"Java",fees:30000,city:"Mumbai",status:"Completed",marks:75},
{name:"Anusha",age:22,course:"Data Science",fees:43000,city:"Hyderabad",status:"Active",marks:93},
{name:"Deepak",age:20,course:"Python",fees:22000,city:"Chennai",status:"Inactive",marks:69},
{name:"Swathi",age:23,course:"MERN",fees:34000,city:"Bangalore",status:"Completed",marks:86},
{name:"Ajay",age:24,course:"Java",fees:31000,city:"Delhi",status:"Active",marks:77},
{name:"Nikhil",age:21,course:"React",fees:27000,city:"Hyderabad",status:"Completed",marks:80},
{name:"Ramesh",age:26,course:"Python",fees:25000,city:"Mumbai",status:"Active",marks:91},
{name:"Kavya",age:22,course:"Data Science",fees:42000,city:"Pune",status:"Completed",marks:97}
])
```

---

# Hands-on 1: Equality ($eq)

### Find students whose course is Python

```javascript
db.students.find({course:"Python"})
```

Using `$eq`

```javascript
db.students.find({
    course:{
        $eq:"Python"
    }
})
```

---

### Find students from Hyderabad

```javascript
db.students.find({
    city:{
        $eq:"Hyderabad"
    }
})
```

---

### Find Active students

```javascript
db.students.find({
    status:{
        $eq:"Active"
    }
})
```

---

# Hands-on 2: Not Equal ($ne)

### Students not studying Python

```javascript
db.students.find({
    course:{
        $ne:"Python"
    }
})
```

---

### Students not from Hyderabad

```javascript
db.students.find({
    city:{
        $ne:"Hyderabad"
    }
})
```

---

### Students not Active

```javascript
db.students.find({
    status:{
        $ne:"Active"
    }
})
```

---

# Hands-on 3: Greater Than ($gt)

### Age greater than 22

```javascript
db.students.find({
    age:{
        $gt:22
    }
})
```

---

### Fees greater than 30000

```javascript
db.students.find({
    fees:{
        $gt:30000
    }
})
```

---

### Marks greater than 90

```javascript
db.students.find({
    marks:{
        $gt:90
    }
})
```

---

# Hands-on 4: Greater Than Equal ($gte)

### Age >=22

```javascript
db.students.find({
    age:{
        $gte:22
    }
})
```

---

### Fees >=30000

```javascript
db.students.find({
    fees:{
        $gte:30000
    }
})
```

---

### Marks >=85

```javascript
db.students.find({
    marks:{
        $gte:85
    }
})
```

---

# Hands-on 5: Less Than ($lt)

### Age less than 22

```javascript
db.students.find({
    age:{
        $lt:22
    }
})
```

---

### Fees less than 30000

```javascript
db.students.find({
    fees:{
        $lt:30000
    }
})
```

---

### Marks less than 80

```javascript
db.students.find({
    marks:{
        $lt:80
    }
})
```

---

# Hands-on 6: Less Than Equal ($lte)

### Age <=22

```javascript
db.students.find({
    age:{
        $lte:22
    }
})
```

---

### Fees <=25000

```javascript
db.students.find({
    fees:{
        $lte:25000
    }
})
```

---

### Marks <=75

```javascript
db.students.find({
    marks:{
        $lte:75
    }
})
```

---

# Hands-on 7: Range Queries

### Students aged between 21 and 24

```javascript
db.students.find({
    age:{
        $gte:21,
        $lte:24
    }
})
```

---

### Fees between 25000 and 35000

```javascript
db.students.find({
    fees:{
        $gte:25000,
        $lte:35000
    }
})
```

---

### Marks between 80 and 90

```javascript
db.students.find({
    marks:{
        $gte:80,
        $lte:90
    }
})
```

---

# Hands-on 8: $in Operator

### Students studying Python or Java

```javascript
db.students.find({
    course:{
        $in:["Python","Java"]
    }
})
```

---

### Students from Hyderabad or Bangalore

```javascript
db.students.find({
    city:{
        $in:["Hyderabad","Bangalore"]
    }
})
```

---

### Students whose marks are 85,90,95

```javascript
db.students.find({
    marks:{
        $in:[85,90,95]
    }
})
```

---

# Hands-on 9: $nin Operator

### Students not studying Python or Java

```javascript
db.students.find({
    course:{
        $nin:["Python","Java"]
    }
})
```

---

### Students not from Hyderabad or Bangalore

```javascript
db.students.find({
    city:{
        $nin:["Hyderabad","Bangalore"]
    }
})
```

---

### Students whose marks are not 85,90,95

```javascript
db.students.find({
    marks:{
        $nin:[85,90,95]
    }
})
```

---

# Hands-on 10: Multiple Conditions

### Active Python students

```javascript
db.students.find({
    course:"Python",
    status:"Active"
})
```

---

### Active students with marks above 85

```javascript
db.students.find({
    status:"Active",
    marks:{
        $gt:85
    }
})
```

---

### Java students whose fees are below 32000

```javascript
db.students.find({
    course:"Java",
    fees:{
        $lt:32000
    }
})
```

---

### Python students from Hyderabad

```javascript
db.students.find({
    course:"Python",
    city:"Hyderabad"
})
```

---

### Active students from Hyderabad with marks above 80

```javascript
db.students.find({
    status:"Active",
    city:"Hyderabad",
    marks:{
        $gt:80
    }
})
```

---

# Practice Exercises

1. Find students whose age is exactly 22.
2. Find students whose age is not 22.
3. Find students whose fees are greater than 35,000.
4. Find students whose marks are less than 70.
5. Find students whose marks are between 75 and 90.
6. Find students studying Python or MERN.
7. Find students not studying React or NodeJS.
8. Find students from Hyderabad or Pune.
9. Find completed students with marks above 90.
10. Find active Python students whose fees are below 26,000.

This dataset and these exercises cover all the comparison operators discussed in your uploaded material (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`) and provide a complete classroom-style hands-on practice set.
