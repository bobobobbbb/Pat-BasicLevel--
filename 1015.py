#python3
#1015翻转列表
#测试通过
class Data():
    def __init__(self, Addr, Data, Next):
        self.Addr = Addr
        self.Data = Data
        self.Next = Next

def getData(Next):
    for data in Data_lst:
        if data.Addr == Next:
            return data
    return None
    
def sortData_lst(StaAddr):
    sortedData_lst = list()
    StaData = getData(StaAddr)
    sortedData_lst.append(StaData)
    while StaData.Next != '-1':
        StaData = getData(StaData.Next)
        sortedData_lst.append(StaData)
    return sortedData_lst

def reverseData_lst(sortedData_lst, K):
    resultData_lst = list()
    while len(sortedData_lst) >= K:
        partialList = sortedData_lst[:K]
        partialList.reverse()
        resultData_lst.extend(partialList)
        sortedData_lst = sortedData_lst[K:]
    resultData_lst.extend(sortedData_lst)
    return resultData_lst

def changeNext(reversedData_lst):
    index = 0
    listLen = len(reversedData_lst)
    for data in reversedData_lst:
        if index != listLen - 1:
            data.Next = reversedData_lst[index + 1].Addr
        index += 1
    reversedData_lst[listLen - 1].Next = '-1'
    return reversedData_lst
    

line1 = input()
StaAddr_str, N_str, K_str = line1.split()
K = int(K_str)
N = int(N_str)
Data_lst = list()

while N:
    newLine_lst = input().split()
    a = Data(newLine_lst[0], newLine_lst[1], newLine_lst[2])
    Data_lst.append(a)
    N -= 1
sortedData_lst = sortData_lst(StaAddr_str)
reversedData_lst = reverseData_lst(sortedData_lst, K)
changeNext_lst = changeNext(reversedData_lst)
for data in changeNext_lst:
    print(data.Addr, data.Data, data.Next)
