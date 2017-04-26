#python3 
#1020.完美数列

p = int(input().split()[1])
num_lst = input().split()
for index in range(len(num_lst)):
    num_lst[index] = int(num_lst[index])
maxNum_lst = list()
while num_lst:
    maxNum = 1
    minNum = min(num_lst)
    num_lst.remove(minNum)
    for i in num_lst:
        if i <= (p * minNum):
            maxNum += 1
    maxNum_lst.append(maxNum)
print(max(maxNum_lst))
