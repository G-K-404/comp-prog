#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>

using namespace std;

string str1, str2;
vector<vector<int>> dp;

int go(int i, int j) {
    if (i >= str1.length()) {
        return str2.length() - j;
    }
    if (j >= str2.length()) {
        return str1.length() - i;
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    if (str1[i] == str2[j]) {
        return dp[i][j] = go(i + 1, j + 1);
    }
    int ans = INT_MAX;
    ans = min(ans, go(i + 1, j + 1) + 1); // Replace
    ans = min(ans, go(i, j + 1) + 1);     // Insert
    ans = min(ans, go(i + 1, j) + 1);     // Delete
    return dp[i][j] = ans;
}

int main() {
    cin >> str1 >> str2;
    dp.resize(5001, vector<int>(5001, -1));
    int r = go(0, 0);
    cout << r << endl;
    return 0;
}