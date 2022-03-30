# link - https://www.acmicpc.net/problem/1654
import sys

def binary_search(lan, src, dst, target):
    global max_len
    mid = (src + dst) // 2

    if src > dst:
        return 0

    count = 0
    for l in lan:
        count += l // mid

    if count >= target:
        max_len = max(mid, max_len)
        binary_search(lan, mid + 1, dst, target)
    else:
        binary_search(lan, src, mid - 1, target)


k, n = map(int, input().split())
lans = []

for i in range(k):
    lans.append(int(sys.stdin.readline().rstrip()))

max_len = 0
binary_search(lans, min(lans) // (n // k + 1), max(lans) // (n // k) + 1, n)

print(max_len)