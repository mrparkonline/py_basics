# Create a Python program that helps us calculate the greatest common divisor of two user inputted integers. You may assume that the inputted integers will always be integers and greater than 1.

# GCD

import math

# input
num1 = int(input('Enter the first value: '))
num2 = int(input('Enter the second value: '))

# processing
answer = math.gcd(num1, num2)

# output
print('The GCD is:', answer)