import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
k = int(input())

arr.sort()
i, j = 0, len(arr) - 1
count = 0
while i < j:
    tmp = arr[i] + arr[j]
    if tmp == k:
        count += 1
        i += 1
        j -= 1
    elif tmp < k:
        i += 1
    elif tmp > k:
        j -= 1
        i = 0
print(count)