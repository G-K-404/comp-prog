from itertools import permutations

def simulate(teams, outcomes):
    for outcome in outcomes:
        winners = []
        for i in range(0, len(teams), 2):
            a, b = teams[i], teams[i+1]
            if outcome == '0':
                winners.append(min(a, b))
            else:  # outcome == '1'
                winners.append(max(a, b))
        teams = winners
    return teams[0]

def solve():
    n = int(input().strip())
    s = input().strip()
    teams = list(range(1, 2**n + 1))
    winning_champions = set()
    for perm in permutations(teams):
        champion = simulate(list(perm), s)
        winning_champions.add(champion)
    print(" ".join(map(str, sorted(winning_champions))))

if __name__ == '__main__':
    solve()
