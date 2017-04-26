#python3 
#1017.打印沙漏
#测试通过
def getSandClockLevel(Num):
    Level = 1
    total = 1
    if Num == 1:
        return Level
    while total <= Num:
        Level += 1
        total += (2 * Level - 1) * 2
    return Level - 1

def getRest(Num, Level):
    requir = 1
    if Level == 1:
        return Num - Level
    for i in range(2, Level + 1):
        requir += (i * 2 - 1) * 2
    
    return Num - requir
            
def printSandClock(level, symbol):
    currentLevel = level
    space = 0
    while currentLevel > 1:
        print(space * ' ', end = '')
        print((currentLevel * 2 - 1) * symbol)
        currentLevel -= 1
        space += 1

    print((space - 1) * ' ', end = ' ')
    print(symbol)
    currentLevel += 1
    space -= 1
    while currentLevel <= level:
        print(space * ' ', end = '')
        print((currentLevel * 2 - 1) * symbol)
        currentLevel += 1
        space -= 1

Num_str, symbol = input().split()
Num = int(Num_str)
level = getSandClockLevel(Num)
rest = getRest(Num, level)
printSandClock(level, symbol)
if rest != 0:
    print(rest)
