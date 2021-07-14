
x = input()
alphabet = {}

for i in range(len(x)):
    if x[i] not in alphabet.keys():
        alphabet[x[i]] = i

for k in range(ord('a'),ord('z')+1):
    if chr(k) not in alphabet.keys():
        print(-1,end=" ")
    else:
        print(alphabet[chr(k)])