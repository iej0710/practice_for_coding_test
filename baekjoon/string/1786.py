# Time-out
# Next: Re-implement to KMP algorithm

t = input()
p = input()

idx = 0
count = 0
ans = []

while idx < len(t):
    idx = t.find(p, idx)
    if idx == -1:
        break
    else:
        count += 1
        ans.append(idx)
        idx += 1

print(count)
for i in range(count):
    print(ans[i] + 1, end=' ')
print()