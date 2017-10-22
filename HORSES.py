t = int(input())
for i in range(t):
    n = int(input())
    s = [int(j) for j in input().split()]
    d = []
    s.sort()
    for k in range(n-1):
        d.append(s[k+1] - s[k])
    print(min(d))

#Success
