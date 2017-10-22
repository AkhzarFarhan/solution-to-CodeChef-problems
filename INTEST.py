numbers = list(map(int, input().split()))
count = 0
a = []
for i in range(numbers[0]):
    a.append(int(input()))
for j in range(numbers[0]):
    if a[j] % numbers[1] == 0:
        count += 1
print(count)
#Success