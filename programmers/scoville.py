import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, x1 + 2 * x2)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer