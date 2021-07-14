import sys
n = int(input())

arr = list(map(int,sys.stdin.readline().rstrip().split()))

m = max(arr)
for i in range(n):
    arr[i] = arr[i]/m * 100
print(sum(arr) / n)