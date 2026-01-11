#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;
int n;
vector<vector<int>> a;
vector<int> dp;

int go(int i, int mask) {
    if (i == n) return mask == (1 << n) - 1 ? 1 : 0;
    if (dp[mask] != -1) return dp[mask];
    int res = 0;
    for (int j = 0; j < n; ++j) {
        if (!(mask & (1 << j)) && a[i][j]) {
            res = (res + go(i + 1, mask | (1 << j))) % MOD;
        }
    }
    return dp[mask] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    a.assign(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> a[i][j];
    dp.assign(1 << n, -1);
    cout << go(0, 0) << '\n';
    return 0;
}
