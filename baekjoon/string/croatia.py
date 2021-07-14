import re

text = input()

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count = 0
res = len(text)
for a in croatia:
    text = text.replace(a,'*')
    '''for i in re.finditer(a,text):
        count += 1
        res -= len(a)'''

print(len(text))