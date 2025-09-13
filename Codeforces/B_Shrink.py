t = int(input())
for _ in range(t):
    n = int(input())
    res = [0] * n
    l, r = 0, n - 1
    val = 1
    while l <= r:
        if val % 2 == 1:
            res[l] = val
            l += 1
        else:
            res[r] = val
            r -= 1
        val += 1
    print(' '.join(map(str, res[::-1]))) 
