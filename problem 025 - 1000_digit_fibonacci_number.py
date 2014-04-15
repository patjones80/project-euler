
# project euler 25

# completely brute force = about 40 sec run time; clearly need an optimization

import time

start = time.clock()

F = (1, 1, 2)
j = 3

while len(str(F[2])) < 1000:          
    F = (F[1],F[2],F[1]+F[2])
    j=j+1
    print('F[%s]: %s' % (str(j),F[2]))
         
print('\ntime: %s' % str(time.clock()-start))

