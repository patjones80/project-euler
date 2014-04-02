
# Recycled code from Problem 20 (Factorial Sums)

# http://projecteuler.net/problem=16


def order_of(b):                            # function to determine the order of b
    i = 0
    
    while b / (10**i) > 10:
        i = i + 1

    return i

M = 2**1000
max_order = order_of(M)

num = M
f_sum = 0

for j in range(max_order, -1, -1):          # start with the highest power of 10 to get the first digit, then work down
    
    f_sum = f_sum + num // 10**j            # add the j-th digit to the running sum
    num = num % 10**j                       # this essentially peels the first digit off the sequence
                                        
print('\nThe sum of the digits in ' + str(M) + ' is ' + str(f_sum) + '\n')
