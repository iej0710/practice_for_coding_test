import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
person = {}
answer = set()
for i in range(n):
    name = sys.stdin.readline().rstrip()
    if name not in person.keys():
        person[name] = 1

for i in range(m):
    name = sys.stdin.readline().rstrip()
    try:
        if person[name]:
            answer.add(name)
    except:
        continue

answer = list(answer)
answer.sort()
print(len(answer))
for name in answer:
    print(name)
