from itertools import permutations
from collections import deque
import copy


def operate(x, y, oper):
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    else:
        return x * y


def solution(expression):
    answer = 0
    operation = set()
    op = []
    arr = []
    num = ''
    for char in expression:
        if ord('0') <= ord(char) <= ord('9'):
            num += char
        else:
            operation.add(char)
            arr.append(int(num))
            op.append(char)
            num = ''
    arr.append(int(num))

    for rank_op in permutations(list(operation), len(operation)):
        o = deque(copy.deepcopy(op))
        number = deque(copy.deepcopy(arr))
        for rank in rank_op:
            rotate = len(o)
            for r in range(rotate):
                opr = o.popleft()
                n1 = number.popleft()
                n2 = number.popleft()
                if opr == rank:
                    number.appendleft(operate(n1, n2, opr))
                else:
                    o.append(opr)
                    number.append(n1)
                    number.appendleft(n2)
            number.rotate(-1)
        answer = max(answer, abs(number[0]))

    return answer

ex = "100-200*300-500+20"
ex2 = "50*6-3*2"
print(solution(ex)) #answer: 60420
print(solution(ex2)) #answer: 300
