from collections import Counter
import sys

n = int(input())

words = {}
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp not in words.keys():
        flag = 1
        for word in words:
            if len(tmp) == len(word):
                tmp_char = sorted(list(tmp))
                word_char = sorted(list(word))
                count = 0
                for k in range(len(tmp_char)):
                    if tmp_char[k] != word_char[k]:
                        break
                    else:
                        count += 1
                if count == len(tmp_char):
                    words[word] += 1
                    flag = 0
        if flag == 1:
            words[tmp] = 1
    else:
        words[tmp] += 1

print(len(words.keys()))