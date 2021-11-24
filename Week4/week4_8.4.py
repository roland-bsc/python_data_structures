fname = input("Enter file name: ")
fh = open(fname)          #open the file and assign to filehandle
lst = list()              #create an empty list

for line in fh:           #look thru each line of the file and 
    line = line.rstrip()  #strip trailing whitespaces
    words = line.split()  #split each item in list and put it in words variable
    for word in words:    #loop thru every word in words
        if word in lst:   #if word is already in lst, leave it alone
            continue
        lst.append(word)  #if word is NOT in lst, then append the word in lst

lst.sort()                #sort the lst
print(lst)
