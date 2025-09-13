I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def min_step(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    px,py = [0],[0]
    ans = inf
    for x in s:
        if x=='X':
            px.append(px[-1]+1)
            py.append(py[-1])
        else:
            px.append(px[-1])
            py.append(py[-1]+1)
    px = px[1:]
    py = py[1:]
    for i,x in enumerate(s):
        x = (px[-1]-px[i-1]) if i>0 else px[-1]
        y = py[i-1] if i>0 else 0
        ans = min(ans, y+x)
    return ans  

if __name__ == "__main__":
    s = input()
    res = min_step(s)
    print(res)
