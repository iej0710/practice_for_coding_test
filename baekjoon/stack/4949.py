while 1:
    try:
        s = input()
    except:
        break
    if len(s) == 1 and s[0] == '.':
        print('yes')
        break
    stack1 = []
    stack2 = []
    flag = 1
    for char in s:
        if char == '[':
            stack1.append(char)
        elif char == '(':
            stack2.append(char)
        elif char == ']' and len(stack1) > 0:
            stack1.pop()
        elif char == ')' and len(stack2) > 0:
            stack2.pop()
        elif char == ']' and len(stack1) == 0:
            flag = 0
            break
        elif char == ')' and len(stack2) == 0:
            flag == 0
            break

    if flag == 1 and len(stack1) == 0 and len(stack2) == 0:
        print('yes')
    else:
        print('no')