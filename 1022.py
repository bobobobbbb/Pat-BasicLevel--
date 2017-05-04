#!/usr/bin/env python3
#1022.挖掘机技术哪家强
#未测试

def getMaxValueKey(a_dict):
    maxValue = 0
    valueKey = None
    for key, value in a_dict.items():
        if value > maxValue:
            valueKey = key
    return valueKey


if __name__ == "__main__":
    participationNum = int(intput())
    gradeTable = dict()
    while participationNum:
        line = input().split()
        if gradeTable.has_key(line[0]):
            gradeTable[line[0]] += int(line[1])
        else:
            gradeTable.setdefault(line[0], int(line[1]))
        participationNum -= 1
    key = getMaxValueKey(gradeTable)
    print(key, gradeTable[key])
    
    