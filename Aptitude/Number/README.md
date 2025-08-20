# Number Theory: 🧠🔢

This guide provides a concise summary of fundamental concepts in number theory, essential for aptitude preparation. It covers different types of numbers, their properties, divisibility rules, and other useful facts.

## 1. Types of Numbers
* **Integers**: All numbers with a fractional part of zero (e.g., -3, 0, 10).
* **Natural Numbers**: Counting numbers greater than zero (1, 2, 3...).
* **Whole Numbers**: All natural numbers, including zero (0, 1, 2, 3...).
* **Prime Numbers**: Numbers with exactly two distinct factors: 1 and themselves (e.g., 2, 3, 53).
* **Composite Numbers**: Numbers greater than 1 that are not prime (e.g., 4, 60, 91).
* **Co-primes**: Two numbers whose highest common factor (HCF) is 1.

***

## 2. Important Facts About Prime Numbers
* **0 and 1** are neither prime nor composite.
* **2** is the only even prime number.
* There are **25** prime numbers less than 100.
* To find the **count of divisors** for a number *n*, use its prime factorization: if $n = p_1^{e_1} \times p_2^{e_2} \times ...$, the number of divisors is $(e_1 + 1)(e_2 + 1)...$

***

## 3. Divisibility Rules & Remainders
This section provides a summary of divisibility rules for numbers 2 through 11 and how to find remainders quickly.

### Divisibility Rules

| Divisibility by | Rule |
|---|---|
| 2 | Last digit is even. |
| 3 | Sum of digits is divisible by 3. |
| 4 | Last two digits are divisible by 4. |
| 5 | Last digit is 0 or 5. |
| 6 | Divisible by both 2 and 3. |
| 7 | Double the last digit and subtract from the rest of the number. The result is divisible by 7. |
| 8 | Last three digits are divisible by 8. |
| 9 | Sum of digits is divisible by 9. |
| 11 | The alternating sum of digits is 0 or a multiple of 11. |

### Remainder Rules

* **By 2**: Remainder is 1 if the last digit is odd, 0 if even.
* **By 3**: Remainder is the same as the remainder of the sum of its digits divided by 3.
* **By 4**: Remainder is the same as the remainder of the last two digits divided by 4.
* **By 5**: Remainder is the same as the remainder of the last digit divided by 5.
* **By 9**: Remainder is the same as the remainder of the sum of its digits divided by 9.

***

## 4. Division Theorem and Useful Rules
The fundamental division theorem is **Dividend = (Divisor x Quotient) + Remainder**.

### Other Key Rules
* $(x^n - a^n)$ is divisible by $(x-a)$ for all values of $n$.
* $(x^n - a^n)$ is divisible by $(x+a)$ for all even values of $n$.
* $(x^n + a^n)$ is divisible by $(x+a)$ for all odd values of $n$.
* If a three-digit number is repeated to form a six-digit number (e.g., 123123), it is divisible by **7, 11, and 13**.

***

## 5. Cyclicity of Numbers 🔄
Cyclicity refers to the repeating pattern of the unit digit when a number is raised to successive powers. This helps determine the last digit without extensive calculation.

* **Digits 0, 1, 5, 6**: The unit digit remains the same regardless of the power.
* **Digits 4, 9**: The unit digit alternates between two numbers.
    * **4**: alternates between 4 and 6.
    * **9**: alternates between 9 and 1.
* **Digits 2, 3, 7, 8**: The unit digit pattern repeats every four powers.
    * **2**: 2, 4, 8, 6
    * **3**: 3, 9, 7, 1
    * **7**: 7, 9, 3, 1
    * **8**: 8, 4, 2, 6