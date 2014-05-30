
def name_value(name_in):
    j = 0

    for c in name_in:
        j = j + ord(c) - 64
        
    return j

f = open(r'C:\Python32\text_file_inputs\names.txt','r')

for line in f:
    names = line.replace('"','').split(',')

f.close()

names.sort()
total = 0

for n in names:
    total = total + name_value(n)*(names.index(n)+1)

print(str(total))

