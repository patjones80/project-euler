
# project euler 30

# these numbers turn out to be related to "narcissistic numbers"

# see this for an interesting discussion:
# http://mathworld.wolfram.com/NarcissisticNumber.html

import time

N = 354294
m = 5
total = 0

start = time.clock()

for j in range(2, N+1):

    jlist = list(str(j))
    n = 0

    for k in range(0, len(jlist)):
        digit = int(jlist[k])
        n = n + digit**m
    
    if j == n:
        print('%s: %s' % (j, n))
        total = total + j

print('\nsum: %s' % total)        
print('\ntime: %s' % str(time.clock()-start))
    

            
        
    
    

