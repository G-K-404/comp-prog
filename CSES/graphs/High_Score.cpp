#include <iostream>
#include <vector>
#include <limits>
using namespace std;

const long long INF = 1e18;

struct Edge {
    int from, to;
    long long weight;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        int a, b;
        long long x;
        cin >> a >> b >> x;
        edges[i] = {a, b, -x};  // Negate to find longest path using Bellman-Ford
    }

    vector<long long> dist(n + 1, INF);
    dist[1] = 0;

    // Bellman-Ford for n-1 iterations
    for (int i = 1; i < n; ++i) {
        for (auto& e : edges) {
            if (dist[e.from] < INF) {
                dist[e.to] = min(dist[e.to], dist[e.from] + e.weight);
            }
        }
    }

    // Check for negative cycle reachable from 1 and can reach n
    vector<bool> affected(n + 1, false);
    for (int i = 0; i < m; ++i) {
        auto& e = edges[i];
        if (dist[e.from] < INF && dist[e.from] + e.weight < dist[e.to]) {
            affected[e.to] = true;
        }
    }

    // DFS to check if affected nodes can reach n
    vector<vector<int>> adj(n + 1);
    for (auto& e : edges) {
        adj[e.from].push_back(e.to);
    }

    vector<bool> visited(n + 1, false);
    function<void(int)> dfs = [&](int u) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) dfs(v);
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (affected[i]) {
            dfs(i);
        }
    }

    if (visited[n]) {
        cout << -1 << '\n';  // positive cycle reachable from 1 and can reach n
    } else {
        cout << -dist[n] << '\n';  // negate back the distance to get the max score
    }

    return 0;
}
