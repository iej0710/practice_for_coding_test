from collections import deque
import sys

n,k = map(int, sys.stdin.readline().rstrip().split())

arr = deque([i for i in range(1,n + 1)])
res = '<'
while len(arr) > 0:
    print(arr)
    arr.rotate(-k + 1)
    res += str(arr.popleft())
    if len(arr) != 0:
        res += ', '

print(res+'>')