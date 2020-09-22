# Create a Python program that mimics the heads or tails game. The program should output either ‘H’ for heads or ‘T’ for tails randomly on each execution of the program.

from random import choice

print(choice('HT'))
print(choice(['Heads', 'Tails']))

'''
# Using 5 print() statements, create a tiny Python program that generates 5 random integers from 1 to 100; moreover, the program should output the same 5 random numbers everytime it runs.

from random import randrange
from random import seed

seed(2)
print(randrange(1,101))
print(randrange(1,101))
print(randrange(1,101))
print(randrange(1,101))
print(randrange(1,101))
'''