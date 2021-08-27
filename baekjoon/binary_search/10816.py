import sys
from collections import Counter

def search(arr,x,src,dst):
    if arr[src] == x:
        return 1
    else:
        if abs(src - dst) <= 1:
            return 0
    idx = (src + dst) // 2
    if arr[idx] > x:
        return search(arr,x,src,idx)
    else:
        return search(arr,x,idx,dst)

n = int(input())
A = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(input())
B = list(map(int,sys.stdin.readline().rstrip().split()))

answer = []
A_count = Counter(A)
A = sorted(list(A_count.keys()))

for i in B:
    try:
        print(A_count[i],end=' ')
    except:
        print(0,end=' ')