#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(void){
    int x,n;
    cin>>x>>n;
    vector<int> v;
    v.resize(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    multiset<int> gap;
    set<int> lights;
    gap.emplace(x);
    lights.emplace(0);
    lights.emplace(x);
    vector<int> ans;
    for (auto i:v){
        auto it = lights.upper_bound(i);
        int ve = *it;
        it--;
        int b = *it;
        int g = ve-b;
        gap.erase(gap.find(g));
        gap.emplace(i-b);
        gap.emplace(ve-i);
        lights.emplace(i);
        ans.push_back(*gap.rbegin());
    }
    for(int i=0; i<n; i++){
        cout<<ans[i]<<' ';
    }
}