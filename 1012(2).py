#python3

a, b, c = tuple(input().split())
a = int(a)
b = int(b)
c = int(c)
n = 0
i = 1
total = a + b
while total > 0:
    n += (total % c * i)
    total //= c
    i *= 10

print(n)