#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int n;
vector<double> probs;
vector<vector<double>> dp;
vector<vector<bool>> visited;

double go(int i, int cnt) {
    if (i == n) {
        return (cnt > n / 2) ? 1.0 : 0.0;
    }
    if (visited[i][cnt]) return dp[i][cnt];

    visited[i][cnt] = true;
    double take = go(i + 1, cnt + 1) * probs[i];
    double ntake = go(i + 1, cnt) * (1 - probs[i]);
    dp[i][cnt] = take + ntake;

    return dp[i][cnt];
}

int main() {
    cin >> n;
    probs.resize(n);
    dp.assign(n + 1, vector<double>(n + 1, 0.0));
    visited.assign(n + 1, vector<bool>(n + 1, false));

    for (int i = 0; i < n; ++i) {
        cin >> probs[i];
    }

    cout << fixed << setprecision(9) << go(0, 0) << endl;

    return 0;
}
