#python3
#1018.人口普查
#测试通过
from datetime import datetime
from datetime import timedelta

#birth为datetime数据
class Person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

today = datetime(2014, 9, 6)
population = int(input())
people_lst = []
while population:
    population -= 1
    line1_lst = input().split()
    birth = datetime.strptime(line1_lst[1], '%Y/%m/%d')
    if birth < datetime(1814, 9, 6) or birth > today:
        continue
    p = Person(line1_lst[0], birth)
    people_lst.append(p)
people_lst.sort(key = lambda x: x.birth)    
print(len(people_lst), people_lst[0].name, people_lst[-1].name)