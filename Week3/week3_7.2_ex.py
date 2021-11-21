# Use the file name mbox-short.txt as the file name
#return value of script is average DSPAM confidence number
fname = input("Enter file name: ")
try:
    fh = open(fname)
    count = 0
    total_conf = 0.0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        confidence = float(line[20:])
        total_conf = total_conf + confidence
        count = count + 1
    print("Average spam confidence:", total_conf/count)
except:
    print('File cannot be opened:', fname)
    exit()