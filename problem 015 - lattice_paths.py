
# This is really more of a math problem than anything else, with very little code needed to solve it. Here's one
# approach to it...

# Let 0 = one rightward movement, and 1 = one downward movement. Using this scheme, each path can be represented
# using sequences of 0's and 1's. For the 2 x 2 grid given in the problem, the six possible paths are:

# 0011, 0101, 0110, 1001, 1010, 1100

# Clearly, an N x N grid requires a sequence 2N digits long, and will have equal numbers of 0's and 1's.

# For the 20 x 20 grid, the possible paths will have various combinations of 20 "distinct" 1's embedded in 40 digit bits
# strings. This thus becomes a problem of calculating the combination

# (n k) = n! / (k!*(n-k)!)

# where n = 40 and k = 20. This reduces to 40!/20!*20!, which the code below calculates.

# Note: elapsed time for the calculation on HP quad core was ~ 0.0000594 sec.

import time

def fact(N):

    if N == 1:
        return N
    else:
        return N*fact(N-1)

start = time.clock()

paths = fact(40)/(fact(20)*fact(20))

elapsed = time.clock() - start

print('nCk = ' + str(paths) + '\n\n')
print('Elapsed time: ' + str(elapsed))


