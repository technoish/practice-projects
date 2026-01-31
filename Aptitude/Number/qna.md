# 📘 Numbers — Practice Questions (Solved) — Table Notes

---

## ✅ Question 1 — Successive Division Remainders

| Given | Value |
|--------|---------|
| Divisors | 35, 45, 55 |
| Remainders | 18, 28, 38 |

### Method

| Step | Work |
|------|------|
| LCM(35,45,55) | 3465 |
| Find common difference | 35−18 = 17, 45−28 = 17, 55−38 = 17 |
| Common remainder | 17 |
| Required number | 3465 − 17 |

**Answer:** Smallest number = **3448**

---

## ✅ Question 2 — Four Digit Numbers Divisible by 7

| Item | Value |
|--------|---------|
| Smallest 4-digit | 1000 |
| Largest 4-digit | 9999 |

### Steps

| Step | Work |
|------|------|
| First multiple ≥1000 | 1001 |
| Last multiple ≤9999 | 9996 |
| AP formed | 1001, 1008, …, 9996 |
| Common difference | 7 |

Formula used: an = a1 + (n−1)d

| Calculation | Result |
|-------------|---------|
| 9996 = 1001 + (n−1)×7 | n−1 = 1285 |
| n | 1286 |

**Answer:** Total numbers = **1286**

---

## ✅ Question 3 — Find Maximum B

Addition pattern:

1 2 B  
B 4 C  
C 6 7  
------  
10 3 5  

### Column Logic

| Column | Result |
|----------|---------|
| Units column | B + C ends in 5 |
| Carry condition | B + C = 8 |

### Maximize B

| Case | Result |
|------|---------|
| Take C = 0 | B = 8 |

### Verification

128 + 840 + 067 = 1035

**Answer:** **B = 8**

---

## ✅ Question 4 — Prime Number Check

| Number | √n Limit | Test Result | Final |
|-----------|------------|-------------|--------|
| 247 | < 16 | Divisible by 13 | Not Prime |
| 397 | < 20 | Not divisible by primes ≤19 | Prime |
| 423 | < 21 | Divisible by 3 | Not Prime |

**Answer:** Only **397** is prime

---

## ✅ Question 5 — Unit Digit of Product

Expression: (17)^153 × (31)^62

### Reduce to Unit Digits

| Base | Unit Digit |
|--------|-------------|
| 17 | 7 |
| 31 | 1 |

### Cycle of 7

| Power | Unit Digit |
|---------|-------------|
| 1 | 7 |
| 2 | 9 |
| 3 | 3 |
| 4 | 1 |

Cycle length = 4

### Reduce Power

| Step | Result |
|------|----------|
| 153 % 4 | 1 |
| Unit digit of 7^153 | 7 |
| Unit digit of 1^62 | 1 |

Final multiply → 7 × 1 = **7**

**Answer:** Unit digit = **7**

---
