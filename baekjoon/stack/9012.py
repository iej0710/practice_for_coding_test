T = int(input())

for i in range(T):
    arr = []
    flag = 1
    s = input()
    for j in s:
        if j == '(':
            arr.append(j)
        elif j == ')' and len(arr) > 0:
            arr.pop()
        elif j == ')' and len(arr) == 0:
            flag = 0
            break
    if len(arr) == 0 and flag == 1:
        print('YES')
    else:
        print('NO')