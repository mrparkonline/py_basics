#Program the following minimum credit card payment protocol. 

# The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is GREATER; but if this exceeds the balance, then the minimum payment is the balance. 

# Write a program to print out the minimum payment using min() and max(). Assume that the variable balance contains the customer's balance. Your program does not need to print the dollar sign.

# Example 1: if your balance is 1000, then your program should print 21. 
# Example 2: if your balance is 25, then your program should print 10.

# input
balance = float(input('Enter your balance: '))

# processing
payment_percent = balance * 0.021 # 2.1% 

fee = max(min(10, balance), payment_percent)
# output
print('Your fee is:', fee)