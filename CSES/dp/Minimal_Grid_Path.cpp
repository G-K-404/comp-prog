#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> grid(n);
    for (int i = 0; i < n; ++i)
        cin >> grid[i];

    queue<pair<int, int>> q;
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    q.push({0, 0});
    visited[0][0] = true;

    string result = "";
    result += grid[0][0];

    for (int step = 0; step < 2 * n - 2; ++step) {
        vector<pair<int, int>> next;
        char minChar = 'Z' + 1;

        // Explore all current frontier
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (auto [dx, dy] : vector<pair<int,int>>{{1, 0}, {0, 1}}) {
                int nx = x + dx, ny = y + dy;
                if (nx < n && ny < n && !visited[nx][ny]) {
                    if (grid[nx][ny] < minChar) {
                        minChar = grid[nx][ny];
                        next.clear();
                        next.push_back({nx, ny});
                    } else if (grid[nx][ny] == minChar) {
                        next.push_back({nx, ny});
                    }
                }
            }
        }

        // Mark and enqueue only minimal char positions
        for (auto [x, y] : next) {
            if (!visited[x][y]) {
                visited[x][y] = true;
                q.push({x, y});
            }
        }

        result += minChar;
    }

    cout << result << '\n';
    return 0;
}
