def max_network_rank(starts: list[int], ends: list[int], n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    indeg = [0]*(n+1)
    for i in range(len(starts)):
        indeg[starts[i]]+=1
        indeg[ends[i]]+=1
    ans = -1
    for x, y in zip(starts, ends):
        ans = max(ans, indeg[x]+indeg[y]-1)
    return ans

if __name__ == "__main__":
    starts = [int(x) for x in input().split()]
    ends = [int(x) for x in input().split()]
    n = int(input())
    res = max_network_rank(starts, ends, n)
    print(res)
