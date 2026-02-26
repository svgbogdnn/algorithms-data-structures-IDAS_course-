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
# static inline bool prefix(const vector<string> &words, int ai, int bi, unordered_map<unsigned long long, char> &memo){
#     const string &a = words[ai];
#     const string &b = words[bi];
#     int la = (int)a.size();
#     int lb = (int)b.size();
#     if (la >= lb) return false;
#
#     unsigned long long key = ( (unsigned long long)(unsigned int)ai << 32 )
#                            |  (unsigned long long)(unsigned int)bi;
#
#     auto it = memo.find(key);
#     if (it != memo.end()) {
#         return it->second != 0;
#     }
#
#     bool ok = (b.compare(0, la, a, 0, la) == 0);
#     memo.emplace(key, ok ? 1 : 0);
#     return ok;
# }
#
# pair<int,int> ChampagnePapi21(const vector<string> &words,
#                               const vector<int> &seq) {
#     int k = (int)seq.size();
#     if (k == 0) return {1, 1};
#
#     unordered_map<unsigned long long, char> memo;
#     memo.reserve((size_t)k * 2);
#
#     int best_len = 1;
#     int best_l = 1;
#     int best_r = 1;
#     int cur_l = 1;
#     int cur_len = 1;
#
#     int i = 0;
#     while (i < k - 1) {
#         int a_idx = seq[i];
#         int b_idx = seq[i + 1];
#
#         bool ok = prefix(words, a_idx, b_idx, memo);
#
#         if (ok) {
#             cur_len = cur_len + 1;
#             if (cur_len > best_len) {
#                 best_len = cur_len;
#                 best_l = cur_l;
#                 best_r = i + 2;
#             }
#         } else {
#             cur_l = i + 2;
#             cur_len = 1;
#         }
#         i = i + 1;
#     }
#     return {best_l, best_r};
# }
#
# int main() {
#     FastIO();
#
#     int m;
#     if (!(cin >> m)) return 0;
#     vector<string> words(m + 1);
#     int i = 1;
#     while (i <= m) {
#         cin >> words[i];
#         i = i + 1;
#     }
#
#     int k;
#     cin >> k;
#     vector<int> seq(k);
#     i = 0;
#     while (i < k) {
#         cin >> seq[i];
#         i = i + 1;
#     }
#
#     auto ans = ChampagnePapi21(words, seq);
#     cout << ans.first << ' ' << ans.second << '\n';
#     return 0;
# }

''' .6 ' Снова в космос - '''  # impossible

def prefix(s):
    n = len(s)
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
    return pi

def minper(s):
    n = len(s)
    pi = prefix(s)
    p = n - pi[n - 1]
    if p == 0:
        p = n
    return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    g = gcd(a, b)
    x = a // g
    y = x * b
    return y

def zalgo(t):
    n = len(t)
    z = [0] * n
    l = 0
    r = 0
    i = 1
    while i < n:
        if i <= r:
            k = i - l
            b = r - i + 1
            if z[k] < b:
                z[i] = z[k]
            else:
                z[i] = b
        while i + z[i] < n and t[z[i]] == t[i + z[i]]:
            z[i] = z[i] + 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        i = i + 1
    return z

def findRotationOffset(a, b):
    if len(a) != len(b):
        return -1
    n = len(a)
    if n == 0:
        return 0
    t = b + '#' + a + a
    z = zalgo(t)
    need = len(b)
    i = need + 1
    while i < len(t):
        if z[i] >= need:
            pos = i - (need + 1)
            return pos
        i = i + 1
    return -1

def eqrot(a, b, t):
    n = len(a)
    if n != len(b):
        return False
    j = 0
    while j < n:
        ai = (t + j) % n
        if a[ai] != b[j]:
            return False
        j = j + 1
    return True

def modinv(a, mod):
    t = 0
    newt = 1
    r = mod
    newr = a % mod
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r != 1:
        return -1
    if t < 0:
        t = t + mod
    return t



def solve():
    first = input().strip().split()
    r = int(first[0])
    c = int(first[1])

    rows = []
    i = 0
    while i < r:
        s = input().strip()
        rows.append(s)
        i = i + 1

    b = minper(rows[0])
    i = 1
    while i < r:
        p = minper(rows[i])
        b = lcm(b, p)
        i = i + 1

    if b > c // 2:
        b = c // 2

    temps = []
    i = 0
    while i < r:
        t = rows[i][0:b]
        temps.append(t)
        i = i + 1

    best_a = 1
    best_t = 0
    found = False

    a = 1
    limit = r // 2
    while a <= limit:
        if a >= r:
            break

        off = findRotationOffset(temps[0], temps[a])
        if off == -1:
            a = a + 1
            continue

        ok = True
        i = 0
        while i + a < r:
            good = eqrot(temps[i], temps[i + a], off)
            if not good:
                ok = False
                break
            i = i + 1

        if ok:
            best_a = a
            best_t = off % b
            found = True
            break

        a = a + 1

    if not found:
        best_a = 1
        best_t = 0

    g = gcd(best_a, b)
    if best_t % g != 0:
        best_t = best_t - (best_t % g)
    a1 = best_a // g
    b1 = b // g
    t1 = best_t // g
    inv = modinv(a1, b1)
    if inv == -1:
        s = 0
    else:
        s = (inv * t1) % b1
        s = s % b

    print(best_a, b, s)


if __name__ == '__main__':
    solve()
