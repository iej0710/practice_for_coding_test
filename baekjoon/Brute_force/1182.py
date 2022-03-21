import sys

def dfs(arr, src, partial_sum, target):
    global count
    if src > len(arr) - 1:
        return count
    if partial_sum + arr[src] == target:
        count += 1
    dfs(arr, src + 1, partial_sum, target)
    dfs(arr, src + 1, partial_sum + arr[src], target)


def solution(arr, ans):
    global count
    count = 0

    dfs(arr, 0, 0, ans)
    return count


n, s = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(arr, s))