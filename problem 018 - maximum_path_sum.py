

def get_max(j, level, t, sum_0):

    global max_sum
    
    for k in range(j, j+2):

        path_sum = sum_0 + t[level][k]
            
        if level == len(t)-1:
            if path_sum > max_sum:
                max_sum = path_sum

        else:
            get_max(k, level+1, t, path_sum)

# initializations

f = open('C:\\Users\\Pat\\Desktop\\triangle_1.txt', 'r')
triangle = []
max_sum = 0

# read triangle into list

for line in f:
    row = [int(s) for s in line.split()]
    triangle.append(row)

# call max procedure

sum_0 = triangle[0][0]
get_max(0, 1, triangle, sum_0)

print(str(max_sum))

