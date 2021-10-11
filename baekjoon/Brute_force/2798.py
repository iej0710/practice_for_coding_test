import sys
from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

delta = m

for seq in permutations(arr,3):
    if 0 <= m - sum(seq) < delta:
        delta = m-sum(seq)
        res = sum(seq)

print(res)