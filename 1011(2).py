#python3
#用python3重写一遍
nums = '0123456789'
s = input()
for num in nums:
    n = s.count(num)
    if n > 0:
        print(num, ":", n)