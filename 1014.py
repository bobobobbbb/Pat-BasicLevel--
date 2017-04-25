#python3

s = input()
a = float(s)
index = s.find('E')
E = int(s[index + 1:])
zeroCount = 0
precise = index - E - 3
outputPat = '%' + '.' + str(precise) + 'f'
print(outputPat % a)