from collections import deque

n = int(input())
schedule = []
for i in range(n):
    schedule.append(list(map(int, input().split())))

cand = deque()
cand.append([1, 0])
max_res = 0

while len(cand) > 0:
    day, cost = cand.popleft()
    if day > n + 1:
        continue
        #max_res = max(max_res, cost)
    elif day == n + 1:
        #if schedule[day - 1][0] == 1:
        #    max_res = max(max_res, cost + schedule[day - 1][1])
        #else:
        max_res = max(max_res, cost)
    else:
        cand.append([day + schedule[day - 1][0], cost + schedule[day - 1][1]])
        cand.append([day + 1, cost])

print(max_res)