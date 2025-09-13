I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

num = I()
k = II()
n = len(num)
def go(r,tight):
    if r==n:
        return 0
    if tight:
        for x in range(int(num[r]),9):
            if x==int(num[r]):
                return 
    