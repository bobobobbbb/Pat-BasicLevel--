#python2
#1011.个位数统计

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = raw_input()
for num in nums:
    n = s.count(num)
    if n > 0:
        print num + ':' + str(n)

