I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def Dec(num):
        if num >= 1:
            Dec(num // 2)
            return num % 2

def binvert(num):
    fin = []
    fin.append(Dec(num))
    return fin
    

def solve():
    ls = LII()
    k = II()
    bi = []
    fl = []
    for any in ls:
        fl.append(binvert(any))
    for i in range(len(fl)):
         for j in range(len(fl)):
              if(i!=j):
                   
                   
t = II()
for _ in range(t):
    solve()