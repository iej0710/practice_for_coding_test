from collections import deque

def solution(enter, leave):
    meet = {i: 0 for i in range(1, len(enter) + 1)}
    in_room = set()
    enter = deque(enter)
    leave = deque(leave)
    flag = 1
    while len(enter) > 0 and len(leave) > 0:
        if flag == 1:
            left = leave.popleft()
            flag = 0
        if left in in_room:
            in_room.remove(left)
            flag = 1
            continue
        entrance = enter.popleft()
        in_room.add(entrance)
        if entrance != left:
            meet[entrance] += len(in_room) - 1
            for i in in_room:
                if i != entrance:
                    meet[i] += 1
        else:
            in_room.remove(left)
            meet[left] += len(in_room)
            for i in in_room:
                if i != left:
                    meet[i] += 1
            flag = 1
    return list(meet.values())

print(solution([1,3,2],[1,2,3]))
print(solution([1,4,2,3],[2,1,3,4]))
print(solution([3,2,1],[1,3,2]))