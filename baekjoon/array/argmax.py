arr = []
for i in range(9):
    arr.append(int(input()))

m = max(arr)
for i in range(len(arr)):
    if arr[i] == m:
        idx = i
        break
print(max(arr),idx)