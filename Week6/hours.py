fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()

for line in fh:
    if not line.startswith('From '): 
        continue
    words = line.split()
    time_stamp = words[5]
    time_pieces = time_stamp.split(":")
    hour = time_pieces[0] 
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for val,key in lst:
    print(val,key)