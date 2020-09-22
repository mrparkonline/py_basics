# 09.16.2020
# Tutorial

# The program should take these inputs: party size, the cost of the meal and the percentage for the tip. 
# The output should be: the amount for the tip and how much each person is paying for the meal.

# input
party_size = int(input('Enter the size of your party: '))
cost = float(input('Enter the cost of your meal: '))
tip_percent = int(input('Enter the tip percentage: '))

# processing
tip = cost * (tip_percent / 100)
tip = round(tip, 2) # this rounds our value to two decimal places

total_cost = cost + tip
individual_cost = round(total_cost / party_size, 2)

# output
print('The tip was:', tip)
print('Individual cost was:', individual_cost)