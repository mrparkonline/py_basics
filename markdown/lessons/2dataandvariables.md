---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Data & Variables
---

Majority of the time you will be dealing with data contained in variables.

__Data:__ Any representable information for us to grab, show and manipulate.

__Variables:__ A labeled container that holds data for us to reference to in our code.

### Basic Data Types

__Integers__: Integers are numbers that range from negative infinity to positive infinity. Now computers have limitations based on their computer architecture.

- Examples: ```1, -1, 42, 1000```

__Floating Point Values:__ Floating Points are what we call decimals in computer programming; moreover, floating points represent all the real numbers. 

- Example: ```0.5, 3.14, 3.649```

__Booleans:__

Boolean data type can only have two values → __True__ or __False__. These values are often used in conditional or decision making situations. If a certain situation is True, then a Boolean value is generated by the program, and vice versa.

__Strings:__ Strings are considered a collection of alphanumeric and special symbols. A single alphanumeric or special symbol are sometimes called a character. To denote that a value is a string, we trap it inside double or single quotation marks.

- Example: ```“Hello”, “Park”, “3.14”, “42” … “” or ‘’ are empty strings```

__Lists:__ Lists are a collection of different and multiple data types; moreover, it is one of the way to have a collection of values. We denote the start and the end of a list with square brackets, and separate values are separated by commas.

- Example: ```[“Apple”, “Orange”, “Watermelon”], [1,2,3,4,5], [ ]```

__NOTE:__ Strings and Lists have their own units of study due to their complexity.

### Variables

_Just like in math, computer programming is dependent on the manipulation of variables. However, there will be huge differences._

Variables are used to hold values of data. Since variables hold data, the variable itself will be __TYPED__ based on its containing value. To create a variable, we denote a name to the left, and value to the right by using an equal sign.

__FORMAT:__ label = value

__Examples:__


```python
# Variable containing someone's age
age = 28

# Variable containing names
# for variables containing string values, we can use either single or double quotations as long as we don't mix and match

firstName = "Mr."
lastName = 'Park'

# Variable containing a float
pi = 3.14

# Variable with multiple values via list
fruits = ['Apple', 'Orange', 'Watermelon']
```

#### Variable Naming Rules

1. You don’t start a variable with capitals
2. There are no white spaces, we connect multi word variables with either camelCasing or under_scores.
3. Variable names should be effective and short, not vague.
4. Do not use any [built-in function names](https://docs.python.org/3/library/functions.html) nor [keywords](https://www.w3schools.com/python/python_ref_keywords.asp) as variable names

#### Variable Naming Convention Set from the Python Organization:
- The variable name describes its data that it contains
- The variable name exists on its own
    - doesn’t require abbreviation
    - it not a shortened form of a word
- The variable name is not ambiguous
- The variable name does not contain any whitespace 
- The variable name does not start with numbers
- The variable name does not start with capital letters (6ix is a very bad variable name)

#### Variable Names: ```under_scoring```

When you create a variable name that requires multiple words to describe the data, you can separate the words with an underscore (-)

```python
# Example
first_name = “Mr.”
```

#### Variable Names: ```camelCasing```

Unlike separating multiple words with an underscore, we can also combine them by capitalizing the words after the first. 

It is a rule that, in Python, your variable should not start with capitals, but camelCasing will allow us to capitalize our subsequents words after the first.


```python
# Example
firstName = “Mr.”
```