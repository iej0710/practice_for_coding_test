import sys

n, s = map(int, input().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

i, j = 0, 1
res = len(arr) + 1
partial_sum = arr[i] + arr[j]
while j < len(arr):
    if partial_sum < s:
        if j < len(arr) - 1:
            j += 1
            partial_sum += arr[j]
        else:
            break
    elif partial_sum >= s:
        res = min(res, j - i + 1)
        if i < j:
            partial_sum -= arr[i]
            i += 1
        else:
            if j < len(arr) - 1:
                j += 1
                partial_sum += arr[j]
            else:
                break



if res <= len(arr):
    print(res)
else:
    print(0)