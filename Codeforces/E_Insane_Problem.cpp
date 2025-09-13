#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
    auto II = []() { int x; cin >> x; return x; };
    auto LII = []() { 
        vector<int> x(5); 
        for (int i = 0; i < 5; ++i) cin >> x[i]; 
        return x; 
    };

    int t = II(); // Number of test cases
    while (t--) {
        vector<int> x = LII();
        long long k = x[0];
        long long l1 = x[1], r1 = x[2];
        long long l2 = x[3], r2 = x[4];

        set<long long> kvalues;
        long long kmax = r2 / l1;
        long long kmin = l2 / r1;

        long long m = k;
        while (m <= kmin) {
            m *= k;
        }

        while (m <= kmax) {
            kvalues.insert(m);
            if (m > r2 / k) break; // Prevent overflow
            m *= k;
        }

        int result = 0;

        for (long long x = l1; x <= r1; ++x) {
            for (long long y = l2; y <= r2; ++y) {
                if (kvalues.count(x * y)) {
                    ++result;
                }
            }
        }

        cout << result << endl;
    }

    return 0;
}
