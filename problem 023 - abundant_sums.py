
def is_abundant(m):

    # uses brute force, checking every number up to sqrt(n)
      
    j = 1
    k = 0                           # use k as the running sum of the divisors

    m = abs(m)
    
    while j < m/2 + 1:
        if m % j == 0:
            k = k + j
        j = j + 1
        
    if k > m:
        return True

# get all the abundant numbers up to 28,123

A = []
upper = 28124

for n in range(1,upper):
    if is_abundant(n):
        A.append(n)

# get all the sums of the abundant numbers

A_sums = {24}
A_len  = len(A)

j = 0
k = 0

while A[j] < upper/2:
    while A[j]+A[k] < upper:        
        A_sums.add(A[j]+A[k])       # this works because sets don't duplicate values
        k=k+1
    j=j+1
    k=j

q = 0

# determine what is not a sum of abundant numbers and tally them

for p in range(1,upper):
    if p not in A_sums:
        q = q + p

print(str(q))

    
