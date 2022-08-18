from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = set(map(int, input().split()))
arr = sorted(list(arr))

for case in combinations_with_replacement(arr, m):
    for element in case:
        print(element, end=' ')
    print()
