def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            num = '0' + bin(num)[2:]
            idx = num.rfind('0')
            num = list(num)
            num[idx] = '1'
            if num[-1] == '1':
                num[idx + 1] = '0'
            num = int("".join(num), 2)
            answer.append(num)

    return answer