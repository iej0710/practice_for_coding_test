#not solved

def dfs(g, src, res, used, tickets):
    global result
    if sum(used) == len(tickets):
        result = min(result, res)
        return result

    for v, tid in g[src]:
        if used[tid] == 0:
            used[tid] = 1
            dfs(g, v, res + ',' + v, used, tickets)
            used[tid] = 0


def solution(tickets):
    global result
    answer = []
    result = 'Z' * 3 * (len(tickets) + 1)
    g = {}
    eg = {}
    idx = 0
    for src, dst in tickets:
        try:
            g[src].append([dst, idx])
        except:
            g[src] = [[dst, idx]]
        idx += 1
    for k in g.keys():
        g[k].sort()

    used = [0] * len(tickets)
    res = ''
    dfs(g, 'ICN', res, used, tickets)
    result = 'ICN' + result

    answer = result.split(',')

    return answer

ex = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(ex))
ex1 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(ex1))