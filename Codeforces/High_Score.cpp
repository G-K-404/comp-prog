#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long x;
        cin >> u >> v >> x;
        adj[u].emplace_back(v, x);
    }

    vector<long long> score(n + 1, LLONG_MIN);
    priority_queue<pair<long long, int>> pq;
    pq.emplace(0, 1);
    score[1] = 0;

    while (!pq.empty()) {
        auto [dis, node] = pq.top(); pq.pop();
        if (dis < score[node]) continue;
        for (auto &[v, w] : adj[node]) {
            if (score[node] + w > score[v]) {
                score[v] = score[node] + w;
                pq.emplace(score[v], v);
            }
        }
    }
    cout << score[n] << '\n';
    return 0;
}