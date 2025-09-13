I = lambda: input()
II = lambda: int(input())

t = II()
for _ in range(t):
    n = II()
    s = I()
    total = 0
    for i in range(n):
        cnt0 = cnt1 = 0
        for j in range(i, min(n, i + 200)):
            if s[j] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            total += max(cnt0, cnt1)
    print(total)
