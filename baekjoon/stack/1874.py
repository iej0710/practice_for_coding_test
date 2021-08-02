n = int(input())

arr = []
seq = []
for i in range(n):
    seq.append(int(input()))

element = 1
idx = 0
res = []
flag = 1
while len(seq) > idx:
    if  len(arr) == 0:
        arr.append(element)
        element += 1
        res.append('+')
    if arr[-1] == seq[idx]:
        arr.pop()
        res.append('-')
        idx += 1
    elif arr[-1] > seq[idx]:
        print('NO')
        flag = 0
        break
    else:
        arr.append(element)
        res.append('+')
        element += 1

if flag == 1:
    for i in res:
        print(i)