n = int(input())

for i in range(n):
    x, s = input().split()
    for i in range(len(s)):
        print(s[i]*int(x),end="")
    print()