#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;

int n;
vector<int> coins;
set<int> sums;
unordered_set<long long> visited;

int main() {
    cin >> n;
    coins.resize(n);
    for (int i = 0; i < n; ++i) cin >> coins[i];
    int max_sum = 0;
    for (int x : coins) max_sum += x;
    vector<bool> dp(max_sum + 1, false);
    dp[0] = true;
    for (int coin : coins) {
        for (int s = max_sum; s >= coin; --s) {
            if (dp[s - coin]) dp[s] = true;
        }
    }
    vector<int> ans;
    for (int i = 1; i <= max_sum; ++i) {
        if (dp[i]) ans.push_back(i);
    }
    cout << ans.size() << endl;
    for (int x : ans) cout << x << " ";
    cout << endl;
    return 0;
}