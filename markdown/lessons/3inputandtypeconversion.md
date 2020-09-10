---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Input and Type Conversion
---

To allow users to interact with our program via keyboard, we need a way to read inputs from it.

## ```input()``` built-in function

- ```input()``` is a built-in function that is able to grab input from the console when typed from the keyboard by the user
- The __input()__ function will always read its data as a string data typed value

Let's see an example.


```python
# Our example program

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Hello,', first_name, last_name)
```

    Enter your first name: Mr.
    Enter your last name: Park
    Hello, Mr. Park


- Since we are grabbing data with input, it should be assigned to variables
    - first_name has been assigned with the user input of "Mr."
    - last_name has been assigned with the user input of "Park"
- the ```input()``` can contain a string message/argument inside to display when running the code
    - For our example, the argument was "Enter your first name: " for the first input
- After the input is finished, the variable now contains the values inputted which we printed

## Type Conversion Functions

Since ```input()``` only reads data as string data typed values, we are going to need a way to convert them to numeric data types for different scenarios.

These functions will produce an error if they cannot convert the argument to their targetted data type.

Example: ```int('hello world')``` will produce an error ... 'hello world' is not an integer.

#### ```int()``` function

This function allows us to the convert given argument into an integer.


```python
string_three = "3"
integer_three = int(string_three) # now integer_three contains an integer of 3

print(integer_three + 3) # should be 6
print(string_three + 3) # an error because a string of 3 cannot add an integer of 3
```

    6



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-c6a3c3a9a014> in <module>
          3 
          4 print(integer_three + 3) # should be 6
    ----> 5 print(string_three + 3) # an error because a string of 3 cannot add an integer of 3
    

    TypeError: can only concatenate str (not "int") to str


#### ```float()``` function

This function allow us to convert the given argument into a floating point value.


```python
string_pi = "3.14"
float_pi = float(string_pi)

integer_three = 3
float_three = float(integer_three)

print(float_pi)
print(float_three)
```

    3.14
    3.0


#### ```str()``` function

This function allow us to convert non-string typed value back into a string.

_This function may seem silly now; it will be very important in the future unit._


```python
num1 = 42
num2 = 3.14159

str_num1 = str(num1)
str_num2 = str(num2)

print(str_num1)
print(str_num2)
```

    42
    3.14159

