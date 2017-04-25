#python3
#组个最小数

InputNums = input().split()
minNum_str = ''
while InputNums:
    minNum_char = min(InputNums)    
    minNum_str += minNum_char
    InputNums.remove(minNum_char)

if minNum_str.startswith('0'):
    index = 0
    for i in minNum_str:
        if i != '0':
            fristNonZero = i
            break
        index += 1
    minNum_str = fristNonZero + minNum_str[:index] + minNum_str[index + 1:]
    print(minNum_str)
else:
    print(minNum_str)