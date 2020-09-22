# Create a Python program that calculates the distance between two points. There should be 4 integer inputs: x-coordinate and y-coordinate from the first point and x-coordinate and y-coordinate of the second point.

## Distance Solution

from math import sqrt as squareRoot

# input
x_p1 = float(input('Enter coordinate x for point 1:'))
y_p1 = float(input('Enter coordinate y for point 1:'))

x_p2 = float(input('Enter coordinate x for point 2:'))
y_p2 = float(input('Enter coordinate y for point 1:'))

# processing
difference_x = x_p2 - x_p1
difference_y = y_p2 - y_p1

distance = squareRoot(difference_x**2 + difference_y**2)

# output
print('The distance between the two points are:', distance, 'units.')