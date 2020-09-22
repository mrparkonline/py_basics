# Painting our Fences
import math

# input
fence1 = input('Enter your first fence side: ')
fence2 = input('Enter your second fence side: ')
fence3 = input('Enter your third fence side: ')

# processing
fence1_length = len(fence1)
fence2_length = len(fence2)
fence3_length = len(fence3)

paint_cans_needed = fence1_length + fence2_length + fence3_length

total_cans = math.ceil(paint_cans_needed / 12) * 12

leftover = total_cans - paint_cans_needed
total_cost = math.ceil(paint_cans_needed / 12) * 14.95


# output
print('We needed', paint_cans_needed, 'cans.')
print('There were', leftover, 'cans leftover.')
print('The total cost is:', total_cost)

