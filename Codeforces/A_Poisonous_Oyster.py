I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
s1,s2 = input().strip().split(" ")
if s1=="sick" and s2 =="sick":
    print(1)
elif s1=="fine" and s2 =="sick":
    print(3)
elif s1=="sick" and s2 =="fine":
    print(2)
else:
    print(4)