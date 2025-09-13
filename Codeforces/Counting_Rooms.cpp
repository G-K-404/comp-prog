#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
vector<string> grid;
vector<vector<bool>> vis;

int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

void bfs(int x, int y) {
    queue<pair<int,int>> q;
    q.push({x, y});
    vis[x][y] = true;

    while (!q.empty()) {
        auto [cx, cy] = q.front(); q.pop();
        for (int d = 0; d < 4; ++d) {
            int nx = cx + dirs[d][0];
            int ny = cy + dirs[d][1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                !vis[nx][ny] && grid[nx][ny] == '.') {
                vis[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    cin >> n >> m;
    grid.resize(n);
    vis.assign(n, vector<bool>(m, false));

    for (int i = 0; i < n; ++i)
        cin >> grid[i];

    int rooms = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (!vis[i][j] && grid[i][j] == '.') {
                bfs(i, j);
                ++rooms;
            }

    cout << rooms << "\n";
    return 0;
}
