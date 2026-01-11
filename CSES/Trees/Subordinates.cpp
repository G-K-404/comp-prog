
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> parents(n-1,0);
    for(int i=0; i<n-1; i++){
        cin>>parents[i];
    }
    vector<vector<int>> adj(n);
    int idx = 1;
    for(auto x:parents){
        adj[x-1].push_back(idx);
        idx++;
    }
    vector<int>ans(n,0);
    function<void(int)> go = [&](int node){
        for(auto x:adj[node]){
            go(x);
            ans[node]+=ans[x]+1;
        }
    };
    go(0);
    for(auto x:ans){
        cout<<x<<" ";
    }
}
