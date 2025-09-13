I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s = I()
dic = {}
dic['A'] = []
res = 0
for i,x in enumerate(s):
    if x=='A':
        dic[x].append(i)
    elif x=='B':
        for z in dic['A']:
            if z<i:
                if 2*i-z < len(s):
                    if s[2*i-z] == 'C':
                        res+=1
print(res)