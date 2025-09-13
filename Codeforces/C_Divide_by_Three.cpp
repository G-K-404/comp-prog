#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <algorithm>
#include <string>

using namespace std;

string divide_by_three(const string& n) {
    int length = n.size();
    vector<int> digits(length);
    bool zero_present = false;

    for (int i = 0; i < length; ++i) {
        digits[i] = n[i] - '0';
        if (n[i] == '0') zero_present = true;
    }

    const int MAX_SUM = 9 * length + 1;
    unordered_map<long long, int> max_digits;
    unordered_map<long long, bool> visited;
    vector<pair<int, int> > topo;

    stack<pair<int, int> > stk;
    stk.push(make_pair(0, 0));

    while (!stk.empty()) {
        pair<int, int> current = stk.top(); stk.pop();
        int i = current.first;
        int s = current.second;
        long long key = 1LL * i * MAX_SUM + s;

        if (visited.find(key) != visited.end()) continue;
        visited[key] = true;
        topo.push_back(make_pair(i, s));

        if (i < length) {
            stk.push(make_pair(i + 1, s + digits[i]));
            stk.push(make_pair(i + 1, s));
        }
    }

    reverse(topo.begin(), topo.end());

    for (size_t idx = 0; idx < topo.size(); ++idx) {
        int i = topo[idx].first;
        int s = topo[idx].second;
        long long key = 1LL * i * MAX_SUM + s;

        if (i == length) {
            bool valid = (s % 3 == 0) && (zero_present || s > 0);
            max_digits[key] = valid ? 0 : -1;
        } else {
            long long take_key = 1LL * (i + 1) * MAX_SUM + (s + digits[i]);
            long long skip_key = 1LL * (i + 1) * MAX_SUM + s;

            int take = (max_digits.find(take_key) != max_digits.end()) ? max_digits[take_key] : -1;
            int skip = (max_digits.find(skip_key) != max_digits.end()) ? max_digits[skip_key] : -1;

            int res = -1;
            if (take != -1) res = max(res, take + 1);
            if (skip != -1) res = max(res, skip);
            max_digits[key] = res;
        }
    }

    long long start_key = 0;
    if (max_digits.find(start_key) == max_digits.end() || max_digits[start_key] == -1)
        return "-1";

    string result;
    int i = 0, s = 0;
    while (i < length) {
        long long curr_key = 1LL * i * MAX_SUM + s;
        long long take_key = 1LL * (i + 1) * MAX_SUM + (s + digits[i]);
        long long skip_key = 1LL * (i + 1) * MAX_SUM + s;

        int curr = max_digits[curr_key];
        int take = (max_digits.find(take_key) != max_digits.end()) ? max_digits[take_key] : -1;
        int skip = (max_digits.find(skip_key) != max_digits.end()) ? max_digits[skip_key] : -1;

        if (take != -1 && take + 1 == curr) {
            result += char(digits[i] + '0');
            s += digits[i];
            i++;
        } else if (skip != -1 && skip == curr) {
            i++;
        } else {
            break;
        }
    }

    // Strip leading zeros
    size_t pos = 0;
    while (pos < result.size() && result[pos] == '0') ++pos;
    string final_result = result.substr(pos);
    return final_result.empty() ? "0" : final_result;
}

int main() {
    string n;
    cin >> n;
    cout << divide_by_three(n) << endl;
    return 0;
}
