# Creating a program that outputs the smaller variable value without using the min() function. 

# Without knowing the user inputted values of num1 and num2, create a program that outputs the lower value without using the min()

# No ifs, no booleans

# input
num1 = int(input('Enter a value: '))
num2 = int(input('Enter a value: '))

# processing
total_sum = num1 + num2
smaller_value = total_sum - max(num1, num2)

# output
print(smaller_value)