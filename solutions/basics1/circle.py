# Area of a Circle

import math

# input
radius = float(input('Enter the radius of your circle: '))

# processing
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# output
print('The circle area is:', area, 'units squared.')
print('The circumference is:', circumference, 'units.')