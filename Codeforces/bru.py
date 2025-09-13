def minimumLevels(self, possible: list[int]) -> int:
    dwins = 0
    bwins = 0
    ds = []
    bs = []
    for i in range(len(possible)-1):
        for j in range(i+1):
            if(possible[j]):
                dwins+=1
            else:
                dwins -= 1
        for k in range(i+1, len(possible)):
            if(possible[j]):
                bwins+=1
            else:
                bwins -= 1
        ds.append(dwins)
        bs.append(bwins)
    bru = []
    for i in range(len(possible)):
        bru.append(ds[i]-bs[i])
    if(max(bru)<0):
        return -1
    else:
        ans = bru.index(max(bru)) + 1
        return ans
