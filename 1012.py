#python3

a, b, d = tuple(raw_input().split(' '))
a = int(a)
b = int(b)
d = int(d)
c = a + b
n = 0
i = 1
while c > 0:
    n += (c % d * i)
    c /= d
    i *= 10
 
print n