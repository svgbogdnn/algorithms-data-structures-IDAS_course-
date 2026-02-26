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
# vi ChampagnePapi21(const string &s){
#     int n = (int)s.size();
#     vi sa(n), rnk(n), tmp(n);
#     int i = 0;
#
#     while (i < n) {
#         sa[i] = i;
#         rnk[i] = (unsigned char)s[i];
#         i = i + 1;
#     }
#
#     int k = 1;
#     while (k < n) {
#         sort(all(sa), [&](int a, int b){
#             int ra1 = rnk[a];
#             int rb1 = rnk[b];
#             int ra2 = (a + k < n) ? rnk[a + k] : -1;
#             int rb2 = (b + k < n) ? rnk[b + k] : -1;
#             if (ra1 != rb1) return ra1 < rb1;
#             return ra2 < rb2;
#         });
#
#         tmp[sa[0]] = 0;
#         int classes = 1;
#
#         i = 1;
#         while (i < n) {
#             int a = sa[i - 1];
#             int b = sa[i];
#             int ra1 = rnk[a];
#             int rb1 = rnk[b];
#             int ra2 = (a + k < n) ? rnk[a + k] : -1;
#             int rb2 = (b + k < n) ? rnk[b + k] : -1;
#             if (ra1 != rb1 || ra2 != rb2) {
#                 classes = classes + 1;
#             }
#             tmp[b] = classes - 1;
#             i = i + 1;
#         }
#
#         i = 0;
#         while (i < n) {
#             rnk[i] = tmp[i];
#             i = i + 1;
#         }
#
#         if (classes == n) {
#             break;
#         }
#         k = k * 2;
#     }
#
#     return sa;
# }
#
# vi longliveDrizzy(const string &s, const vi &sa){
#     int n = (int)s.size();
#     vi rnk(n), lcp(n, 0);
#
#     int i = 0;
#     while (i < n) {
#         rnk[sa[i]] = i;
#         i = i + 1;
#     }
#
#     int k = 0;
#     i = 0;
#     while (i < n) {
#         int r = rnk[i];
#         if (r == n - 1) {
#             k = 0;
#             i = i + 1;
#             continue;
#         }
#
#         int j = sa[r + 1];
#         while (true) {
#             bool c1 = (i + k < n);
#             bool c2 = (j + k < n);
#             if (!c1 || !c2) {
#                 break;
#             }
#             if (s[i + k] != s[j + k]) {
#                 break;
#             }
#             k = k + 1;
#         }
#
#         lcp[r] = k;
#         if (k > 0) {
#             k = k - 1;
#         }
#         i = i + 1;
#     }
#
#     return lcp;
# }
#
# int main(){
#     FastIO();
#
#     string s;
#     if (!(cin >> s)) {
#         return 0;
#     }
#
#     vi sa = ChampagnePapi21(s);
#     vi lcp = longliveDrizzy(s, sa);
#
#     ll n = (ll)s.size();
#     ll total = n * (n + 1) / 2;
#
#     ll sum_lcp = 0;
#     int i = 0;
#     while (i < sz(lcp)) {
#         sum_lcp = sum_lcp + lcp[i];
#         i = i + 1;
#     }
#
#     ll ans = total - sum_lcp;
#     cout << ans << eol;
#     return 0;
# }

''' .9 ' Количество подматриц + '''  # hard

def longliveDrizzy(arr, k, base, mod):
    n = len(arr)
    if k > n:
        return []
    p = 1
    i = 1
    while i < k:
        p = (p * base) % mod
        i = i + 1

    res = []
    h = 0
    i = 0
    while i < k:
        h = (h * base + arr[i]) % mod
        i = i + 1
    res.append(h)

    i = k
    while i < n:
        outv = arr[i - k]
        h = (h - (outv * p) % mod) % mod
        h = (h * base + arr[i]) % mod
        res.append(h)
        i = i + 1
    return res


def SixGodCooking(colvals, k, base, mod):
    return longliveDrizzy(colvals, k, base, mod)


def ChampagnePapi21(grid, n, m, k):
    mod1 = 1000000007
    mod2 = 1000000009
    br = 911382323
    bc = 972663749

    p_row_1 = 1
    p_row_2 = 1
    i = 1
    while i < k:
        p_row_1 = (p_row_1 * br) % mod1
        p_row_2 = (p_row_2 * br) % mod2
        i = i + 1

    rowh1 = []
    rowh2 = []
    r = 0
    while r < n:
        row = grid[r]
        a1 = [0] * (m - k + 1)
        a2 = [0] * (m - k + 1)

        h1 = 0
        h2 = 0
        j = 0
        while j < k:
            v = ord(row[j])
            h1 = (h1 * br + v) % mod1
            h2 = (h2 * br + v) % mod2
            j = j + 1
        a1[0] = h1
        a2[0] = h2

        j = k
        idx = 1
        while j < m:
            vout = ord(row[j - k])
            vnew = ord(row[j])

            h1 = (h1 - (vout * p_row_1) % mod1) % mod1
            h1 = (h1 * br + vnew) % mod1

            h2 = (h2 - (vout * p_row_2) % mod2) % mod2
            h2 = (h2 * br + vnew) % mod2

            a1[idx] = h1
            a2[idx] = h2
            j = j + 1
            idx = idx + 1

        rowh1.append(a1)
        rowh2.append(a2)
        r = r + 1

    seen = set()
    col = 0
    while col <= m - k:
        colvals1 = []
        colvals2 = []
        r = 0
        while r < n:
            colvals1.append(rowh1[r][col])
            colvals2.append(rowh2[r][col])
            r = r + 1

        vhash1 = SixGodCooking(colvals1, k, bc, mod1)
        vhash2 = SixGodCooking(colvals2, k, bc, mod2)

        t = 0
        limit = n - k + 1
        while t < limit:
            key = (vhash1[t] << 32) ^ vhash2[t]
            seen.add(key)
            t = t + 1

        col = col + 1

    ret = len(seen)
    return ret


def solve():
    first = input().strip().split()
    n = int(first[0])
    m = int(first[1])
    k = int(first[2])

    grid = []
    i = 0
    while i < n:
        s = input().strip()
        grid.append(s)
        i = i + 1

    res = ChampagnePapi21(grid, n, m, k)
    print(res)


if __name__ == '__main__':
    solve()
