# Create a program that takes in 3 integers that are 5 digits long. Find the product of multiplying the last digits of the 3 integers.

# input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

# processing
last_digit1 = num1 % 10 # if you ever need the last digit, you can alway do modulus of 10
last_digit2 = num2 % 10 
last_digit3 = num3 % 10 

total_product = last_digit1 * last_digit2 * last_digit3
#print(num1, last_digit1)

# output
print('The total product of multiplying the last digits is:', total_product)