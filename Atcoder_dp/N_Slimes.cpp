#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];
    // Prefix sum
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + s[i];
    // dp[l][r]: min cost to merge slimes from l to r (inclusive)
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l + len - 1 < n; ++l) {
            int r = l + len - 1;
            dp[l][r] = INF;
            for (int k = l; k < r; ++k) {
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + prefix[r + 1] - prefix[l]);
            }
        }
    }
    cout << dp[0][n - 1] << '\n';
    return 0;
}
