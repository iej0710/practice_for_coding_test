import heapq

def solution(operations):
    answer = []
    max_h = []
    min_h = []
    count = 0
    for op in operations:
        op, num = op.split()
        print(count, max_h, min_h)
        num = int(num)
        if op == 'I':
            heapq.heappush(max_h, -num)
            heapq.heappush(min_h, num)
            count += 1
        elif op == 'D':
            if count == 0:
                continue
            else:
                count -= 1
            if num == 1:
                r = heapq.heappop(max_h)
                min_h.remove(-r)
            else:
                r = heapq.heappop(min_h)
                max_h.remove(-r)
    print(count, max_h, min_h)
    if count == 0:
        answer = [0, 0]
    else:
        answer = [heapq.heappop(min_h), -1 * heapq.heappop(max_h)]
    return answer


ex = ["I 16","D 1"]
ex2 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
ex3 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
ex4 = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]

#print(solution(ex))
#print(solution(ex2))
print(solution(ex3))
print(solution(ex4))