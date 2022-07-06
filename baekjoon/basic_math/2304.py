import sys

n = int(input())

arr = []
max_x = 0
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    max_x = max(max_x, arr[i][0])

arr = sorted(arr, key=lambda x: -x[1])

res = arr[0][1]
mid, h  = arr[0][0], arr[0][1]
left_x, right_x = arr[0][0], arr[0][0]
left_h, right_h = arr[0][1], arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] > mid:
        if h == arr[i][1] or right_x < arr[i][0]:
            res += (arr[i][0] - right_x) * arr[i][1]
            right_x, right_h = arr[i][0], arr[i][1]

    else:
        if h == arr[i][1] or left_x > arr[i][0]:
            res += (left_x - arr[i][0]) * arr[i][1]
            left_x, left_h = arr[i][0], arr[i][1]

print(res)