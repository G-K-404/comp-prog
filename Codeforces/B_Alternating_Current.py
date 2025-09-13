I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
def solve():
    s = I()
    stack = []
    for x in s:
        if stack and x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    print("Yes" if not stack else "No")
solve()
