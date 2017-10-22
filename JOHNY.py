t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    k = int(input())
    initial = a[k-1]
    a.sort()
    for l in range(n):
        if a[l] == initial:
            temp = l+1
            break
    print(temp)

#Success