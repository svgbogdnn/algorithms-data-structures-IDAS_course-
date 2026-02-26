# C++
# '''
# #include <iostream>
# #include <vector>
# #include <string>
# #include <algorithm>
# #include <cmath>
# #include <cstdio>
# #include <cstdlib>
# #include <ctime>
# #include <cstring>
# #include <fstream>
# #include <sstream>
# #include <iomanip>
# #include <queue>
# #include <stack>
# #include <list>
# #include <map>
# #include <set>
# #include <unordered_map>
# #include <unordered_set>
# #include <bitset>
# #include <functional>
# #include <iterator>
# #include <stdexcept>
# #include <typeinfo>
# #include <utility>
# #include <bits/stdc++.h>
#
# using namespace std;
#
# template <class T> void print(T v) { for (auto e: v) cout << e << " "; cout << '\n';}
# #define FastIO() {ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);}
# #define INF 0x3f3f3f3f3f3f //
# #define fi first
# #define se second
# #define ld long double
# typedef vector<int> vi;
# typedef vector<vi> vvi;
# typedef long long ll;
# typedef unsigned long long ull;
# #define eol '\n'
# #define deb(x) cout << #x << " = " << x << '\n';
# #define pii pair<int, int>
# #define all(a) (a).begin(), (a).end()
# #define sz(x) ((int)(x).size())
# #define mfor(i, start, end) for (int i = (start); i < (end); i++)
# #define rep(i, n) for (int i = 0; i < (n); i++)
# #define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
# #define fill(x, y) memset(x, y, sizeof(x))
# #define sqr(x) ((x)*(x))
# #define unq(x) (x.resize(unique(all(x)) - x.begin()))
# #define readArr(arr, n) {for (int i = 0; i < n; i++) cin >> arr[i];}
# #define pi acos(-1.0);
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# vector<long long> longliveDrizzy(const vector<long long> &arr, int k, long long base, long long mod) {
#     int n = (int)arr.size();
#     if (k > n) {
#         return {};
#     }
#
#     long long p = 1;
#     int i = 1;
#     while (i < k) {
#         p = (p * base) % mod;
#         i = i + 1;
#     }
#
#     vector<long long> res;
#     long long h = 0;
#     i = 0;
#     while (i < k) {
#         h = (h * base + arr[i]) % mod;
#         i = i + 1;
#     }
#     res.push_back(h);
#
#     i = k;
#     while (i < n) {
#         long long outv = arr[i - k];
#         h = (h - (outv * p) % mod) % mod;
#         if (h < 0) {
#             h = h + mod;
#         }
#         h = (h * base + arr[i]) % mod;
#         res.push_back(h);
#         i = i + 1;
#     }
#
#     return res;
# }
#
# vector<long long> SixGodCooking(const vector<long long> &colvals, int k, long long base, long long mod) {
#     return longliveDrizzy(colvals, k, base, mod);
# }
#
# long long ChampagnePapi21(const vector<string> &grid, int n, int m, int k) {
#     const long long mod1 = 1000000007LL;
#     const long long mod2 = 1000000009LL;
#     const long long br = 911382323LL;
#     const long long bc = 972663749LL;
#
#     long long p_row_1 = 1;
#     long long p_row_2 = 1;
#     int i = 1;
#     while (i < k) {
#         p_row_1 = (p_row_1 * br) % mod1;
#         p_row_2 = (p_row_2 * br) % mod2;
#         i = i + 1;
#     }
#
#     vector<vector<long long>> rowh1(n, vector<long long>(m - k + 1));
#     vector<vector<long long>> rowh2(n, vector<long long>(m - k + 1));
#
#     int r = 0;
#     while (r < n) {
#         const string &row = grid[r];
#         long long h1 = 0;
#         long long h2 = 0;
#
#         int j = 0;
#         while (j < k) {
#             int v = (unsigned char)row[j];
#             h1 = (h1 * br + v) % mod1;
#             h2 = (h2 * br + v) % mod2;
#             j = j + 1;
#         }
#         rowh1[r][0] = h1;
#         rowh2[r][0] = h2;
#
#         j = k;
#         int idx = 1;
#         while (j < m) {
#             int vout = (unsigned char)row[j - k];
#             int vnew = (unsigned char)row[j];
#
#             h1 = (h1 - (vout * p_row_1) % mod1) % mod1;
#             if (h1 < 0) {
#                 h1 = h1 + mod1;
#             }
#             h1 = (h1 * br + vnew) % mod1;
#
#             h2 = (h2 - (vout * p_row_2) % mod2) % mod2;
#             if (h2 < 0) {
#                 h2 = h2 + mod2;
#             }
#             h2 = (h2 * br + vnew) % mod2;
#
#             rowh1[r][idx] = h1;
#             rowh2[r][idx] = h2;
#             j = j + 1;
#             idx = idx + 1;
#         }
#
#         r = r + 1;
#     }
#
#     unordered_set<ull> seen;
#     int col = 0;
#     while (col <= m - k) {
#         vector<long long> colvals1;
#         vector<long long> colvals2;
#         colvals1.reserve(n);
#         colvals2.reserve(n);
#
#         r = 0;
#         while (r < n) {
#             colvals1.push_back(rowh1[r][col]);
#             colvals2.push_back(rowh2[r][col]);
#             r = r + 1;
#         }
#
#         vector<long long> vhash1 = SixGodCooking(colvals1, k, bc, mod1);
#         vector<long long> vhash2 = SixGodCooking(colvals2, k, bc, mod2);
#
#         int t = 0;
#         int limit = n - k + 1;
#         while (t < limit) {
#             ull a = (ull)vhash1[t];
#             ull b = (ull)vhash2[t];
#             ull key = (a << 32) ^ b;
#             seen.insert(key);
#             t = t + 1;
#         }
#
#         col = col + 1;
#     }
#
#     long long ret = (long long)seen.size();
#     return ret;
# }
#
# int main() {
#     FastIO();
#
#     int n, m, k;
#     if (!(cin >> n >> m >> k)) {
#         return 0;
#     }
#
#     vector<string> grid(n);
#     int i = 0;
#     while (i < n) {
#         cin >> grid[i];
#         i = i + 1;
#     }
#
#     long long res = ChampagnePapi21(grid, n, m, k);
#     cout << res << eol;
#     return 0;
# }
