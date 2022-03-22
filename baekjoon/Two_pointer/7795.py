import sys
def binary_search(arr, src, dst, target):
    mid = (src + dst) // 2
    if src > dst:
        return mid
    if target > arr[mid]:
        return binary_search(arr, mid + 1, dst, target)
    else:
        return binary_search(arr, src, mid - 1, target)

T = int(input())

for test in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0

    B.sort()
    id_b = 0
    for i in range(len(A)):
        id_b = binary_search(B, 0, m - 1, A[i])
        count += id_b + 1

    print(count)