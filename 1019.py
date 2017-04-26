#python3
#1019.旧键盘
#测试通过
line1 = input()
line2 = input()

ruinedKey_lst = list()
index = 0
for i in line1:
    if i != line2[index]:
        ruinedKey_lst.append(i)
        continue
    index += 1
    if index >= len(line2):
        index -= 1

ruinedKey_lst2 = list()
for i in ruinedKey_lst:
    if i.isalpha():
        ruinedKey_lst2.append(i.upper())
    else:
        ruinedKey_lst2.append(i)

printed_lst = list()
for i in ruinedKey_lst2:
    if i not in printed_lst:
        print(i, end = '')
        printed_lst.append(i)
    else:
        pass
    