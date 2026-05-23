# codes

[Day-1](https://colab.research.google.com/drive/16hRa-RbgM4dpU1-oh9jNJ5-ydoOLhptm?usp=sharing)


[test-3](https://forms.gle/7iSQ1bdE4a6ruwmN6)

# REAL WORLD QUESTIONS

---

## 📝 Question 1 — Income Tax Calculator

**Q: Write a Python program to calculate income tax based on annual salary:**

| Condition | Tax |
|-----------|-----|
| Salary > ₹15,00,000 | 30% tax |
| Salary > ₹10,00,000 | 20% tax |
| Salary > ₹5,00,000 | 10% tax |
| Salary ≤ ₹5,00,000 | No tax |

**Sample Input:**
```
Enter your annual salary: 1200000
```
**Expected Output:**
```
--- Tax Summary ---
Annual Salary : ₹1200000.00
Tax Rate      : 20%  (₹240000.00)
Net Salary    : ₹960000.00
```

---

## 📝 Question 2 — Electricity Bill Calculator

**Q: Write a Python program to calculate electricity bill based on units consumed:**

| Units Consumed | Rate per Unit |
|----------------|---------------|
| Above 300 units | ₹6 per unit |
| 201 – 300 units | ₹4 per unit |
| 101 – 200 units | ₹3 per unit |
| 0 – 100 units | ₹2 per unit |

**Sample Input:**
```
Enter units consumed: 250
```
**Expected Output:**
```
--- Electricity Bill ---
Units Consumed : 250
Rate Applied   : ₹4 per unit
Total Bill     : ₹1000.00
```

---

## 📝 Question 3 — Movie Ticket Pricing

**Q: Write a Python program to calculate movie ticket price based on age:**

| Condition | Ticket Price |
|-----------|-------------|
| Age < 5 | Free |
| Age 5 – 12 | ₹100 |
| Age 13 – 59 | ₹250 |
| Age ≥ 60 | ₹150 (Senior discount) |

**Sample Input:**
```
Enter your age: 65
```
**Expected Output:**
```
--- Ticket Booking ---
Age          : 65
Category     : Senior Citizen
Ticket Price : ₹150.00
```

---

## 📝 Question 4 — Employee Bonus Calculator

**Q: Write a Python program to calculate employee bonus based on years of experience:**

| Experience | Bonus |
|------------|-------|
| Above 10 years | 20% of salary |
| 5 – 10 years | 15% of salary |
| 2 – 5 years | 10% of salary |
| Below 2 years | No bonus |

**Sample Input:**
```
Enter salary      : 50000
Enter experience  : 7
```
**Expected Output:**
```
--- Bonus Details ---
Salary     : ₹50000.00
Experience : 7 years
Bonus      : 15%  (₹7500.00)
Take Home  : ₹57500.00
```

---

## 📝 Question 5 — Student Grade Calculator

**Q: Write a Python program to assign grade based on marks obtained:**

| Marks | Grade |
|-------|-------|
| ≥ 90 | A+ |
| ≥ 80 | A |
| ≥ 70 | B |
| ≥ 60 | C |
| ≥ 50 | D |
| Below 50 | Fail |

**Sample Input:**
```
Enter marks: 85
```
**Expected Output:**
```
--- Result ---
Marks  : 85
Grade  : A
Result : Pass
```

---

> 💡 All 5 questions use the **same concept** — `if`, `elif`, `else` with real-world scenarios. Try solving them one by one!


## 📝 Question — ATM Withdrawal Eligibility Checker

**Q: Write a Python program to check whether an ATM withdrawal is eligible based on the following conditions:**

| Condition | Result |
|-----------|--------|
| PIN correct AND sufficient balance | Transaction Successful |
| PIN correct BUT insufficient balance | Transaction Failed – Low Balance |
| PIN wrong (1st & 2nd attempt) | Wrong PIN – Try Again |
| PIN wrong (3rd attempt) | Card Blocked |

---

**Rules:**
1. User has a **pre-set PIN** and **account balance**
2. Allow maximum **3 PIN attempts**
3. Check if withdrawal amount is **less than or equal to balance**
4. Deduct amount and show **remaining balance** on success

---

**Sample Input:**
```
Welcome to the ATM
Enter your PIN        : 1234
Enter withdrawal amt  : 5000
```

**Expected Output — Case 1 (PIN correct + sufficient balance):**
```
--- Transaction Summary ---
Status            : ✅ Transaction Successful
Amount Withdrawn  : ₹5000.00
Remaining Balance : ₹15000.00
```

**Expected Output — Case 2 (PIN correct + low balance):**
```
--- Transaction Summary ---
Status  : ❌ Transaction Failed
Reason  : Insufficient Balance
Balance : ₹3000.00
```

**Expected Output — Case 3 (Wrong PIN):**
```
❌ Wrong PIN! Attempts remaining: 2
```

**Expected Output — Case 4 (3 wrong attempts):**
```
🔒 Your card has been blocked. Contact your bank.
```

---

> 💡 **Hint:** Use:
> - `if / elif / else` → to check PIN and balance conditions
> - `for` loop → to allow 3 PIN attempts
> - `break` → to exit loop on success or card block

---`

---

