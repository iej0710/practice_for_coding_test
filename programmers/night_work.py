import heapq
def solution(n, works):
    answer = 0
    w = []
    for i in range(len(works)):
        heapq.heappush(w, -works[i])

    for i in range(n):
        t = heapq.heappop(w)
        heapq.heappush(w, t + 1)

    for r in w:
        if r < 0:
            answer += r ** 2

    return answer
