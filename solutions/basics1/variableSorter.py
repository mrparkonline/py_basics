# Variable Sorter

# Create a program that takes 3 integer values from the user and store them into 3 variables of first, second and third. 

# The program then should sort the 3 variables such that first <= second <= third.

# input
first = int(input('Enter a value: '))
second = int(input('Enter a value: '))
third = int(input('Enter a value: '))

print('first is now:', first)
print('second is now:', second)
print('third is now:', third)

# processing
# min() and max()
total_sum = first + second + third
smallest = min(first, second, third)
largest = max(first, second, third)

first = smallest
third = largest
second = total_sum - first - third

# output
print('first is now:', first)
print('second is now:', second)
print('third is now:', third)