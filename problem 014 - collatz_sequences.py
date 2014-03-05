
# Project Euler #14, Collatz Sequences

import time

# recursive version (took ~ 42 sec compared to the while loop's 26 sec)

# def get_collatz(n, total):
#        
#    total = total + 1
#
#    if n == 1:
#        return total
#    else:
#        if n % 2:
#            return get_collatz(3*n + 1, total)
#        else:
#            return get_collatz(n//2, total)


def get_collatz(n):
        
    total = 0

    while n > 1:

        total = total + 1
        
        if n % 2:
            n = 3*n + 1
        else:
            n = n//2

    return total

prev = 0,0
start = time.clock()

for j in range(999999, 1, -1):

    seq_len = get_collatz(j)
    
    if seq_len > prev[1]:
        prev = j,seq_len    

end = time.clock() - start

print ('number: ' + str(prev[0]) + '\n')
print ('stopping time: ' + str(prev[1]) + '\n')
print ('process time: ' + str(end))



