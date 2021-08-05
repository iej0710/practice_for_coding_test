from queue import deque
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
seq = list(map(int,sys.stdin.readline().rstrip().split()))

que = deque([i for i in range(1,n+1)])

res = 0
flag = 1
for i in range(len(seq)):
    tmp = 0
    while que[0] != seq[i]:
        que.rotate(1)
        tmp += 1
    if tmp > len(que) // 2:
        res += abs(tmp - len(que))
    else:
        res += tmp
    que.popleft()


print(res)