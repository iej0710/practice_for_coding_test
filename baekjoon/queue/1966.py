'''from queue import PriorityQueue ##중요도가 같은 문서들이 있을 경우, 우선순위가 문제와는 다르게 배치됨
import sys

T = int(input())

for i in range(T):
    que = PriorityQueue()
    n, m = map(int,sys.stdin.readline().rstrip().split())
    importance = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        que.put((importance[j],j))
    count = 0
    while que.get()[1] != m:
        count += 1
    if m == 0:
        print(1)
    else:
        print(count)'''

from collections import deque
import sys

T = int(input())

for i in range(T):
    n, m = map(int,sys.stdin.readline().rstrip().split())
    importance = list(map(int,sys.stdin.readline().rstrip().split()))

    arr = [[j,importance[j]] for j in range(n)]
    #arr = sorted(arr,key=lambda x: x[1],reverse=True)

    count = 0
    docu = deque([j for j in range(n)])
    arr = deque(sorted(importance,reverse=True))

    while len(arr) > 0:
        idx = docu.popleft()
        imp = arr.popleft()
        if importance[idx] < imp:
            docu.append(idx)
            arr.appendleft(imp)
        elif importance[idx] == imp:
            count += 1
            if idx == m:
                break
        else:
            docu.append(idx)
            arr.appendleft(idx)

    print(count)
