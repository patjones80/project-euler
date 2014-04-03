
# open file

f = open('C:\\Python32\\text_file_inputs\\project euler 013.txt', 'r')

large_sum = 0

for line in f:
    large_sum = large_sum + int(line)

print('sum: ' + str(large_sum) + '\n')

f.close()


