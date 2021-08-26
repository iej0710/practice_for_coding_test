from collections import deque
import sys

T = int(input())

for i in range(T):
    function_list = input()
    n = int(input())
    temp = input()
    reverse_flag = 0
    if n != 0:
        arr = deque(map(int,temp.strip('[').strip(']').split(',')))
    else:
        arr = []
    error = 1
    for task in function_list:
        if task == 'R':
            reverse_flag += 1
        else:
            if len(arr) == 0:
                error = 0
                break
            else:
                if reverse_flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if error == 1:
        if reverse_flag % 2 == 1:
            arr.reverse()
        #print(list(arr))
        ans = ''
        for i in arr:
            ans += str(i) +','
        ans = '[' + ans[:-1] + ']'
        print(ans)
    else:
        print('error')


