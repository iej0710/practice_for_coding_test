def solution(n, times):
    answer = 0
    times.sort()
    src = 0
    dest = times[-1] * n

    while src <= dest:
        mid = (src + dest) // 2

        tmp = 0
        for time in times:
            tmp += mid // time

        if tmp >= n:
            dest = mid - 1
            answer = mid
        else:
            src = mid + 1

    return answer