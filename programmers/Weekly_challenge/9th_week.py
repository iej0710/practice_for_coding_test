from collections import deque

def bfs(graph, src, visited):
    visited.add(src)
    neighbor = deque([src])

    while len(neighbor) > 0:
        tmp = neighbor.popleft()
        for v in sorted(graph[tmp]):
            if v not in visited:
                visited.add(v)
                neighbor.append(v)
    return visited

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        graph = {}
        for j in range(len(wires)):
            if i != j:
                if wires[j][0] in graph.keys():
                    graph[wires[j][0]].append(wires[j][1])
                else:
                    graph[wires[j][0]] = [wires[j][1]]
                if wires[j][1] in graph.keys():
                    graph[wires[j][1]].append(wires[j][0])
                else:
                    graph[wires[j][1]] = [wires[j][0]]
        tree1 = bfs(graph, list(graph.keys())[0], set())
        answer = min(answer, abs(n - (2 * len(tree1))))

    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))