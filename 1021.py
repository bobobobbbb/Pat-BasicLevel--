#!/usr/bin/env python3
#未测试
if __name__ == "__main__":
    line = int(input())
    IDcodeList = list()
    while line:
        IDcode = input()
        IDcodeList.append(IDcode)
        line -= 1
    weight_list = [7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2]
    sum_lst = list()
    for i, IDcode in enumerate(IDcodeList):
        sum = 0
        for char in IDcode:
            if not char.isdigit():
                sum = -1
                break
            sum += weight_list[i] * int(char)
        sum_list.append(sum)
    Z_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #M: 1 0 X 9 8 7 6 5 4 3 2
    M_lst = ['1', '0', 'X', '9', '8', '7', '6', '5', '3', '2', '1']
    ZM_dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'5', 7:'3', 8:'2', 9:'2', 10:'1'}
    afterMod_lst = [(i % 11) for i in sum_lst]
    valid_IDcode = list()
    for i ,afterModNum in enumerate(afterMod_lst):
        if ZM_dict[afterModNum] == IDcodeList[i][-1]:
            print(IDcodeList[i])
    



