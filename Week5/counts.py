counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    #this is a EXPLICIT way to look for new keys in a dictionary
    # if name not in counts:
    #     counts[name] = 1
    # else:
    #     counts[name] = counts[name] + 1

    #this is the elegant way of looking for new keys in a dict()
    counts[name] = counts.get(name, 0) + 1
    
print(counts)