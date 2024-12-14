#include<iostream>
#include<cstring>
using namespace std;
long long dp[100001];
long long h[100001];
void solve(){
    int n,k; 
    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>h[i];
    }
    memset(dp, 1+1e4, sizeof(dp));
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = abs(h[1]-h[0]);
    for(int i=3; i<=n; i++){
        for(int j=1; j<=min(k, i-1); j++){
            dp[i] = min(dp[i], dp[i-j]+abs(h[i-1]-h[i-j-1]));
        }
    }
    cout<<dp[n];
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    solve();
}