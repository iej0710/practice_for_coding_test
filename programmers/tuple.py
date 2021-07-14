import string

def solution(s):
    answer = []
    s = s.strip(string.punctuation).split('},{')
    count_element = {}
    for token in s:
        tmp = token.split(',')
        for element in tmp:
            if int(element) not in count_element:
                count_element[int(element)] = 1
            else:
                count_element[int(element)] += 1
    count_element = sorted(count_element.items(),reverse=True,key = lambda item: item[1])
    for i in count_element:
        answer.append(i[0])
    return answer