
# euler problem 21
# some theoretical background: http://en.wikipedia.org/wiki/Amicable_numbers

def get_div(n):

    div_list = []

    for j in range(1, n//2 + 1):
        if n % j == 0:
            div_list.append(j)
    
    return div_list

pairs = []

for num in range(2, 10000):

    if num not in pairs:
        
        sum_a = sum(get_div(num))
        sum_b = sum(get_div(sum_a))

        if sum_b == num and num != sum_a:
            
            pairs.append(num)
            pairs.append(sum_a)
            
            print(str(num) + ', ' + str(sum_a))

print('\nsum: ' + str(sum(pairs)))

        
