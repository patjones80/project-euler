

# project euler 27, quadratic primes

# is there any better optimization than just confining b to primes?

def is_prime(m):

     # uses brute force, checking every number up to sqrt(n)
      
    j = 2

    m = abs(m)
    
    while j < int(m**0.5) + 1:
        if m % j == 0:
            return False
        else:
            j += 1

    return True


# make list of primes from -999 to 999 ahead of time

primes = []

for j in range(-999, 1000):
    if is_prime(j):
        primes.append(j)

# use a tuple to store the combination of a, b with highest n

high_count  = (0, 0, 0)

for b in primes:
    for a in range(-999, 1000):

        n = 0

        while is_prime(n**2 + a*n + b):
            n += 1
            
        if n > high_count[2]:
            high_count = (a, b, n)

print('a: ' + str(high_count[0]) + ' b: ' + str(high_count[1]) + ' n: ' + str(high_count[2]) + '\n')
print('a x b: ' + str(high_count[0]*high_count[1]))


        
