x, b = map(int, input().split())

if x == 0:
    print(0)

else:
    res = ''
    idx = 0
    flag = 1
    if x < 0 and b > 0:
        flag = 0
        x *= -1
    while abs(x) > 0:
        num = (x % abs(b))
        res = str(x % abs(b)) + res
        x = (x - num) // b
        idx += 1
    if flag == 0:
        print('-' + res)
    else:
        print(res)