import sys

n = int(input())

card = {}
for i in range(n):
    c = int(sys.stdin.readline().rstrip())
    if c in card.keys():
        card[c] += 1
    else:
        card[c] = 1

card = sorted(card.items(), key=lambda x: (-x[1], x[0]))
print(card[0][0])