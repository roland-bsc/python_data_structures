d = dict()
d['csev'] = 2
d['cwen'] = 4
d['zhang'] = 11
d['abellano'] = 2
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(f"Unsorted ${tups}")
tups = sorted(d.items())
print(f"Sorted ${tups}")