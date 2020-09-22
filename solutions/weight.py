# 09.16.2020
# Maxime to Miniac

# input
# let a,b,c,d,e be their respective weight limits for the bridges
a = int(input('Enter weight limit for a: '))
b = int(input('Enter weight limit for b: '))
c = int(input('Enter weight limit for c: '))
d = int(input('Enter weight limit for d: '))
e = int(input('Enter weight limit for e: '))

# processing
route1 = min(a, b, c) # Has bridges, a,b,c
route2 = min(d, e) # Has bridges, d,e
max_weight = max(route1, route2)

# output
print('We can carry over a weight of:', max_weight)