while 1:
    try:
        s = input()
    except:
        break
    if len(s) == 1 and s[0] == '.':
        break
    stack1 = []

    flag = 1
    for char in s:
        if char == '[' or char == '(':
            stack1.append(char)
        elif char == ']' and len(stack1) > 0:
            tmp = stack1.pop()
            if tmp == '(':
                flag = 0
                break
        elif char == ')' and len(stack1) > 0:
            tmp = stack1.pop()
            if tmp == '[':
                flag = 0
                break
        elif char == ']' and len(stack1) == 0:
            flag = 0
            break
        elif char == ')' and len(stack1) == 0:
            flag = 0
            break

    if flag == 1 and len(stack1) == 0:
        print('yes')
    else:
        print('no')