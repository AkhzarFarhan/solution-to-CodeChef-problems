import sys

t = int(input())
for i in range(t):
    n = int(input())
    temp = n // 5
    a = temp
    while temp >= 5:
        res = temp // 5
        a += temp
    print(a)
#Success