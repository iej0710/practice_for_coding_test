import heapq
import sys

n = int(input())
left = []
right = []
for i in range(n):
    mid = int(sys.stdin.readline().rstrip())

    if len(left) == len(right):
        heapq.heappush(left, -mid)
    else:
        heapq.heappush(right, mid)

    if len(right) > 0:
        right_min = heapq.heappop(right)
        left_max = -heapq.heappop(left)
        if left_max > right_min:
            heapq.heappush(left, -right_min)
            heapq.heappush(right, left_max)
        else:
            heapq.heappush(left, -left_max)
            heapq.heappush(right, right_min)
    res = -heapq.heappop(left)
    heapq.heappush(left, -res)
    print(res)