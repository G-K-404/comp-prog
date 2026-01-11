I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

class DSU:
    def __init__(self,size):
        parent = list(range(size))
    def find(self,i):
        if (self.parent[i]==i):
            return i
        par = self.parent[i]
        return self.find(par)
    def unite(self,i,j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep] = jrep
        return
def solve():
    n,m = MII()
    grid = [list(map(str,I())) for _ in range(n)]
    for x in grid:
        for y in grid:
            if 
solve()

    