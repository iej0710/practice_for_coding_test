def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    src, dst = 0, len(citations) - 1
    while src <= dst:
        mid = (src + dst) // 2
        if citations[mid] > mid:
            src = mid + 1
        elif citations[mid] == mid:
            return mid
        else:
            dst = mid - 1

    return src