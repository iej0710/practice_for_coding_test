import sys
from itertools import permutations
import math

N = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
operation = list(map(int,sys.stdin.readline().rstrip().split()))
operation_dict = ['+','-','*','/']

operation = [operation_dict[i] for i in range(len(operation_dict)) for j in range(operation[i])]

operation = set(permutations(operation,len(operation)))
print(operation, len(operation))
min_res = 10 ** 8
max_res = -10 ** 8
for case in operation:#permutations(operation,len(operation)):
    answer = arr[0]
    for i in range(len(case)):
        if case[i] == '+':
            answer += arr[i+1]
        elif case[i] == '-':
            answer -= arr[i+1]
        elif case[i] == '*':
            answer *= arr[i+1]
        else:
            flag = 0
            if answer < 0:
                answer = abs(answer)
                flag = 1
            answer = math.floor(answer / arr[i+1])
            if flag == 1:
                answer *= -1
    if answer > max_res:
        max_res = answer
    if answer < min_res:
        min_res = answer

print(max_res)
print(min_res)