---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Outputing Information w/ Python
---

## ```print()``` an output function

Anytime we need to output data/information on to the interpreter, we use the ```print()``` function.

![](figures/02_f1.png)

```
print() is a built-in function provided by Python, it helps us output to the interpreter

'Hello, World' is the argument ... the data/information that we want to output to the interpreter
```

There are special words that are followed by parenthesis (brackets), which we call them as functions or built-in functions. The programming language of Python will have these functions to help us manipulate code. We will explore these as we code, and in the future, you will be able to create your own functions as well.

```print()``` is a built-in function that outputs a message onto the console interpreter. The function is often used to output data for our programs. By the way, the print() function won’t activate your paper printer.

At this moment, I recommend that you write the code above in your editor and executing it by pressing run.

## ```print()``` is a multi-argument function

Examine the code snippet below:


```python
message1 = 'Hello'
message2 = 'World'

print(message1, message2, '!')
```

    Hello World !


The resulting output was ```Hello World !```.

Since ```print()``` is a multi-argument function, we can provide it multiple values to print at once.
- The data will be printed in one single line
- We separate each argument by commas (,)
- The comma will automatically add a whitespace in between each arguments. _If you don't like this behaviour, we can modify this later._
