---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Modules
---

Modules are collection of code that is available for us to call upon when needed. This helps us program while not reinventing the wheel.

### What are Modules?

A module is a Python code with a sole purpose that it exists to:
- Group related code
- Extend the capabilities of your current Python code by importing it to your own code
- Avoid creating solutions that already exist

The two modules that we will focus on will be: __math__ and __random__.

There are a lot modules that exists beyond what Python 3 offers (pandas and plotly to name a few). These can be installed to your computer.

### Special Keywords

To use any modules, we need the following 3 keywords:
- ```import```
- ```from```
- ```as```

### ```math``` module

The math module allow us to access more built-in functions to access some mathematical functions that basic python does not include. 

You can find the entire offering of the math module [here](https://docs.python.org/3/library/math.html).

```python
math.ceil(x) → rounds up the parameter x to its closest integer
math.floor(x) → rounds down the parameter x to its closest integer
math.fabs(x) → returns the absolute (non-negative) value of x
math.factorial(x) → returns the calculation of x factorial (x!)
math.gcd(a,b) → returns the greatest common divisor of parameters a and b
math.log(x) → returns the natural log (ln) of x
math.log2(x) → returns the base 2 log of x
math.log10(x) → returns the base 10 log of x
math.pow(x,y) → returns to power of x to the exponent of y
math.sqrt(x) → returns the square root of x
math.sin(x) → returns the sine of x
math.cos(x) → returns the cosine of x
math.tan(x) → returns the tangent of x
math.asin(x) → returns the arc sine of x
math.acos(x) → returns the arc cosine of x
math.atan(x) → returns the arc tangent of x
math.degrees(x) → returns the conversion of x radians to degrees
math.radians(x) → returns the conversion of x degrees to radians
```



```python
# Math Module Example
# Just using only the import statement

import math # this gives access to the entire module

# to use any of the functions seen above, we need the "math." prefix

# Greatest common divider
a = 144
b = 252

result = math.gcd(a,b)
print('The GCD of', a, 'and', b, 'is:', result)
```

    The GCD of 144 and 252 is: 36



```python
# Math Module Example 2
# Using from ... import ... as 
# from allow us to target a single function/item from our importing module
# as allow us to rename the imported function

from math import sqrt as squareRoot # we have now only imported square root function and renamed it
# this way, we don't need the 'math.' prefix

print('The square root of 25 is:', squareRoot(25))
```

    The square root of 25 is: 5.0


### ```random``` module

The random module is a way to add random-like functionality to our code. Generation of random number is very fun way concept especially in game development.

You can find the entire offering of the random module [here](https://docs.python.org/3/library/random.html).

```

random.seed(x) → the parameter x (an integer) is optional …

    The seed function exists to help us generate a more predictable randomness. 
    If the seed() is given an integer, the program will generate the random same number every time.
   
random.random() → This function requires no parameters. 
    Every time this function is called, it will generate a random float from 0.0 inclusively to 1.0 exclusively

random.randrange(a,b,c) → This function helps to generate random numbers, it will behave differently based on the number of arguments

    random.randrange(x) → Generates random integers from 0 to x, but not including x

    random.randrange(a,b) → Generates random integers from a to b, but not including b

    random.randrange(a,b,c) → Generates random integers from a to b; not including b, and 
    the available values will be a set of values from parameter a increasing by parameter c


random.randint(a,b) → Behaves the same way as random.randrange(a,b+1)

random.choice(sequence) → Returns a random value from the parameter sequence
    if the sequence is a string → returns a single character
    if the sequence is a list → returns a single item

```


```python
# Example ... just using random()

import random
print('Random number generated:', random.random())

# Whenever this program runs, it should generate a new random floating point value
```

    Random number generated: 0.15972819314209852



```python
# Example 2
# Using randrange to generate random integers

from random import randrange # if you like what the function is called, as statement is not required

value1 = randrange(10) # Value 1 now contains a random value from 0 to 9 inclusively
value2 = randrange(1,101) # Value 2 now contains a random value from 1 to 100 inclusively

value3 = randrange(10, 1000, 3) 
# Value 3 now contains a random value of X such that the list of numbers to choose from goes from 10 to 1000
# However, the interval between each number is 3 units away

print('value1:', value1)
print('value2:', value2)
print('value3:', value3)
```

    value1: 2
    value2: 52
    value3: 490



```python
# Example 3
# Using choice

from random import choice

word = 'The Lazy Dog sleeps in his crate.'
array = ['Oranges', 'Watermelons', 'Apples', 'Kiwis', 'Bananas']

print('Random letter from word:', choice(word))
print('Random item from array:', choice(array))
```

    Random letter from word: a
    Random item from array: Watermelons

