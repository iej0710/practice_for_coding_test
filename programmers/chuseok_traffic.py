import datetime
from collections import deque


def solution(lines):
    answer = 0
    form = '%Y-%m-%d %H:%M:%S.%f'

    queue = deque()
    for line in lines:
        date, time, processing = line.split()
        dt_datetime = datetime.datetime.strptime(date + ' ' + time, form)
        processing = float(processing[:-1])
        queue.append([dt_datetime, processing])

    end = datetime.datetime.strptime('2016-09-15 00:00:0.0', form)
    while len(queue) > 0:
        ed, p = queue.popleft()
        delta = ed - end
        count = 0
        print(delta)
        for i in range(len(queue)):
            process_end = queue[i][0] - ed
            print(process_end)
            if process_end.total_seconds() <= queue[i][1] + 1:
                count += 1
        answer = max(count, answer)

    return answer

example = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(example))

ex2 =  [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(ex2))