import sys

while 1:
    text = sys.stdin.readline().rstrip()
    if text[0] == '.':
        break

    container = []
    for c in text:
        if c in ['(', ')', '[', ']']:
            container.append(c)

    if len(container) == 0:
        print('yes')
        continue
    elif len(container) % 2 == 1:
        print('no')
        continue
    else:
        temp = []
        while len(container) > 0:
            a = container.pop()
            if len(temp) == 0:
                temp.append(a)
            elif a == '(' and temp[-1] == ')':
                temp.pop()
            elif a == '[' and temp[-1] == ']':
                temp.pop()
            else:
                temp.append(a)
        if len(temp) == 0:
            print('yes')
        else:
            print('no')