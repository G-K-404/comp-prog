#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n, m;
vector<int> fa, sa;
vector<vector<int>> dp;
vector<vector<string>> dp2;

int go(int i, int j) {
    if (i == n || j == m) return 0;
    if (dp[i][j] != -1) return dp[i][j];
    int c = 0;
    if (fa[i] == sa[j]) {
        c = go(i + 1, j + 1) + 1;
    }
    c = max(c, go(i + 1, j));
    c = max(c, go(i, j + 1));
    return dp[i][j] = c;
}

string go2(int i, int j) {
    if (i == n || j == m) return "";
    if (dp2[i][j] != "") return dp2[i][j];
    string c = "";
    if (fa[i] == sa[j]) {
        c = to_string(fa[i]) + " " + go2(i + 1, j + 1);
    } else {
        if (go(i + 1, j) > go(i, j + 1)) {
            c = go2(i + 1, j);
        } else {
            c = go2(i, j + 1);
        }
    }
    return dp2[i][j] = c;
}

int main() {
    cin >> n >> m;
    fa.resize(n);
    sa.resize(m);
    for (int i = 0; i < n; ++i) cin >> fa[i];
    for (int i = 0; i < m; ++i) cin >> sa[i];
    dp.assign(n, vector<int>(m, -1));
    dp2.assign(n, vector<string>(m, ""));
    cout << go(0, 0) << endl;
    cout << go2(0, 0) << endl;
    return 0;
}