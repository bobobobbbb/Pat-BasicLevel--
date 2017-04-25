#python3

def find_key(dictID, value):
    for i in dictID:
        if dictID[i] == value:
            return i
    return None

line1_str = input()
line1_lst = line1_str.split()
moonCakeKind = int(line1_lst[0])
MarketRequirTon = int(line1_lst[1])

line2_str = input()
moonCakeTon_str = line2_str.split()
moonCakeTon = []
for i in moonCakeTon_str:
    moonCakeTon.append(int(i))

line3_str = input()
moonCakeStorage_str = line3_str.split()
moonCakeStorage = []
for i in moonCakeStorage_str:
    moonCakeStorage.append(int(i))

TonToStorage_dict = dict(zip(moonCakeTon, moonCakeStorage))
UnitPrice_lst = []
for Ton, Storage in zip(moonCakeTon, moonCakeStorage):
    result = Ton / Storage
    UnitPrice_lst.append(result)

TonToUP_dict = dict(zip(moonCakeTon, UnitPrice_lst))

totalMoney = 0
CurrentRequirTon = MarketRequirTon
while CurrentRequirTon > 0:
    maxUnitPrice = max(UnitPrice_lst)
    UnitPrice_lst.pop(UnitPrice_lst.index(maxUnitPrice))
    if maxTon >= CurrentRequirTon:
        CurrentRequirTon * 

