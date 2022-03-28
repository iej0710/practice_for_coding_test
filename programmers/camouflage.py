def solution(clothes):
    answer = 1
    cabinet = {}
    for cloth in clothes:
        try:
            cabinet[cloth[1]] += 1
        except:
            cabinet[cloth[1]] = 1

    for part, num in cabinet.items():
        answer *= (num + 1)

    return answer - 1