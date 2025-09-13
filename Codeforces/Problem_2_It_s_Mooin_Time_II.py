
from collections import *
n = int(input())
arr = list(map(int, input().split()))
mp = defaultdict(list)
st  = set()
p  = [0]*n
for i in range(len(arr)):
    st.add(arr[i])
    mp[arr[i]].append(i)
    p[i] = len(st)
ans = 0
for x in st:
    if len(mp[x])>=2:
        i = mp[x][-1]
        j = mp[x][-2]
        ans+=p[j-1]
        if len(mp[x])>2:
            ans-=1
print(ans)
