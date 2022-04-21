from collections import deque
import math

wheel = []
for i in range(4):
    wheel.append(deque(list(map(int, list(input())))))

k = int(input())
for i in range(k):
    idx, direction = map(int, input().split())
    idx -= 1
    right, left = wheel[idx][2], wheel[idx][6]
    wheel[idx].rotate(direction)
    move = idx
    d = direction
    while move < 3:
        move += 1
        if right != wheel[move][6]:
            right = wheel[move][2]
            d = -d
            wheel[move].rotate(d)
        else:
            break
    d = direction
    move = idx
    while 0 < move:
        move -= 1
        if left != wheel[move][2]:
            left = wheel[move][6]
            d = -d
            wheel[move].rotate(d)
        else:
            break
score = 0
for idx in range(4):
    if wheel[idx][0] == 1:
        score += math.pow(2, idx)

print(int(score))