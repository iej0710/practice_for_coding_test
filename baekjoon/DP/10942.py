import sys
def print_map(A):
    for a in A:
        print(a)
    print()


N = int(input())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
'''with open('boj10942_tle-20582490.in','r') as f:
    N = int(f.readline().rstrip())
    arr = list(map(int, f.readline().rstrip().split()))
    M = int(f.readline().rstrip())

    q = []
    for i in range(M):
        q.append(list(map(int, f.readline().rstrip().split())))'''


p = [[0] * N for i in range(N)]

for i in range(N):
    p[i][i] = 1
    if i < N - 1 and arr[i] == arr[i + 1]:
        p[i][i + 1] = 1

for d in range(1, N):
    for i in range(N - d):
        j = i + d
        if p[i + 1][j - 1] == 1 and arr[i] == arr[j]:
            p[i][j] = 1

'''
with open('boj10942_tle-20582490.out', 'r') as f:
    count = 0
    for s, e in q:
        answer = int(f.readline().rstrip())
        if answer == p[s - 1][e - 1]:
            count += 1

print('{} / {} correct. {} % accuracy'.format(count, M, count / M * 100))'''

M = int(input())

for q in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())

    if p[s - 1][e - 1] == 1:
        print(1)
    else:
        print(0)