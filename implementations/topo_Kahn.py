from collections import deque


def Kahnalgo(vert, diredges):
    q = deque([])
    vis = set()
    adj = [[] for _ in range(vert)]
    for x in diredges:
        s,d = x[0], x[1]
        adj[s].append(d)
    incount = [0]*vert
    for x in range(vert):
        for y in adj[x]:
            incount[y]+=1
    for x in range(vert):
        if incount[x]==0:
            q.append(x)
    res = []
    while(q):
        cur = q.popleft()
        res.append(cur)
        vis.add(cur)
        for y in adj[cur]:
            incount[y]-=1
            if incount[y]==0 and y not in vis:
                q.append(y)
    return res

vertices = 3
edges = [(0, 1), (1, 2), (2, 0)]
res = Kahnalgo(vertices, edges)
print(res if len(res)==vertices else "Cycle has  a graph")



