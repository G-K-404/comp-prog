#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(void){
    multiset<int> towers;
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    int ans = 0;
    for(auto i:v){
        auto it = towers.upper_bound(i);
        if(towers.empty() or i>=*towers.rbegin()){
            ans++;
            towers.emplace(i);
            continue;
        }
        int val = *it;
        towers.erase(towers.find(val));
        towers.emplace(i);
    }
    cout<<endl<<ans;
}