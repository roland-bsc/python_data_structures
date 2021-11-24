fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    #print(line)
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    #print(pieces)
    print('Emails came from these domains: ', pieces[1])