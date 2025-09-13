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
st = []
id = 0
ans = []
for i,x in enumerate(lis):
    idx = i
    while st and st[-1][1]>=x:
        st.pop()
    ans.append(idx-st[-1][0] if st else 0)
    st.append((i,x))
print(*ans)