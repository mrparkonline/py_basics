# ISBN

# 9×1+7×3+8×1+0×3+9×1+2×3+1×1+4×3+1×1+8×3+ 9×1+4×3+8×1=120
# 120 - 9 - 12 - 8 = 91

# input
first_digit = int(input('Enter your first digit: '))
second_digit = int(input('Enter your second digit: '))
third_digit = int(input('Enter your third digit: '))

# processing
isbn = 91 + (first_digit * 1) + (second_digit * 3) + (third_digit * 1)

# output
print('The ISBN number is:', isbn)