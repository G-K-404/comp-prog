#include<iostream>
#include<cstring>
using namespace std;
long long dp[101][];
long long v[101];
int w[101];
int n, W;
void solve(){
    cin>>n>>W;
    for(int i=0; i<n; i++){
        cin>>w[i]>>v[i];
    }
    memset(dp, 0, sizeof(dp));
    
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    solve();
}