n = int(input())

people = []
arr = [0 for i in range(n)]
for i in range(n):
    people.append(list(map(int, input().split())))

for i in range(len(people)):
    for j in range(len(people)):
        if i != j:
            if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
                arr[j] += 1

for i in arr:
    print(i + 1, end=' ')

print()