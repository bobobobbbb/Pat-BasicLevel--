#python 3
#Pat乙级真题 
#1009.1019数字黑洞
#14/20

def getProgressiveNumberStr(a_str):
    rel_str = ''
    a_lst = list(a_str)
    while a_lst:
        a = max(a_lst)
        rel_str += a
        a_lst.pop(a_lst.index(a))
    return rel_str

def getDecreaseNumberStr(a_str):
    rel_str = ''
    a_lst = list(a_str)
    while a_lst:
        a = min(a_lst)
        rel_str += a
        a_lst.pop(a_lst.index(a))
    return rel_str

def getResultStr(Inc_str, Dec_str):
    result_int = int(Inc_str) - int(Dec_str)
    result_str = str(result_int)
    while len(result_str) < 4:
        result_str = '0' + result_str
    return result_str

InputNum = input()
if InputNum == InputNum[0] * 4:
    print(InputNum + ' - ' + InputNum + ' = 0000')
else:    
    increase_str = getProgressiveNumberStr(InputNum)
    decrease_str = getDecreaseNumberStr(InputNum)

    while True:
        result_str = getResultStr(increase_str, decrease_str)
        print(increase_str + ' - ' + decrease_str + ' = ' + result_str)
        increase_str = getProgressiveNumberStr(result_str)
        decrease_str = getDecreaseNumberStr(result_str)
        if result_str == '6174':
            break

