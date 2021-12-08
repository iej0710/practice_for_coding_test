def dfs(g, src, visited):
    visited[src] = 1
    for i in range(len(g)):
        if g[src][i] == 1 and visited[i] == 0 and i != src:
            dfs(g, i, visited)


def solution(n, computers):
    answer = 0

    visited = [0] * n
    src = 0
    while sum(visited) < n:
        if visited[src] == 0:
            dfs(computers, src, visited)
            answer += 1
        else:
            src += 1

    return answer