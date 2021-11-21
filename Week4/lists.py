friends = ['Joseph', 'Mary', 'Gless', "Salleh"]

#this loop goes through a set
for friend in friends:
    print('Happy New Year,', friend)

print ('_______________________')

#this loop goes through the number index of the list (i.e. counted loop)
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year ->', friend)
