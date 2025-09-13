#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MOD = 1e9 + 7;

int main() {
    int n, t;
    cin >> n >> t;
    
    vector<int> coins(n);
    for(int i = 0; i < n; i++) {
        cin >> coins[i];
    }
    
    // Create 2D DP table
    vector<vector<int>> dp(n + 1, vector<int>(t + 1, 0));
    
    // Fill DP table
    for(int i = n-1; i >= 0; i--) {
        for(int j = t; j >= 0; j--) {
            if(j == t) {
                dp[i][j] = 1;
                continue;
            }
            
            int ans = 0;
            if(j + coins[i] <= t) {
                ans = (ans + dp[i][j + coins[i]]) % MOD;
            }
            ans = (ans + dp[i+1][j]) % MOD;
            dp[i][j] = ans;
        }
    }
    
    cout << dp[0][0] << endl;
    
    return 0;
}