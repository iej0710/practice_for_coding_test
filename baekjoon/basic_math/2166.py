##신발끈 공식 (CCW 공식)

import sys

N = int(input())

pos = []
for i in range(N):
    pos.append(list(map(int, sys.stdin.readline().rstrip().split())))

res = 0

for i in range(N - 1):
    res += pos[i][0] * pos[i + 1][1] - pos[i + 1][0] * pos[i][1]

res += pos[-1][0] * pos[0][1] - pos[0][0] * pos[-1][1]
print('{:.1f}'.format(abs(res) / 2))