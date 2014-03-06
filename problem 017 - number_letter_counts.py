
# Determine the total number of characters used to spell out the numbers 1 through 1000 inclusive phonetically.

# No spaces or punctuation, with the word 'and' included where applicable.

# http://projecteuler.net/problem=17


d = {  1 : 'one' ,
       2 : 'two' ,
       3 : 'three' ,
       4 : 'four',
       5 : 'five',
       6 : 'six',
       7 : 'seven',
       8 : 'eight',
       9 : 'nine',
      10 : 'ten',
      11 : 'eleven',
      12 : 'twelve',
      13 : 'thirteen',
      14 : 'fourteen',
      15 : 'fifteen',
      16 : 'sixteen',
      17 : 'seventeen',
      18 : 'eighteen',
      19 : 'nineteen',
      20 : 'twenty',
      30 : 'thirty',
      40 : 'forty',
      50 : 'fifty',
      60 : 'sixty',
      70 : 'seventy',
      80 : 'eighty',
      90 : 'ninety',
     100 : 'hundred' }

s = ''

for n in range(1,1000):
    
    if n // 100 >= 1:
        s = s + str(d[n // 100]) + 'hundred'    
        n = n % 100
        if n > 0:
            s = s + 'and'

    if n // 10 >= 2:
        s = s + str(d[n - n % 10])
        n = n % 10

    if n > 0:
        s = s + str(d[n])

s = s + 'onethousand'

print(s + '\n')
print('string length: ' + str(len(s)))


    

    

