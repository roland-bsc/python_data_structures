filename = input("Enter file:")
if len(filename) < 1:
    name = "mbox-short.txt"

handle = open(filename)

email_counts = dict()

for line in handle:
    if not line.startswith('From '): 
        continue
    words = line.split()
    email = words[1]
    if email not in email_counts:
        email_counts[email] = 1
    else:
        email_counts[email] += 1

#print(email_counts)

max_key = max(email_counts, key=email_counts.get) #find the key with the highest value using max() method

print(max_key, email_counts.get(max_key,0)) #print(key with highest value, get the value of the key using get() method