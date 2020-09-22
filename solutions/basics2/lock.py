# A combination lock has 0 to 49 possible values. We can rotate to the right with each tick landing us on a number. 

# input
tick = int(input('Enter the number of ticks on the lockpad: '))

# processing
# since it is a lock with numbers 0 to 49 ... there are 50 possible locations

location = tick % 50

# output
print('After', tick, 'ticks, the lock points to:', location)