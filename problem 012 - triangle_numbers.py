
# euler problem 12

# used prime factorization (see http://www.mathblog.dk/uva-294-divisors/)

# any integer can be factored into powers of prime numbers. for example
# 24 = 2^3 * 3^1.

# number theory says that the number of divisors that an integer can be
# written as a multiplication of those prime powers:

# number of divisors = (a0 + 1) * (a1 + 1) * ...

# in the case of  n = 24, a0 = 3 and a1 = 1, so 24 has (3 + 1)*(1 + 1) or
# 8 divisors (1, 2, 3, 4, 6, 8, 12, 24).


def get_highest_power(n, div):

    # determine the highest power of div that divides into n evenly
    
    j = 0

    while n % div**(j+1) == 0:
        j = j + 1

    return j

def get_div(n):

    # get the prime factorization
    
    primes = [2,3,5,7,11,13,17,19,23,29]    
    n_div  = 1

    for j in primes:
        if n % j == 0:
            n_div = n_div*(get_highest_power(n, j)+1)

    return n_div

j = 0
k = 1
num_div = 0

while num_div < 501:
    j = j + k
    num_div = get_div(j)
    k = k + 1

    print(str(j) + ': ' + str(get_div(j)))
    
    
#def get_div(n):
#
     # uses brute force, checking every number up to sqrt(n)
      
#    a = 0
#
#    for j in range(1, int(n**0.5) + 1):
#        if n % j == 0:
#            a += 1
#
#    if (n**0.5) % 1 == 0:
#        return 2*a - 1
#    else:
#        return 2*a
                
        
        
    


