from itertools import permutations
import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

for seq in list(permutations(range(1,N+1),M)):
    for s in seq:
         print(s,end=' ')
    print()

