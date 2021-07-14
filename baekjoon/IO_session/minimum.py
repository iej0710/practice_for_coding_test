import sys

n,x = map(int,sys.stdin.readline().rstrip().split())

A = sys.stdin.readline().rstrip().split()

for i in range(n):
    if int(A[i]) < x:
        print(int(A[i]),end=' ')