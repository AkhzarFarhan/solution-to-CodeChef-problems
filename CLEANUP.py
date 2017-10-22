t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    m_index = [int(j) for j in input().split()]
    n_index = []
    chef = []
    assistant = []
    for k in range(1, n+1):
        n_index.append(k)
    nm_index = sorted(list(set(n_index) - set(m_index)))
    for l in range(n-m):
        if l == 0:
            chef.append(nm_index[l])
            temp = 0
            continue
        elif temp == 1:
            chef.append(nm_index[l])
            temp = 0
            continue
        else:
            if temp == 0:
                assistant.append(nm_index[l])
                temp = 1
                continue
    print(*chef)
    print(*assistant)

#Success
