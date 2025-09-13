#include<bits/stdc++.h>
using namespace std;

vector<int> copies;

int solve(vector<int> &price, vector<int> &pages, int n, int w, vector<vector<int>> &dp) {
    if(n == 0 || w == 0) return 0;
    int take = 0;
    if(dp[n][w] != -1) return dp[n][w];
    
    int nottake = solve(price, pages, n-1, w, dp);
    if(price[n-1] <= w && copies[n-1] > 0) {
        copies[n-1]--;
        take = pages[n-1] + solve(price, pages, n, w-price[n-1], dp);
        copies[n-1]++;
    }

    return dp[n][w] = max(take, nottake);
}


int main() {
    int n, x;
    cin>>n>>x;

    vector<int> price(n);
    vector<int> pages(n);
    copies.resize(n);

    for(int i = 0; i < n; i++) cin>>price[i];
    for(int i = 0; i < n; i++) cin>>pages[i];
    for(int i = 0; i < n; i++) cin>>copies[i];
    vector<vector<int>> dp(n+1, vector<int> (x + 1, -1));

    cout<<solve(price, pages, n, x, dp)<<"\n";

    return 0;
}
