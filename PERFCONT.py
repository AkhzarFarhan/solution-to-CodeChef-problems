t = int(input())
for i in range(t):
    number = [int(j) for j in input().split()]
    solution_stat = [int(k) for k in input().split()]
    cakewalk = 0
    hard = 0
    for l in range(number[0]):
        if solution_stat[l] >= number[1]//2:
            cakewalk += 1
        elif solution_stat[l] <= number[1]//10:
            hard += 1
        else:
            continue
    if cakewalk == 1:
        if hard == 2:
            print("yes")
        else:
            print("no")
    else:
        print("no")

#Success
