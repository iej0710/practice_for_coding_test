import sys

longest_word = ''
flag = 1
while flag:
    text = sys.stdin.readline().rstrip().split(' ')
    if text[-1] == 'E-N-D':
        del text[-1]
        flag = 0

    sorted_word = sorted(text, key=lambda x: -len(x))

    if len(longest_word) < len(sorted_word[0]):
        for word in text:
            if len(word) == len(sorted_word[0]):
                longest_word = word
                break

print(longest_word.lower())