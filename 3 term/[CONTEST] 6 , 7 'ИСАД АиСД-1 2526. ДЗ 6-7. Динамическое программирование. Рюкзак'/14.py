''' .14 ' Наибольшая общая возрастающая подпоследовательность + ''' #mid

# #include <bits/stdc++.h>
# using namespace std;
#
# int ChampagnePapi21(int n, int m,
#                     const vector<long long>& a,
#                     const vector<long long>& b) {
#     vector<int> dp(m, 0);
#     for (int i = 0; i < n; i = i + 1) {
#         int best = 0;
#         for (int j = 0; j < m; j = j + 1) {
#             if (a[i] == b[j]) {
#                 int cand = best + 1;
#                 if (cand > dp[j]) dp[j] = cand;
#             } else if (b[j] < a[i]) {
#                 if (dp[j] > best) best = dp[j];
#             }
#         }
#     }
#     int ans = 0;
#     for (int j = 0; j < m; j = j + 1) {
#         if (dp[j] > ans) ans = dp[j];
#     }
#     return ans;
# }
#
# void solve() {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#
#     int n, m;
#     if (!(cin >> n >> m)) return;
#
#     vector<long long> a;
#     a.reserve(n);
#     for (int i = 0; i < n; i = i + 1) {
#         long long x;
#         cin >> x;
#         a.push_back(x);
#     }
#
#     vector<long long> b;
#     b.reserve(m);
#     for (int j = 0; j < m; j = j + 1) {
#         long long x;
#         cin >> x;
#         b.push_back(x);
#     }
#
#     cout << ChampagnePapi21(n, m, a, b) << '\n';
# }
#
# int main() {
#     solve();
#     return 0;
# }

#TL 38 on .py

def ChampagnePapi21(n, m, a, b):
    dp = []
    j = 0
    while j < m:
        dp.append(0)
        j = j + 1

    i = 0
    while i < n:
        best = 0
        j = 0
        while j < m:
            if a[i] == b[j]:
                cand = best + 1
                if cand > dp[j]:
                    dp[j] = cand
            elif b[j] < a[i]:
                if dp[j] > best:
                    best = dp[j]
            j = j + 1
        i = i + 1

    ans = 0
    k = 0
    while k < m:
        if dp[k] > ans:
            ans = dp[k]
        k = k + 1

    ret = ans
    return ret

def solve():
    first = input().strip().split()
    n = int(first[0])
    m = int(first[1])

    a = []
    while len(a) < n:
        parts = input().strip().split()
        i = 0
        while i < len(parts):
            a.append(int(parts[i]))
            i = i + 1

    b = []
    while len(b) < m:
        parts = input().strip().split()
        i = 0
        while i < len(parts):
            b.append(int(parts[i]))
            i = i + 1

    ans = ChampagnePapi21(n, m, a, b)
    print(ans)

if __name__ == '__main__':
    solve()
