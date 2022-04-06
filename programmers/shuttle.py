from collections import deque

def time_shift(h, m, shift):
    m += shift
    if m > 59:
        m %= 60
        h += 1
    elif m < 0:
        m += 60
        h -=1
    return h, m

def solution(n, t, m, timetable):
    answer = ''
    ph, pm = 9, 0
    timetable = deque(sorted([list(map(int, timetable[i].split(':'))) for i in range(len(timetable))],
                             key=lambda x: (x[0], x[1])))

    shuttle = 0
    lh, lm = ph, pm
    for i in range(1, n):
        lm += t
        if lm >= 60:
            lm %= 60
            lh += 1

    count = 0
    h, minute = ph, pm
    while shuttle < n:
        while count < m and len(timetable) > 0:
            h, minute = timetable.popleft()
            if h > lh or (h == lh and minute > lm):
                answer = '{:0>2}:{:0>2}'.format(lh, lm)
                return answer
            if h < ph or (h == ph and minute <= pm):
                count += 1
            else:
                timetable.appendleft([h, minute])
                break
        if shuttle < n - 1 and count == m:
            print(1)
            shuttle += 1
            count = 0
            ph, pm = time_shift(ph, pm, t)
        elif shuttle < n - 1 and count < m and len(timetable) > 0:
            print(2)
            shuttle += 1
            count = 0
            ah, am = time_shift(ph, pm, -1)
            answer = '{:0>2}:{:0>2}'.format(ah, am)
            ph, pm = time_shift(ph, pm, t)
        elif shuttle <= n - 1 and count < m and len(timetable) == 0:
            print(3)
            answer = '{:0>2}:{:0>2}'.format(ph, pm)
            break
        elif shuttle == n - 1 and count == m:
            print(4)
            ah, am = time_shift(h, minute, -1)
            answer = '{:0>2}:{:0>2}'.format(ah, am)
            break

    return answer
#'{:0>2}:{:0>2}'.format(lh, lm - 1)
ex = ["08:00", "08:01", "08:02", "08:03"]
print(solution(1, 1, 5, ex))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2,	["09:00", "09:00", "09:00", "09:00"]))