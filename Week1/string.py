data = 'From coy.abellano@gmail.com Tues Nov 9 09:55:31 2021'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)