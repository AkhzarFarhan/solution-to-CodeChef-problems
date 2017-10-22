a, b = map(int, input().split())
d = a - b
if d % 10 == 9:
     w = d - 1
elif d % 10 == 0:
    w = d + 1
else:
    w = d + 1
print(w)
#Success