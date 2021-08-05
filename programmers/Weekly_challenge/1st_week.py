def solution(price, money, count):
    answer = (price * (count ** 2) + price * count) / 2 - money
    if answer >= 0:
        return answer
    else:
        return 0

example = [3, 20, 4]

print(solution(example[0],example[1],example[2]))