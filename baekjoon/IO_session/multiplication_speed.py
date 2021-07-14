import sys

T = int(input())

for i in range(int(T)):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{}: {}'.format(i+1,a + b))
