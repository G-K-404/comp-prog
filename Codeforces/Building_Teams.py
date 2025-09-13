from collections import defaultdict, deque

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())

n, m = MII()
frnds = defaultdict(list)
for _ in range(m):
    u, v = MII()
    frnds[u].append(v)
    frnds[v].append(u)

colors = [-1] * n
flag = False

for start in range(1, n + 1):
    if colors[start - 1] == -1:
        colors[start - 1] = 0
        q = deque([start])
        while q:
            node = q.popleft()
            for x in frnds[node]:
                if colors[x - 1] == -1:
                    colors[x - 1] = 1 - colors[node - 1]
                    q.append(x)
                elif colors[x - 1] == colors[node - 1]:
                    print("IMPOSSIBLE")
                    flag = True
                    break
            if flag:
                break
    if flag:
        break

if not flag:
    print(*[c + 1 for c in colors])