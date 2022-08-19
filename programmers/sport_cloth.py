from collections import deque

def solution(n, lost, reserve):
    answer = n - len(lost)
    have_cloth = set(lost).intersection(set(reserve))
    answer += len(have_cloth)
    lost = deque(sorted(list(set(lost) - have_cloth)))
    reserve = deque(sorted(list(set(reserve) - have_cloth)))

    while len(reserve) > 0 and len(lost) > 0:
        idl = lost.popleft()
        idr = reserve.popleft()
        if idl == idr:
            answer += 1
        elif idr > idl:
            if idr - idl == 1:
                answer += 1
            else:
                reserve.appendleft(idr)
        else:
            if idl - idr == 1:
                answer += 1
            else:
                lost.appendleft(idl)
    return answer