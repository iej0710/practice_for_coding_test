def max_depth(graph,start,visited,d,res,path):
    if len(graph) == len(visited):
        return d
    visited.add(start)
    for v in graph[start]:
        if v[0] not in visited:
            tmp = path.copy()
            tmp.append(v[0])
            res.append([v[0],d+v[1],tmp])
            max_depth(graph,v[0],visited,d+v[1],res,tmp)


len_v = int(input())
tree = {i + 1:[] for i in range(len_v)}

for i in range(len_v):
    tmp = list(map(int,input().split()))
    for i in range(1,len(tmp) - 1,2):
        tree[tmp[0]].append([tmp[i],tmp[i+1]])


src = list(tree.keys())[0]
visit = set()
res1 = []
p = []
max_depth(tree,src,visit,0,res1,p)
res1 = sorted(res1,key=lambda x: x[1],reverse=True)[0]

res2 = []
max_depth(tree,res1[0],set(),0,res2,[])
res2 = sorted(res2, key=lambda x: x[1], reverse=True)[0]
print(max(res1[1],res2[1]))
