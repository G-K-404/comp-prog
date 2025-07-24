#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MOD = 1e9 + 7;
vector<vector<int>> adj;
vector<vector<int>> children;
int n;
long long memo[2][100005];
bool vis[2][100005];

void dfs(int node, int parent) {
    for (int x : adj[node]) {
        if (x != parent) {
            children[node].push_back(x);
            dfs(x, node);
        }
    }
}

long long go(int take, int node) {
    if (vis[take][node]) return memo[take][node];
    vis[take][node] = true;
    if (children[node].empty()) return memo[take][node] = 1;
    long long res = 1;
    if (take) {
        for (int x : children[node]) {
            res = res * go(0, x) % MOD;
        }
    } else {
        for (int x : children[node]) {
            res = res * (go(0, x) + go(1, x)) % MOD;
        }
    }
    return memo[take][node] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    adj.assign(n + 1, vector<int>());
    children.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    memset(vis, 0, sizeof(vis));
    dfs(1, 0);
    cout << (go(0, 1) + go(1, 1)) % MOD << '\n';
    return 0;
}
