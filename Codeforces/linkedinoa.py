I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

edgecost = II()
inputcost = II()
bundlecost = II()
x = II()
y = II()

print(min(bundlecost*max(x,y),(bundlecost*min(x,y) + edgecost*(x-y) if x>y else inputcost*(y-x)), x*edgecost+y*inputcost))