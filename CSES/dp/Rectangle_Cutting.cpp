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
        return INT_MAX;
    }
    if (j >= str2.length()) {
        return INT_MAX;
    }
    if (i == str1.length() - 1 && j == str2.length() - 1) {
        return str1[i] == str2[j] ? 0 : 1;
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    if (str1[i] == str2[j]) {
        if (i + 1 < str1.length() && j + 1 < str2.length()) {
            return dp[i][j] = go(i + 1, j + 1);
        } else {
            if (j + 1 < str2.length()) {
                return dp[i][j] = str2.length() - j - 1;
            } else {
                return dp[i][j] = str1.length() - i - 1;
            }
        }
    }
    int ans = INT_MAX;
    int a = go(i + 1, j + 1) + 1;
    ans = min(ans, a);
    int b = go(i, j + 1) + 1;
    ans = min(ans, b);
    int c = go(i + 1, j) + 1;
    ans = min(ans, c);
    return dp[i][j] = ans;
}

int main() {
    cin >> str1 >> str2;
    dp.resize(str1.length(), vector<int>(str2.length(), -1));
    int r = go(0, 0);
    cout << r << endl;
    return 0;
}