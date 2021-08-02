import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
idx_list = []
res = [-1] * N
for i in range(N):

    while len(idx_list) > 0:
        if arr[i] > arr[idx_list[-1]]:
            res[idx_list.pop()] = arr[i]
        else:
            idx_list.append(i)
            break
    if len(idx_list) == 0:
        idx_list.append(i)

for i in res:
    print(i,end=' ')