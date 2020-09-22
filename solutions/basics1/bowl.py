# Write a program that reads in three weights and prints out the weight of Mama Bear's bowl. You may assume all weights are positive integers less than 100.

# input
weight1 = int(input('Enter a weight: '))
weight2 = int(input('Enter a weight: '))
weight3 = int(input('Enter a weight: '))

# processing
total_sum = weight1 + weight2 + weight3
middle_bowl = total_sum - min(weight1, weight2, weight3) - max(weight1, weight2, weight3)

# output
print('The weight of the mamabowl is:', middle_bowl)