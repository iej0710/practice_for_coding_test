def solution(s):
    answer = []
    zero_count, t_count = 0, 0

    while s != '1':
        zeros = s.count('0')
        zero_count += zeros
        s = str(bin(len(s) - zeros))[2:]
        t_count += 1
    answer = [t_count, zero_count]
    return answer

print(solution("110010101001"))