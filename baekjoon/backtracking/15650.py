from itertools import combinations
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

for seq in list(combinations(range(1,N+1),M)):
    for s in seq:
         print(s,end=' ')
    print()

