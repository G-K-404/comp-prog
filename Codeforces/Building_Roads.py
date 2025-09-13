I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LII = lambda: list(map(int, input().split()))

class UnionFind():
    def __init__(self, size):
        self.par = list(range(size))
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return False
        self.par[irep] = jrep
        return True

n, m = MII()
un = UnionFind(n)
for _ in range(m):
    u, v = LII()
    un.unite(u-1, v-1)

roots = set()
for i in range(n):
    roots.add(un.find(i))
ans = 0
roots = list(roots)
answ = []
print(len(roots)-1)
for i in range(len(roots)-1):
    print(un.find(roots[i])+1,un.find(roots[i+1])+1)