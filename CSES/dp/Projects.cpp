#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Job {
    int start, end, profit;
};

// Comparator to sort jobs based on end time
bool compare(Job a, Job b) {
    return a.end < b.end;
}

// Binary search to find the last job that does not overlap
int findLastNonConflicting(vector<Job>& jobs, int index) {
    int low = 0, high = index - 1, ans = -1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (jobs[mid].end < jobs[index].start) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<Job> jobs(n);

    for (int i = 0; i < n; i++) {
        cin >> jobs[i].start >> jobs[i].end >> jobs[i].profit;
    }

    // Sort jobs by end time
    sort(jobs.begin(), jobs.end(), compare);

    // DP array to store the maximum profit
    vector<long long> dp(n, 0);

    // Base case: The maximum profit by taking only the first job
    dp[0] = jobs[0].profit;

    for (int i = 1; i < n; i++) {
        // Option 1: Exclude the current job
        long long exclude = dp[i - 1];

        // Option 2: Include the current job
        int last = findLastNonConflicting(jobs, i);
        long long include = jobs[i].profit;
        if (last != -1) {
            include += dp[last];
        }

        // Take the maximum of both options
        dp[i] = max(exclude, include);
    }

    // Final answer is the max profit we can get
    cout << dp[n - 1] << "\n";

    return 0;
}
