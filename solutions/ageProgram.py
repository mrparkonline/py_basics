'''
Exercise 4: Develop an Instruction Set that calculates your age based on the current year.
'''

# input section
current_year = int(input('Enter the current year: '))
birth_year = int(input('Enter your birth year: '))

# processing
age = current_year - birth_year

# output
print('Your age is:', age)