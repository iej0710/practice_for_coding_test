import sys
arr = list(map(str, sys.stdin.readline().rstrip().split()))

changed = []
for i in arr:
    tmp = 0
    for j in range(len(i)):
        tmp += int(i[j]) * (10**j)
    changed.append(tmp)

print(max(changed))