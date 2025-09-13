import sys
from collections import defaultdict

input = sys.stdin.readline

def count_subarrays_with_sum(pref, target):
    """
    Given a list `pref` of prefix sums (with pref[0]=0),
    return the number of pairs (i<j) with pref[j] - pref[i] == target.
    """
    freq = defaultdict(int)
    cnt = 0
    for P in pref:
        # if P - target was seen before, any of those positions
        # gives a subarray ending here of sum = target
        cnt += freq[P - target]
        # record current prefix
        freq[P] += 1
    return cnt

def solve():
    t = int(input())
    for _ in range(t):
        n, s, x = map(int, input().split())
        a = list(map(int, input().split()))

        ans = 0
        i = 0
        # process each block where all a[i] <= x
        while i < n:
            # skip over any a[i] > x
            if a[i] > x:
                i += 1
                continue

            # start of a new valid block
            start = i
            while i < n and a[i] <= x:
                i += 1
            end = i  # a[start:end] are all <= x

            block = a[start:end]
            length = end - start

            # build prefix sums for the block
            pref = [0] * (length + 1)
            for j in range(length):
                pref[j+1] = pref[j] + block[j]

            # (1) total subarrays in block with sum == s
            total = count_subarrays_with_sum(pref, s)

            # find all positions of x in this block
            x_positions = [j for j, val in enumerate(block) if val == x]

            # *** NEW: if there’s no x in this block, it can’t contribute ***
            if not x_positions:
                continue

            # (2) subtract those in no-x regions
            bad = 0
            # region before first x
            left_len = x_positions[0]
            bad += count_subarrays_with_sum(pref[:left_len+1], s)

            # between consecutive x's
            for p, q in zip(x_positions, x_positions[1:]):
                length_mid = q - p - 1
                if length_mid > 0:
                    mid_pref = [0] * (length_mid + 1)
                    for k in range(length_mid):
                        mid_pref[k+1] = mid_pref[k] + block[p+1+k]
                    bad += count_subarrays_with_sum(mid_pref, s)

            # region after last x
            right_len = length - 1 - x_positions[-1]
            if right_len > 0:
                start_idx = x_positions[-1] + 1
                tail_pref = [0] * (right_len + 1)
                for k in range(right_len):
                    tail_pref[k+1] = tail_pref[k] + block[start_idx + k]
                bad += count_subarrays_with_sum(tail_pref, s)

            # add only those that actually include at least one x
            ans += total - bad


        print(ans)

if __name__ == "__main__":
    solve()
