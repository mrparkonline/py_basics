# Write a program that inputs the number of tiles and then prints out the maximum side length. You may assume that the number of tiles is less than ten thousand.

from math import sqrt as squareRoot

# input
tiles = int(input('Enter the number of tiles: '))

# processing
max_side_length = squareRoot(tiles)
max_side_length = int(max_side_length)

# output
print('The largest square has side length', max_side_length)