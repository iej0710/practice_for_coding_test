def solution(s):
    answer = len(s)
    len_fragment = 1
    while len_fragment <= len(s) // 2:
        compressed = ''
        tmp = ''
        count = 1
        for i in range(len(s)//len_fragment):
            pos = i * len_fragment
            if tmp == s[pos:pos+len_fragment]:
                count += 1
            else:
                if count == 1:
                    compressed += tmp
                else:
                    compressed += str(count) + tmp
                tmp = s[pos:pos+len_fragment]
                count = 1
        if count == 1:
            compressed += tmp
        else:
            compressed += str(count) + tmp
        if len(s) % len_fragment != 0:
            pos = len(s) % len_fragment
            compressed += s[-pos:]
        if answer > len(compressed):
            answer = len(compressed)
        len_fragment += 1
    return answer

s = input()
print(solution(s))