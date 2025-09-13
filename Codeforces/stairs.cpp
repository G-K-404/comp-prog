#include <iostream>
using namespace std;

int rec(int level, int n){
    if(level == n){
    return 1;
    }
    int ways= 0;
    for(int i=1; i<=3;i++){
        if(level+i <= n){
            ways += rec(level+i,n);
        }
    }
    return ways;
}

void solve(){
    int n;
    cin>>n;
    cout<<(rec(0,n))<<endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        solve();
    }
}