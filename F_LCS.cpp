#include<iostream>
#include <algorithm>
#include<cstring>
using namespace std;
long long dp[3001][3001];
void solve(){
    string s1,s2;
    cin>>s1>>s2;
    for(int i=s1.length(); i>=0; i--){
        for(int j=s2.length(); j>=0; j--){
            if(i>=s1.length() || j>=s.length()){
                dp[i][j] = 0;
            }
            if(s[i]==s[j]){
                dp[i][j] = 1+dp[i+1][j+1]
            }
            else{
                dp[i][j] = max(dp[i+1][j], dp[i][j+1]);
            }
        }
    }
    int i = 0;
    int j = 0;
    while(true){
        if(i>=s1.length() && j>=s2.length()){
            
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    solve();
}