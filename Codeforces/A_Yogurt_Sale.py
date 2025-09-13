I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
     lis = LII()
     yog = lis[0]
     one = lis[1]
     two = lis[2]
     if(two<one*2):
          print(int(yog/2)*two + (yog%2)*one)
     else:
          print(yog*one)
      
              
        
t=II()
for _ in range(t):
    solve()