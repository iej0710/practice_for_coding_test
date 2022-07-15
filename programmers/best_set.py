def solution(n, s):
    answer = []
    if s // n == 0:
        answer = [-1]
    elif s % n == 0:
        answer = [s // n] * n
    else:
        k = s // n
        answer = [s // n] * n
        for i in range(s % n):
            answer[-1 - i] += 1
    return answer