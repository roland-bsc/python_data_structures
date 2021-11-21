# Solution1
# text = "X-DSPAM-Confidence:    0.8475"
# pos1 = text.find('0')
# pos2 = text.find('5')
# print("pos1: ", pos1)
# print("pos2: ", pos2)
# extractednum =  text[pos1 : pos2 +1]
# print(float(extractednum))

# Solution2 = shorter code
text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find(':')
extractednum = text[pos1+2:] # slice pos1 plus 2 positions from pos1
print(float(extractednum))