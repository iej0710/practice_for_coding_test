import heapq
import sys

n = int(input())

card = []
for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline().rstrip()))
ans = 0
while len(card) > 1:
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)
    ans += c1 + c2
    heapq.heappush(card, c1 + c2)

print(ans)