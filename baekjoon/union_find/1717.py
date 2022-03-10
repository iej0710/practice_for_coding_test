import sys

def union(seq, a, b):
    a_root = find_set(seq, a)
    b_root = find_set(seq, b)
    if a_root <= b_root:
        seq[b_root] = a_root
    else:
        seq[a_root] = b_root

def find_set(seq, a):
    if seq[a] == a:
        return a
    else:
        seq[a] = find_set(seq, seq[a])
        return seq[a]

n, m = map(int, input().split())

set_dict = [i for i in range(n + 1)]

for i in range(m):
    operation, a, b = map(int, sys.stdin.readline().rstrip().split())

    if operation == 0:
        union(set_dict, a, b)
    else:
        if find_set(set_dict, a) == find_set(set_dict, b):
            print('YES')
        else:
            print('NO')
