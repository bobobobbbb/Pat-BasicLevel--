#python3.5.2
from itertools import chain

def compute_cb(A, B):
    global A_cb, B_cb, B_cb_dic, A_cb_dic
    if A == 'J':
        if B == 'B':
            A_cb[0] += 1
            B_cb[2] += 1
            A_cb_dic['J'] += 1
        elif B == 'C':
            A_cb[2] += 1
            B_cb[0] += 1
            B_cb_dic['C'] += 1
        else:
            A_cb[1] += 1
            B_cb[1] += 1
    elif A == 'B':
        if B == 'C':
            A_cb[0] += 1
            B_cb[2] += 1
            A_cb_dic['B'] += 1
        elif B == 'J':
            A_cb[2] += 1
            B_cb[0] += 1
            B_cb_dic['J'] += 1
        else:
            A_cb[1] += 1
            B_cb[1] += 1
    else:                 #when A == 'C'
        if B == 'B':
            A_cb[2] += 1
            B_cb[0] += 1
            B_cb_dic['B'] += 1
        elif B == 'J':
            A_cb[0] += 1
            B_cb[2] += 1
            A_cb_dic['C'] += 1
        else:
            A_cb[1] += 1 
            B_cb[1] += 1

def returnMaxKey(X_dic):
    list1 = list()
    if X_dic['B'] >= X_dic['J'] and X_dic['B'] >= X_dic['C']:
        return 'B'
    elif X_dic['C'] >= X_dic['J']:
        return 'C'
    else:
        return 'J'


count = int(input())
A_list = []
B_list = []
A_cb_dic = {'C':0,'J':0,'B':0}
B_cb_dic = {'C':0,'J':0,'B':0}
for i in range(count):
    line_str = input()
    line_ls = line_str.split()
    A_list.append(line_ls[0])
    B_list.append(line_ls[1])

A_cb = [0,0,0]
B_cb = [0,0,0]   #combcat gains
for A, B in zip(A_list, B_list):
    compute_cb(A, B)

for A in A_cb:
    print(A, end = " ")
print()
for A in reversed(A_cb):
    print(A, end = " ")
print()

print(returnMaxKey(A_cb_dic), " ", returnMaxKey(B_cb_dic))