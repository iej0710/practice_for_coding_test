import re

n = int(input())
count = 0

for i in range(n):
    alphabet = set()
    temp = input()
    for j in range(len(temp)):
        alphabet.add(temp[j])
    alphabet = list(alphabet)
    flag = 1
    for j in alphabet:
        pos1 = temp.find(j)
        pos2 = temp.rfind(j)
        num = len(re.findall(j,temp))
        if num != pos2 - pos1 + 1:
            flag = 0
    if flag == 1:
        count += 1
print(count)