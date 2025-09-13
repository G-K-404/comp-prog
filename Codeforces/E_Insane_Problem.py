I = lambda: input()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t = II()
results = []

for _ in range(t):
    k, l1, r1, l2, r2 = LII()
    count = 0

    # Iterate over all x in the range [l1, r1]
    for x in range(l1, r1 + 1):
        # Start with y = x and compute powers of k
        y = x
        while y < l2:  # Find the first valid y >= l2
            if y > r2 // k:  # Prevent overflow
                y = r2 + 1
                break
            y *= k

        # Count all valid y <= r2
        while y <= r2:
            count += 1
            if y > r2 // k:  # Prevent overflow
                break
            y *= k

    results.append(count)
    print(count)
