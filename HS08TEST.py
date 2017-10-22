numbers = [int(i) if i.isdigit() else float(i) for i in input().split()]
x = numbers[0]
y = numbers[1]
x = float(x)
if x % 5 != 0:
    print('% .2f' % y)
else:
    if x > y-0.50:
        print('% .2f' % y)
    else:
        print('% .2f' % (y-x-0.50))
#Success