#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <limits>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;

    // adj[a][b] = c
    vector<unordered_map<int, long long>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        if (adj[a].count(b)) {
            adj[a][b] = min(adj[a][b], c);
        } else {
            adj[a][b] = c;
        }
        if (adj[b].count(a)) {
            adj[b][a] = min(adj[b][a], c);
        } else {
            adj[b][a] = c;
        }
    }

    // Initialize distance matrix
    vector<vector<long long>> dis(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) {
        dis[i][i] = 0;
    }

    // Fill initial distances from adjacency list
    for (int s = 1; s <= n; ++s) {
        for (const auto& [k, cost] : adj[s]) {
            dis[s][k] = min(dis[s][k], cost);
        }
    }

    // Floyd-Warshall
    for (int k = 1; k <= n; ++k) {
        for (int s = 1; s <= n; ++s) {
            for (int d = 1; d <= n; ++d) {
                if (dis[s][k] < INF && dis[k][d] < INF) {
                    dis[s][d] = min(dis[s][d], dis[s][k] + dis[k][d]);
                }
            }
        }
    }

    // Answer queries
    while (q--) {
        int a, b;
        cin >> a >> b;
        if (dis[a][b] < INF) {
            cout << dis[a][b] << '\n';
        } else {
            cout << -1 << '\n';
        }
    }

    return 0;
}
