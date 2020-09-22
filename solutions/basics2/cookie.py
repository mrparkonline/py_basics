# Cookie Selling Program

# input
start = float(input('Enter your starting money: '))
num_cookies = input('Enter the number of cookies sold: ')
num_big = input('Enter the number of big cookies sold: ')

# processing
total_cookies = len(num_cookies) + len(num_big)

profit_cookies = len(num_cookies) * 1.25 - len(num_cookies) * 0.50
profit_big = len(num_big) * 2 - len(num_big) * 0.75
total_profit = profit_cookies + profit_big

total_money = start + total_profit

# output
print('We sold', total_cookies, 'cookies.')
print('Our profit was:', total_profit)
print('We now have:', total_money)