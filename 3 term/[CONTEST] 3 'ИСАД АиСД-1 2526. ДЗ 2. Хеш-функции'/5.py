# C++
#
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
# vector<int> ChampagnePapi21(const string &t) {
#
#     int n = (int)t.size();
#     vector<int> z(n, 0);
#     int l = 0, r = 0, i = 1;
#
#     while (i < n) {
#         if (i <= r) {
#             int k = i - l;
#             int b = r - i + 1;
#             if (z[k] < b) z[i] = z[k];
#             else z[i] = b;
#         }
#
#         while (i + z[i] < n && t[z[i]] == t[i + z[i]]) z[i] = z[i] + 1;
#         if (i + z[i] - 1 > r) {
#             l = i;
#             r = i + z[i] - 1;
#         }
#
#         i = i + 1;
#     }
#
#     return z;
# }
#
# vector<int> longliveDrizzy(const string &a, const string &b) {
#     if (b.empty() || a.empty()) return {};
#     if (b.size() > a.size()) return {};
#
#     char sep = '#';
#     string t;
#     t.reserve(b.size() + 1 + a.size());
#     t += b;
#     t += sep;
#     t += a;
#     vector<int> z = ChampagnePapi21(t);
#     int m = (int)b.size();
#     vector<int> res;
#     int i = m + 1;
#
#     while (i < (int)t.size()) {
#         if (z[i] == m) {
#             int pos = i - m - 1;
#             res.push_back(pos + 1);
#         }
#
#         i = i + 1;
#     }
#
#     return res;
# }
#
# int main() {
#     FastIO();
#     string a, b;
#     if (!(cin >> a)) return 0;
#     cin >> b;
#     vector<int> occ = longliveDrizzy(a, b);
#     cout << occ.size() << '\n';
#
#     if (occ.empty()) {
#         cout << '\n';
#
#     } else {
#         for (int i = 0; i < (int)occ.size(); i = i + 1) {
#             if (i) cout << ' ';
#             cout << occ[i];
#         }
#         cout << '\n';
#     }
#
#     return 0;
# }

''' .5 ' Цепочка слов + '''  # light hard

def longliveDrizzy(a, b):
    la = len(a)
    lb = len(b)
    if la >= lb:
        return False

    i = 0
    while i < la:
        if a[i] != b[i]:
            return False
        i = i + 1
    return True

def ChampagnePapi21(words, seq):
    k = len(seq)
    if k == 0:
        return (1, 1)

    best_len = 1
    best_l = 1
    best_r = 1
    cur_l = 1
    cur_len = 1

    i = 0
    while i < k - 1:
        a_idx = seq[i]
        b_idx = seq[i + 1]
        a = words[a_idx]
        b = words[b_idx]
        ok = longliveDrizzy(a, b)

        if ok:
            cur_len = cur_len + 1
            if cur_len > best_len:
                best_len = cur_len
                best_l = cur_l
                best_r = i + 2

        else:
            cur_l = i + 2
            cur_len = 1

        i = i + 1

    return (best_l, best_r)

def solve():
    s = input().strip()
    m = int(s)
    words = ['']
    i = 0

    while i < m:
        w = input().strip()
        words.append(w)
        i = i + 1

    s = input().strip()
    k = int(s)
    seq = []
    parts = input().strip().split()
    j = 0

    while j < k:
        val = int(parts[j])
        seq.append(val)
        j = j + 1

    l, r = ChampagnePapi21(words, seq)
    print(l, r)

if __name__ == '__main__':
    solve()
