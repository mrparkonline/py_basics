# Midpoint Question

# input
x = float(input('Enter x: '))
y = float(input('Enter y: '))

x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

# processing
midpoint_x = (x+x2) / 2
midpoint_y = (y+y2) / 2

# midpoint = (midpoint_x, midpoint_y) # tuple
# print(type(midpoint))
# output
print('The mid point is found at: (', midpoint_x, ',', midpoint_y,')')