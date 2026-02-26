# C++
# #
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
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# vi prefix(const string &s){
#     int n = (int)s.size();
#     vi pi(n, 0);
#     int i = 1;
#     while (i < n) {
#         int j = pi[i - 1];
#         while (j > 0 && s[i] != s[j]) {
#             j = pi[j - 1];
#         }
#         if (s[i] == s[j]) {
#             j = j + 1;
#         }
#         pi[i] = j;
#         i = i + 1;
#     }
#     return pi;
# }
#
# int minper(const string &s){
#     int n = (int)s.size();
#     vi pi = prefix(s);
#     int p = n - pi[n - 1];
#     if (p == 0) {
#         p = n;
#     }
#     return p;
# }
#
# long long gcdll(long long a, long long b){
#     while (b != 0) {
#         long long t = a % b;
#         a = b;
#         b = t;
#     }
#     return a;
# }
#
# long long lcmll(long long a, long long b){
#     long long g = gcdll(a, b);
#     long long x = a / g;
#     long long y = x * b;
#     return y;
# }
#
# vi zalgo(const string &t){
#     int n = (int)t.size();
#     vi z(n, 0);
#     int l = 0;
#     int r = 0;
#     int i = 1;
#     while (i < n) {
#         if (i <= r) {
#             int k = i - l;
#             int b = r - i + 1;
#             if (z[k] < b) {
#                 z[i] = z[k];
#             } else {
#                 z[i] = b;
#             }
#         }
#         while (i + z[i] < n && t[z[i]] == t[i + z[i]]) {
#             z[i] = z[i] + 1;
#         }
#         if (i + z[i] - 1 > r) {
#             l = i;
#             r = i + z[i] - 1;
#         }
#         i = i + 1;
#     }
#     return z;
# }
#
# int findRotationOffset(const string &a, const string &b){
#     if ((int)a.size() != (int)b.size()) {
#         return -1;
#     }
#     int n = (int)a.size();
#     if (n == 0) {
#         return 0;
#     }
#     string t;
#     t.reserve(b.size() + 1 + 2 * a.size());
#     t += b;
#     t += '#';
#     t += a;
#     t += a;
#
#     vi z = zalgo(t);
#     int need = (int)b.size();
#     int i = need + 1;
#     while (i < (int)t.size()) {
#         if (z[i] >= need) {
#             int pos = i - (need + 1);
#             return pos;
#         }
#         i = i + 1;
#     }
#     return -1;
# }
#
# bool eqrot(const string &a, const string &b, int t){
#     int n = (int)a.size();
#     if (n != (int)b.size()) {
#         return false;
#     }
#     int j = 0;
#     while (j < n) {
#         int ai = (t + j) % n;
#         if (a[ai] != b[j]) {
#             return false;
#         }
#         j = j + 1;
#     }
#     return true;
# }
#
# long long modinv(long long a, long long mod){
#     long long t = 0;
#     long long newt = 1;
#     long long r = mod;
#     long long newr = a % mod;
#
#     while (newr != 0) {
#         long long q = r / newr;
#         long long tt = newt;
#         newt = t - q * newt;
#         t = tt;
#
#         long long rr = newr;
#         newr = r - q * newr;
#         r = rr;
#     }
#
#     if (r != 1) {
#         return -1;
#     }
#     if (t < 0) {
#         t = t + mod;
#     }
#     return t;
# }
#
# int main(){
#     FastIO();
#
#     int r, c;
#     if (!(cin >> r >> c)) {
#         return 0;
#     }
#
#     vector<string> rows(r);
#     int i = 0;
#     while (i < r) {
#         cin >> rows[i];
#         i = i + 1;
#     }
#
#     long long b = minper(rows[0]);
#     i = 1;
#     while (i < r) {
#         int p = minper(rows[i]);
#         b = lcmll(b, (long long)p);
#         i = i + 1;
#     }
#
#     if (b > c / 2) {
#         b = c / 2;
#     }
#
#     vector<string> temps(r);
#     i = 0;
#     while (i < r) {
#         temps[i] = rows[i].substr(0, (int)b);
#         i = i + 1;
#     }
#
#     long long best_a = 1;
#     long long best_t = 0;
#     bool found = false;
#
#     long long a = 1;
#     long long limit = r / 2;
#     while (a <= limit) {
#         if (a >= r) {
#             break;
#         }
#
#         int off = findRotationOffset(temps[0], temps[(int)a]);
#         if (off == -1) {
#             a = a + 1;
#             continue;
#         }
#
#         bool ok = true;
#         int j = 0;
#         while (j + a < r) {
#             bool good = eqrot(temps[j], temps[j + a], off);
#             if (!good) {
#                 ok = false;
#                 break;
#             }
#             j = j + 1;
#         }
#
#         if (ok) {
#             best_a = a;
#             best_t = ((long long)off) % b;
#             found = true;
#             break;
#         }
#
#         a = a + 1;
#     }
#
#     if (!found) {
#         best_a = 1;
#         best_t = 0;
#     }
#
#     long long g = gcdll(best_a, b);
#     if (best_t % g != 0) {
#         best_t = best_t - (best_t % g);
#     }
#
#     long long a1 = best_a / g;
#     long long b1 = b / g;
#     long long t1 = best_t / g;
#
#     long long inv = modinv(a1, b1);
#     long long s;
#     if (inv == -1) {
#         s = 0;
#     } else {
#         s = (inv * t1) % b1;
#         s = s % b;
#     }
#
#     cout << best_a << ' ' << b << ' ' << s << eol;
#     return 0;
# }

''' .7 ' Циклические сдвиги - '''  # impossible

def ChampagnePapi21(s):
    n = len(s)
    if n == 0:
        return []
    sa = [0] * n
    i = 0
    while i < n:
        sa[i] = i
        i = i + 1
    rank = [0] * n
    i = 0
    while i < n:
        rank[i] = ord(s[i])
        i = i + 1
    tmp = [0] * n
    k = 1
    while k < n:
        maxr = 0
        i = 0
        while i < n:
            if rank[i] > maxr:
                maxr = rank[i]
            i = i + 1
        size = maxr + 2

        key2 = [0] * n
        i = 0
        while i < n:
            j = i + k
            if j < n:
                key2[i] = rank[j] + 1
            else:
                key2[i] = 0
            i = i + 1

        cnt = [0] * size
        i = 0
        while i < n:
            cnt[key2[sa[i]]] = cnt[key2[sa[i]]] + 1
            i = i + 1
        i = 1
        while i < size:
            cnt[i] = cnt[i] + cnt[i - 1]
            i = i + 1
        i = n - 1
        while i >= 0:
            v = sa[i]
            key = key2[v]
            cnt[key] = cnt[key] - 1
            pos = cnt[key]
            tmp[pos] = v
            i = i - 1
        i = 0
        while i < n:
            sa[i] = tmp[i]
            i = i + 1

        key1 = [0] * n
        i = 0
        while i < n:
            key1[i] = rank[i] + 1
            i = i + 1

        cnt = [0] * (maxr + 2 + 1)
        i = 0
        while i < n:
            cnt[key1[sa[i]]] = cnt[key1[sa[i]]] + 1
            i = i + 1
        i = 1
        while i < len(cnt):
            cnt[i] = cnt[i] + cnt[i - 1]
            i = i + 1
        i = n - 1
        while i >= 0:
            v = sa[i]
            key = key1[v]
            cnt[key] = cnt[key] - 1
            pos = cnt[key]
            tmp[pos] = v
            i = i - 1
        i = 0
        while i < n:
            sa[i] = tmp[i]
            i = i + 1

        newrank = [0] * n
        newrank[sa[0]] = 0
        classes = 1
        i = 1
        while i < n:
            a = sa[i - 1]
            b = sa[i]
            ra1 = rank[a]
            rb1 = rank[b]
            ja = a + k
            jb = b + k
            if ja < n:
                ra2 = rank[ja]
            else:
                ra2 = -1
            if jb < n:
                rb2 = rank[jb]
            else:
                rb2 = -1
            if ra1 != rb1 or ra2 != rb2:
                classes = classes + 1
            newrank[b] = classes - 1
            i = i + 1
        rank = newrank
        if classes == n:
            break
        k = k * 2
    return sa


def longliveDrizzy(s):
    n = len(s)
    if n == 0:
        return 0
    pi = [0] * n
    i = 1
    while i < n:
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j = j + 1
        pi[i] = j
        i = i + 1
    p = n - pi[n - 1]
    if p == 0:
        p = n
    return p


def SixGodCooking(S, K):
    n = len(S)
    if n == 0:
        return 'IMPOSSIBLE'
    T = S + S
    sa = ChampagnePapi21(T)
    p = longliveDrizzy(S)
    seen = [False] * p
    order = []
    i = 0
    need = p
    while i < len(sa):
        pos = sa[i]
        if pos < n:
            cls = pos % p
            if not seen[cls]:
                seen[cls] = True
                order.append(cls)
                if len(order) == need:
                    break
        i = i + 1
    if K < 1 or K > len(order):
        return 'IMPOSSIBLE'
    start = order[K - 1]
    res = S[start:n] + S[0:start]
    return res


def solve():
    S = input().rstrip('\n')
    line = input().strip()
    k = int(line)
    ans = SixGodCooking(S, k)
    print(ans)
if __name__ == '__main__':
    solve()
