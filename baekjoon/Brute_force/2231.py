n = int(input())

res = 0
flag = 0
for i in range(n+1):
    res = i
    tmp = i
    while tmp > 0:
        res += tmp % 10
        tmp = tmp // 10
    if res == n:
        print(i)
        flag = 1
        break

if flag == 0:
    print(0)