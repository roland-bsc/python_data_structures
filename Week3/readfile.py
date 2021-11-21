xfile = open('test.txt')

count = 0

for line in xfile:
    count = count + 1

print('Line counter: ', count)

