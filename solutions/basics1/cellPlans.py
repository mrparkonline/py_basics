'''
Plan A
100 free minutes then 25 cents per minute
15 cents per minute
20 cents per minute

Plan B
250 free minutes then 45 cents per minute
35 cents per minute
25 cents per minute
'''

# inputs
day_usage = int(input('Enter day time usage in minutes: '))
evening_usage = int(input('Enter evening usage in minutes: '))
weekend_usage = int(input('Enter weekend usage in minutes: '))

# processing
planA_dayCost = max(day_usage - 100, 0) * 0.25
planA_evening = 0.15 * evening_usage
planA_weekend = 0.20 * weekend_usage

planB_dayCost = max(day_usage - 250, 0) * 0.45
planB_evening = 0.35 * evening_usage
planB_weekend = 0.25 * weekend_usage

planA = planA_dayCost + planA_evening + planA_weekend
planB = planB_dayCost + planB_evening + planB_weekend

# output
print('Plan A for moe costs:', planA)
print('Plan B for moe costs:', planB)