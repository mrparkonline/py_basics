'''
Exercise 6: Develop an instruction set that calculates the area and the perimeter of a rectangle.
'''

# Area = width/base * height
# Perimeter = 2*width + 2*height

# input
base = float(input('Enter the base as a unit: '))
height = float(input('Enter the height as a unit: '))

# processing
area = base * height
perimeter = (2*base) + (2*height)

# output
print('The area of the rectangle is:', area , 'units squared.')
print('The perimeter of the rectangle is:', perimeter, 'units.')