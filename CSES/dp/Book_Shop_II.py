I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n,x = MII()
prices = LII()
pages = LII()
copies = LII()


memo = {}
def go(ccc, i, cos):
    if i>=n:
        return 0
    if (ccc,i,cos) in memo:
        return memo[(ccc,i,cos)]
    a = 0
    b = 0
    a = go(0,i+1,cos)
    if cos+prices[i] <= x and ccc+1<=copies[i]:
        b = go(ccc+1, i, cos+prices[i])+pages[i]
    memo[(ccc,i,cos)] = max(a,b)
    return max(a,b)
print(go(0,0,0))