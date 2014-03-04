
# factorial sums 

def fact(N):                                # function to determine the factorial of N (recursive)
    if N == 1:
        return 1
    else:
        return N*fact(N-1)

def order_of(b):                            # function to determine the order of b
    i = 0
    
    while b / (10**i) > 10:
        i = i + 1

    return i

print()

M = 100
f = fact(int(M))

max_order = order_of(f)

num = f
f_sum = 0

for j in range(max_order, 0, -1):           # start with the highest power of 10 to get the first digit, then work down
 
    f_sum = f_sum + num // 10**j            # add the j-th digit to the running sum
    num = num % 10**j                       # this essentially peels the first digit off the sequence

                                            
print('The factorial of ' + str(M) + ' is ' + str(f))
print('The sum of the digits in that factorial is ' + str(f_sum))

print()


    
