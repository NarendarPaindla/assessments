Below is a **complete MongoDB Indexes Hands-on Lab** using a realistic **students** collection. It covers every topic in your syllabus with practical examples.

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

# Step 3: Insert Sample Data

```javascript
db.students.insertMany([
{name:"Rahul",email:"rahul@gmail.com",age:21,course:"Python",fees:25000,city:"Hyderabad",status:"Active",marks:85,skills:["Python","HTML","CSS"]},
{name:"Priya",email:"priya@gmail.com",age:22,course:"Java",fees:30000,city:"Bangalore",status:"Inactive",marks:90,skills:["Java","Spring"]},
{name:"Arjun",email:"arjun@gmail.com",age:20,course:"MERN",fees:35000,city:"Chennai",status:"Active",marks:76,skills:["MongoDB","React","NodeJS"]},
{name:"Sneha",email:"sneha@gmail.com",age:23,course:"Python",fees:25000,city:"Delhi",status:"Completed",marks:95,skills:["Python","Django"]},
{name:"Vikram",email:"vikram@gmail.com",age:24,course:"Java",fees:28000,city:"Mumbai",status:"Active",marks:82,skills:["Java","MySQL"]},
{name:"Anjali",email:"anjali@gmail.com",age:19,course:"Data Science",fees:40000,city:"Hyderabad",status:"Active",marks:88,skills:["Python","Pandas","NumPy"]},
{name:"Kiran",email:"kiran@gmail.com",age:25,course:"Python",fees:22000,city:"Pune",status:"Inactive",marks:72,skills:["Python","Flask"]},
{name:"Ravi",email:"ravi@gmail.com",age:22,course:"MERN",fees:36000,city:"Chennai",status:"Completed",marks:91,skills:["MongoDB","Express","React"]},
{name:"Meena",email:"meena@gmail.com",age:21,course:"Java",fees:31000,city:"Delhi",status:"Active",marks:79,skills:["Java","Hibernate"]},
{name:"Suresh",email:"suresh@gmail.com",age:26,course:"Python",fees:26000,city:"Hyderabad",status:"Completed",marks:84,skills:["Python","FastAPI"]}
])
```

---

# Hands-on 1: View Existing Indexes

```javascript
db.students.getIndexes()
```

Output:

```
_id_
```

MongoDB automatically creates an index on `_id`.

---

# Hands-on 2: Create Single Field Index

Create index on Age

```javascript
db.students.createIndex({age:1})
```

---

Create index on Course

```javascript
db.students.createIndex({course:1})
```

---

Create index on Marks

```javascript
db.students.createIndex({marks:-1})
```

---

Check indexes

```javascript
db.students.getIndexes()
```

---

# Hands-on 3: Query Using Index

```javascript
db.students.find({
    age:22
})
```

---

Check execution plan

```javascript
db.students.find({
    age:22
}).explain("executionStats")
```

Look for

```
IXSCAN
```

instead of

```
COLLSCAN
```

---

# Hands-on 4: Unique Index

Create Unique Email Index

```javascript
db.students.createIndex(
{
    email:1
},
{
    unique:true
})
```

Try duplicate email

```javascript
db.students.insertOne({
name:"Test",
email:"rahul@gmail.com"
})
```

Output

```
Duplicate Key Error
```

---

# Hands-on 5: Named Index

```javascript
db.students.createIndex(
{
course:1,
marks:-1
},
{
name:"course_marks_index"
})
```

View indexes

```javascript
db.students.getIndexes()
```

---

# Hands-on 6: Compound Index

```javascript
db.students.createIndex({
course:1,
city:1
})
```

Query

```javascript
db.students.find({
course:"Python",
city:"Hyderabad"
})
```

---

Query only course

```javascript
db.students.find({
course:"Python"
})
```

Uses index

---

Query only city

```javascript
db.students.find({
city:"Hyderabad"
})
```

Will not efficiently use the compound index.

---

# Hands-on 7: ESR Rule

Create

```javascript
db.students.createIndex({
course:1,
marks:-1,
fees:1
})
```

Query

```javascript
db.students.find({
course:"Python",
fees:{
$gt:20000
}
}).sort({
marks:-1
})
```

---

# Hands-on 8: Multikey Index

Skills is an array

```javascript
db.students.createIndex({
skills:1
})
```

Query

```javascript
db.students.find({
skills:"Python"
})
```

---

```javascript
db.students.find({
skills:"React"
})
```

---

# Hands-on 9: Text Index

```javascript
db.students.createIndex({
name:"text",
course:"text"
})
```

Search

```javascript
db.students.find({
$text:{
$search:"Python"
}
})
```

---

Search

```javascript
db.students.find({
$text:{
$search:"Rahul"
}
})
```

---

# Hands-on 10: Sparse Index

Insert document without phone

```javascript
db.students.insertOne({
name:"Ajay",
course:"Python"
})
```

Create Sparse Index

```javascript
db.students.createIndex(
{
phone:1
},
{
sparse:true
})
```

---

Insert

```javascript
db.students.insertOne({
name:"Ramesh",
phone:"9876543210"
})
```

---

# Hands-on 11: Partial Index

```javascript
db.students.createIndex(
{
status:1
},
{
partialFilterExpression:{
status:"Active"
}
})
```

Query

```javascript
db.students.find({
status:"Active"
})
```

---

# Hands-on 12: TTL Index

Create Collection

```javascript
db.sessions.insertOne({
user:"Rahul",
createdAt:new Date()
})
```

Create TTL

```javascript
db.sessions.createIndex(
{
createdAt:1
},
{
expireAfterSeconds:60
})
```

Document automatically deleted after 60 seconds.

---

# Hands-on 13: Case Insensitive Index

```javascript
db.students.createIndex(
{
email:1
},
{
collation:{
locale:"en",
strength:2
}
})
```

Query

```javascript
db.students.find(
{
email:"RAHUL@GMAIL.COM"
}
).collation({
locale:"en",
strength:2
})
```

---

# Hands-on 14: Hashed Index

```javascript
db.students.createIndex({
email:"hashed"
})
```

Equality Query

```javascript
db.students.find({
email:"rahul@gmail.com"
})
```

---

# Hands-on 15: Drop Index

View

```javascript
db.students.getIndexes()
```

Drop by name

```javascript
db.students.dropIndex("age_1")
```

---

Drop all

```javascript
db.students.dropIndexes()
```

---

# Hands-on 16: Explain Query

Without Index

```javascript
db.students.find({
marks:85
}).explain("executionStats")
```

Shows

```
COLLSCAN
```

---

Create Index

```javascript
db.students.createIndex({
marks:1
})
```

---

Run Again

```javascript
db.students.find({
marks:85
}).explain("executionStats")
```

Shows

```
IXSCAN
```

---

# Practice Exercises

### Beginner

1. Create an index on `city`.
2. Create an index on `status`.
3. View all indexes.
4. Drop the `city` index.
5. Create an index on `fees`.

---

### Intermediate

6. Create a unique index on `email`.
7. Create a compound index on `course` and `city`.
8. Search students using the compound index.
9. Create an index on the `skills` array.
10. Search students with the `"React"` skill.

---

### Advanced

11. Create a text index on `name` and `course`.
12. Search for `"Python"` using `$text`.
13. Create a sparse index on `phone`.
14. Create a partial index for active students.
15. Use `.explain("executionStats")` to compare `COLLSCAN` vs `IXSCAN`.
16. Create a TTL index on a `sessions` collection.
17. Create a hashed index on `email`.
18. Create a named index called `student_course_marks_idx`.
19. Drop all indexes except the default `_id` index.
20. Measure query performance before and after creating an index using `explain()`.

This lab covers all the major index concepts from your syllabus: **single-field, compound, unique, named, sparse, partial, TTL, text, multikey, hashed, case-insensitive indexes, `getIndexes()`, `dropIndex()`, `dropIndexes()`, and performance analysis with `explain()`**.
