---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Useful Built-in Functions
---

These functions that we will learn are already programmed into the python language. We will learn how to use these functions to augment our code.

### Maximum and Minimum Functions

```max()``` and ```min()``` are built-in functions that help us find the extremes of its arguments.

__Single Argument Use:__ When a function only has one argument.

For max and min, the single argument must be either string or list. (Technically, iterable & comparable ... grade 12 definition)


```python
# Single Argument Example
word = 'HelloWorld!'

print('Max of', word, 'is:', max(word))
print('Min of', word, 'is:', min(word))
```

    Max of HelloWorld! is: r
    Min of HelloWorld! is: !


__Explanation:__

- When using max or min on a list or a string, we compare each individual item or character
- For strings, we compare them by using the character's [ASCII value](http://www.asciitable.com/)

__Multi-Argument Use:__ When a function has multiple arguments.

For max and min, the arguments themselves will be compared to each other and output the appropriate extreme.

```max()``` and ```min()``` are special functions that can take any number of arguments.


```python
# Multi-Argument Example

print(max(7, 18, 15, 9, 18, 6, 21, 9, 4, 8))
print(min(9, 18, 6, 21, 9, 4, 8))
```

    21
    4


__NOTE:__

We can assign the result of max() and min() function to a variable as well.


```python
# example
result = max('hello')
print(result) # should be o
```

    o


### Length Function

The ```len()``` is the length function which is a __single argument__ function.

The ```len()``` function is used to find the length of collection; moreover, the number of items in the collection.

The only collection type data types in Grade 10 and 11 are strings and lists.

We cannot find the length of non-collection based data types (int, float)


```python
# len() examples
print(len('abcdefg')) # outputs 7 because there are 7 characters in the string
print(len([1,2,3,4,5,6])) # Will return 6 because there are 6 items in the list

```

    7
    6

