#include <iostream>
#include <cstring>
using namespace std;
int n;
int queen[20];
int rec(int row){
    if(row == n){
        return 1;
    }
    int ways = 0;
    bool flag = true;
    for(int i=0;i<n;i++){
        flag = true;
        for(int j=0; j<row; j++){
            if(abs(row-j) == abs(i-queen[j]) || i==queen[j]) {
                flag = false;
            }
        }
        if(flag){
            queen[row] = i;
            ways += rec(row+1);
            queen[row] = -1;
        }
    }
    return ways;
    
}

void solve(){
    cin>>n;
    memset(queen,-1,sizeof(queen));
    cout<<(rec(0))<<endl;
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