import sys

def binary_search(arr, k, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < k:
            start = mid + 1
        elif arr[mid] > k:
            end = mid
        else:
            return mid
    return (start + end) // 2

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

res = [-1] * (len(arr) + 1)

idx = 0

for i in range(len(arr)):
    index = binary_search(res, arr[i], 0, idx)
    if res[index] == -1:
        idx += 1
    res[index] = arr[i]

print(idx)




