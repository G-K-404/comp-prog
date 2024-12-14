#include <algorithm>
#include <cmath>
#include<cstring>
#include <iostream>
using namespace std;
long long dp[100001][3];
long long a[100001][3];
void solve(){
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        for(int j=0; j<3; j++){
        cin>>a[i][j];
    }
    }
    for(int i=0; i<100001; i++){
        for(int j=0; j<3; j++){
        dp[i][j] = 0;
    }
    }
    for(int i=1; i<=n; i++){
        for(int j=0; j<3; j++){
            for(int k=0; k<3; k++){
                if(k!=j){
                dp[i][j] = max(dp[i][j], dp[i-1][k]+a[i-1][j]);
                }
                
            }
        }
    }
    cout<<*max_element(dp[n] , dp[n] + 3);
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    solve();
}