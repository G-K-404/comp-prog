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
    s = s[::-1]
    ans = ""
    for x in range(len(s)):
        if(s[x]=="q"):
            ans += "p"
        elif(s[x] == "p"):
            ans += "q"
        else:
            ans+="w"
    print(ans)


t = II()
for _ in range(t):
    solve()