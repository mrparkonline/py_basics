---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Basic Arithmetic in Python
---

The core arithmetic operations are all available. Therefore, we can do basic math with Python.

### Binary Operators

```python

+ Addition
- Subtraction
* Multiplication
/ Division
// Floor Division
** Exponentiation
% Modulo

```

Let's look at how they work:


```python
# Example
var_a = 10
var_b = 2
var_c = -5

addition = var_a + var_b
print('var_a + var_b:', addition) # We can do arithmetic then assign the result to a variable

print('Subtraction:', var_b - var_c) # we can also do arithmetic as function arguments / inside our print statement

# BEDMAS
calculation = var_a + var_c * var_b
print('Resulting calculation:', calculation) # Python Follows BEDMAS/Order of Arithmetic operations automatically

# Exponentiation
print('Squaring 10^2:', var_a ** 2)
print('Square Root of 125:', 125 ** 0.5)
```

    var_a + var_b: 12
    Subtraction: 7
    Resulting calculation: 0
    Squaring 10^2: 100
    Square Root of 125: 11.180339887498949


### Division vs Floor Division

- Division operation will always turn the quotient into a floating point value
- Floor Division will always give an integer quotient
- Floor Division will always round down to the nearest integer


```python
# Example
print('5 / 2 is', 5 / 2) 
print('5 // 2 is' , 5 // 2)
print('----')
print('6 / 2 is',  6 / 2)
print('6 // 2 is', 6 // 2)
print('----')
print('10 / 11 is', 10 / 11)
print('10 // 11 is', 10 // 11)
```

    5 / 2 is 2.5
    5 // 2 is 2
    ----
    6 / 2 is 3.0
    6 // 2 is 3
    ----
    10 / 11 is 0.9090909090909091
    10 // 11 is 0


### Modulus Operation

The ```%``` Operator is an integer remainder finder.

In computer science, integer arithimetic is an important topic related to data, cryptography, and algorithms. Hence the modulus operation is very important.

If you don't know what a remainder is, please read about them [here](https://www.mathsisfun.com/numbers/division-remainder.html). _The website may seems elementary ... it is because you learn it in elementary school._


```python
# Modulus Example

print(42 % 2) # Output is zero, when 42 is divided by 2 there are no remainders
print(42 % 5) # Output is two, when 42 is divided by 5, 2 is leftover.
```

    0
    2


__NOTE:__

By looking at the modulus operations above we can conclude that:
- 2 is a factor of 42 and 42 is divisble by 2
- 5 is not a factor of 42 and 42 is not divisible by 5 because 42 / 5 will create a __remainder__
