import sys

pos = []

for i in range(3):
    pos.append(list(map(int, sys.stdin.readline().rstrip().split())))
res = 0
for i in range(3):
    res += pos[i][0] * pos[(i + 1) % 3][1] - pos[i][1] * pos[(i + 1) % 3][0]

if res > 0:
    print(1)
elif res == 0:
    print(0)
else:
    print(-1)