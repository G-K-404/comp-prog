#include <iostream>
#include <cstring>
using namespace std;
//dp array consists of cost taken to come from a stone behind and 2 stones behind.
long long dp[100001];
long long h[100000];
void solve(){
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>h[i];
    }
    memset(dp, 1+1e4, sizeof(dp));
    dp[0]= 0;
    dp[1] = 0;
    dp[2] = abs(h[1]-h[0]);
    for(int i=3; i<=n; i++){
        dp[i] = min(dp[i], dp[i-1]+abs(h[i-2]-h[i-1]));
        dp[i] = min(dp[i], dp[i-2]+abs(h[i-3]-h[i-1]));
    }
    cout<<dp[n];
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    solve();
}