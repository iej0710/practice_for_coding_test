def solution(records):
    answer = []
    id2nick = {}
    for record in records:
        tmp = record.split(" ")
        print(tmp)
        if tmp[0] != 'Leave':
            id2nick[tmp[1]] = tmp[2]

    for record in records:
        tmp = record.split(" ")
        if tmp[0] == 'Enter':
            answer.append(id2nick[tmp[1]] + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(id2nick[tmp[1]] + '님이 나갔습니다.')

    return answer

example = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(example))