I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
lis = LII()

def go(l,r):
    if l>r:
        return 0
    if l==r:
        return lis[l]
    le = lis[l]+min(go(l+2,r), go(l+1,r-1))
    ri = lis[r]+min(go(l,r-2), go(l+1,r-1))
    return max(le,ri)
print(go(0,n-1))