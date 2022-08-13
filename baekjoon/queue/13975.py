import sys
import heapq

T = int(input())

for test_case in range(T):
    n = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().rstrip().split()))

    heapq.heapify(files)
    res = 0
    while len(files) > 1:
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        res += f1 + f2
        heapq.heappush(files, f1 + f2)

    print(res)