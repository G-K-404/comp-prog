#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
int n, m, k;
vector<int> arr;
vector<int> prefix;
vector<tuple<int, int, int>> queries;
vector<long long> answers;
int BLOCK;

bool mo_cmp(const tuple<int, int, int> &a, const tuple<int, int, int> &b) {
    int block_a = get<0>(a) / BLOCK;
    int block_b = get<0>(b) / BLOCK;
    if (block_a != block_b) return block_a < block_b;
    return get<1>(a) < get<1>(b);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m >> k;
    arr.resize(n);
    prefix.resize(n + 1);
    answers.resize(m);

    for (int i = 0; i < n; ++i) cin >> arr[i];

    prefix[0] = 0;
    for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] ^ arr[i];

    BLOCK = sqrt(n) + 1;

    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        queries.emplace_back(l, r, i);
    }

    sort(queries.begin(), queries.end(), mo_cmp);

    unordered_map<int, int> freq;
    freq[0] = 1;

    int curr_l = 1, curr_r = 0;
    long long cnt = 0;

    for (auto &[l, r, idx] : queries) {
        while (curr_r < r) {
            ++curr_r;
            int val = prefix[curr_r];
            cnt += freq[val ^ k];
            ++freq[val];
        }
        while (curr_r > r) {
            int val = prefix[curr_r];
            --freq[val];
            cnt -= freq[val ^ k];
            --curr_r;
        }
        while (curr_l < l) {
            int val = prefix[curr_l - 1];
            --freq[val];
            cnt -= freq[val ^ k];
            ++curr_l;
        }
        while (curr_l > l) {
            --curr_l;
            int val = prefix[curr_l - 1];
            cnt += freq[val ^ k];
            ++freq[val];
        }

        answers[idx] = cnt;
    }

    for (auto ans : answers) cout << ans << '\n';

    return 0;
}
