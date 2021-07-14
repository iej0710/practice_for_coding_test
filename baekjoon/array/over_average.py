import sys

n = int(input())

for k in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    student = arr[0]
    point = arr[1:]

    print('{:.3f}%'.format(sum(point[i] > (sum(point) / student) for i in range(student)) / student * 100))