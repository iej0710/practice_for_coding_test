import sys

A, B, C = map(int,sys.stdin.readline().rstrip().split())

x = 0

if C - B <= 0:
    print(-1)
else:
    print(A // (C-B) + 1)
