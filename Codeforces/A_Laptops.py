I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
dstup = []
for x in range(n):
    a,b = MII()
    dstup.append((a,b))
dstup.sort(key = lambda x: (x[0],x[1]))
def solve():
    if n==1:
        print("Poor Alex")
        return
    for i in range(len(dstup)-1):
        if dstup[i][1]>dstup[i+1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")
solve()
        