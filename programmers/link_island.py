def parent(arr, x):
    if arr[x] == x:
        return x
    else:
        arr[x] = parent(arr, arr[x])
        return arr[x]


def union(arr, x, y):
    parent_x = parent(arr, x)
    parent_y = parent(arr, y)

    if parent_x >= parent_y:
        arr[parent_x] = parent_y
    else:
        arr[parent_y] = parent_x


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    arr = [i for i in range(n)]
    for v1, v2, w in costs:
        if parent(arr, v1) != parent(arr, v2):
            answer += w
            union(arr, v1, v2)

    return answer