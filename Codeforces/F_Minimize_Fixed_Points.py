I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n = II()
    dic = {}
    arr = [1]
    t = n+1
    vis = set()
    for i in range(2,t):
        if i in dic:
            arr.append(dic[i])
            continue
        fac = 1
        ni = i*fac
        while ni in vis and (fac+1)*i<=n or (ni==i and (fac+1)*i<=n):
            fac+=1
            ni = i*fac
        vis.add(ni)
        dic[ni] = i
        arr.append(ni)
    print(*arr)


t = II()
for _ in range(t):
    solve()