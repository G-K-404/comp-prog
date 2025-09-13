#include <iostream>
#include <cstring>
using namespace std;
int x,k,n;
int t[1001];
int s[1001];
int taken[1001];

bool valid(int ques){
    int timetaken = 0;
    int skiltaken = 0;
    for(int i =0; i<ques; i++){
        if(taken[i]){
            timetaken += t[i];
            skiltaken++;
        }
    }
    timetaken+=t[ques];
    skiltaken++;
    return (timetaken<=k && skiltaken<=x);
}

int rec(int ques){
    if(ques == n){
        return 0;
    }
    int ans = rec(ques+1);

    if(valid(ques)){
        taken[ques] = 1;
        ans = max(ans, s[ques]+rec(ques+1));
        taken[ques] = 0;
    }
    return ans;
}

void solve(){
    cin>>x>>k>>n;
    for(int i=0; i<n;i++){
        cin>>t[i]>>s[i];
    }
    memset(taken,0,sizeof(taken));
    cout<<(rec(0))<<endl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}