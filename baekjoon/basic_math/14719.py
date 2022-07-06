import heapq

h, w = map(int, input().split())

arr = list(map(int, input().split()))
block_info = []
for i in range(len(arr)):
    heapq.heappush(block_info, [-arr[i], i])

right_h, right_x = heapq.heappop(block_info)
left_h, left_x = right_h, right_x
res = -right_h
top = right_x
while len(block_info) > 0:
    y, x = heapq.heappop(block_info)
    if x > top and x > left_x:
        res += (x - left_x) * -y
        left_h, left_x = y, x
    elif x < top and x < right_x:
        res += (right_x - x) * -y
        right_h, right_x = y, x
print(res - sum(arr))