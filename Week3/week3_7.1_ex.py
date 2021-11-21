# Use words.txt as the file name
#reads words.txt and then prints it in UPPERCASE
fname = input("Enter file name: ")
try:
    fh = open(fname)
    for line in fh:
        line = line.rstrip()
        print(line.upper())
except:
    print('File cannot be opened:', fname)
    exit()
