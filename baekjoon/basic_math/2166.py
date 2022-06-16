##신발끈 공식
## 정답아님...

import sys

N = int(input())

pos = []
for i in range(N):
    pos.append(list(map(int, sys.stdin.readline().rstrip().split())))

res = 0

for i in range(N - 1):
    res += pos[i][0] * pos[i + 1][1] - pos[i + 1][0] * pos[i][1]

print('{:.1f}'.format(abs(res) / 2))