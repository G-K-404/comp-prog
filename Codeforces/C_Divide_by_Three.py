def divide_by_three(n: str) -> str:
    digits = list(map(int, n))
    length = len(digits)
    zero_present = '0' in n

    from collections import defaultdict, deque

    # (i, s) → max_digits_used to reach a valid end from here
    max_digits = {}

    # Same: discover reachable states
    stack = [(0, 0)]
    visited = set()
    topo = []

    while stack:
        i, s = stack.pop()
        if (i, s) in visited:
            continue
        visited.add((i, s))
        topo.append((i, s))
        if i < length:
            stack.append((i + 1, s + digits[i]))
            stack.append((i + 1, s))

    # Bottom-up fill max_digits[(i, s)] with max digit count
    for i, s in reversed(topo):
        if i == length:
            valid = (s % 3 == 0) and (zero_present or s > 0)
            max_digits[(i, s)] = 0 if valid else -1
        else:
            take = max_digits.get((i + 1, s + digits[i]), -1)
            skip = max_digits.get((i + 1, s), -1)

            res = -1
            if take != -1:
                res = max(res, take + 1)
            if skip != -1:
                res = max(res, skip)

            max_digits[(i, s)] = res

    if max_digits.get((0, 0), -1) == -1:
        return "-1"

    # Reconstruct longest valid subsequence
    res = []
    i, s = 0, 0
    while i < length:
        take = max_digits.get((i + 1, s + digits[i]), -1)
        skip = max_digits.get((i + 1, s), -1)
        curr = max_digits[(i, s)]

        if take != -1 and take + 1 == curr:
            res.append(str(digits[i]))
            s += digits[i]
            i += 1
        elif skip != -1 and skip == curr:
            i += 1
        else:
            break  # no valid move

    out = ''.join(res).lstrip('0')
    return out if out else "0"


if __name__ == "__main__":
    import sys
    n = sys.stdin.readline().strip()
    print(divide_by_three(n))
