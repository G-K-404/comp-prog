#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXN = 3005;
long long dp[2][MAXN][MAXN]; // dp[turn][l][r]
bool visited[2][MAXN][MAXN];
vector<long long> a;

long long go(int turn, int l, int r) {
    if (l > r) return 0;
    if (visited[turn][l][r]) return dp[turn][l][r];

    long long res = max(
        a[l] - go(turn ^ 1, l + 1, r),
        a[r] - go(turn ^ 1, l, r - 1)
    );

    visited[turn][l][r] = true;
    return dp[turn][l][r] = res;
}

int main() {
    int n;
    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << go(1, 0, n - 1) << '\n'; // Taro starts → turn = 1
    return 0;
}
