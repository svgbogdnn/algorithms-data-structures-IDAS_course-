'''
https://official.contest.yandex.ru/contest/81974/problems
start 23.09.2025 - finish 12.10.2025 , 9 tasks
2155 lines
'''

''' .1 ' Телефонная книга + '''  # easy

def ChampagnePapi21(n):
    size = 10000000
    book = [None] * size
    out = []
    i = 0

    while i < n:
        parts = input().strip().split()
        cmd = parts[0]

        if cmd == 'add':
            number = int(parts[1])
            name = parts[2]
            book[number] = name

        elif cmd == 'del':
            number = int(parts[1])
            book[number] = None

        else:
            number = int(parts[1])
            name = book[number]
            if name is None:
                out.append('not found')
            else:
                out.append(name)

        i = i + 1

    return out

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    i = 0
    m = len(ans)

    while i < m:
        print(ans[i])
        i = i + 1

if __name__ == '__main__':
    solve()

''' .2 ' Хеширование цепочками + '''  # mid

def longliveDrizzy(s, m):
    p = 1000000007 # p=1000000007 — простое число
    x = 263 #a x=263
    power = 1
    h = 0
    i = 0
    n = len(s)

    while i < n:
        code = ord(s[i])
        addv = (code * power) % p
        h = (h + addv) % p
        power = (power * x) % p
        i = i + 1

    idx = h % m
    return idx

def ChampagnePapi21(m, q):
    table = []
    i = 0
    while i < m:
        table.append([])
        i = i + 1
    out = []
    j = 0

    while j < q:
        parts = input().strip().split()
        cmd = parts[0]

        if cmd == 'check':
            idx = int(parts[1])
            chain = table[idx]
            if len(chain) == 0:
                out.append('')
            else:
                pieces = []
                t = 0
                while t < len(chain):
                    pieces.append(chain[t])
                    t = t + 1
                line = ' '.join(pieces)
                out.append(line)

        elif cmd == 'add':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            found = False
            t = 0
            while t < len(chain):
                if chain[t] == s:
                    found = True
                    break
                t = t + 1
            if not found:
                chain.insert(0, s)

        elif cmd == 'del':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            t = 0
            pos = -1
            while t < len(chain):
                if chain[t] == s:
                    pos = t
                    break
                t = t + 1
            if pos != -1:
                chain.pop(pos)

        elif cmd == 'find':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            t = 0
            found = False
            while t < len(chain):
                if chain[t] == s:
                    found = True
                    break
                t = t + 1
            if found:
                out.append('yes')
            else:
                out.append('no')

        j = j + 1

    return out


def solve():
    s = input().strip()
    m = int(s)
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(m, n)
    i = 0
    k = len(ans)
    while i < k:
        print(ans[i])
        i = i + 1

if __name__ == '__main__':
    solve()

''' .3 ' Сравнения подстрок [АиСД] + '''  # mid

def ChampagnePapi21(s):
    n = len(s)
    p1 = 1000000007
    p2 = 1000000009
    x = 263

    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)

    i = 1
    while i <= n:
        c = ord(s[i - 1])
        pref1[i] = (pref1[i - 1] * x + c) % p1
        pref2[i] = (pref2[i - 1] * x + c) % p2
        pow1[i] = (pow1[i - 1] * x) % p1
        pow2[i] = (pow2[i - 1] * x) % p2
        i = i + 1

    state = (pref1, pref2, pow1, pow2, p1, p2)
    return state


def longliveDrizzy(pref, pw, mod, l, r):
    left = l - 1
    right = r
    a = pref[right]
    b = (pref[left] * pw[right - left]) % mod
    val = a - b
    val = val % mod
    return val


def solve():
    s = input().strip()
    state = ChampagnePapi21(s)
    pref1, pref2, pow1, pow2, p1, p2 = state
    line = input().strip()
    m = int(line)

    i = 0
    while i < m:
        parts = input().strip().split()
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
        d = int(parts[3])

        h1 = longliveDrizzy(pref1, pow1, p1, a, b)
        h2 = longliveDrizzy(pref1, pow1, p1, c, d)
        if h1 != h2:
            print('No')
            i = i + 1
            continue

        g1 = longliveDrizzy(pref2, pow2, p2, a, b)
        g2 = longliveDrizzy(pref2, pow2, p2, c, d)
        if g1 != g2:
            print('No')
        else:
            print('Yes')

        i = i + 1

if __name__ == '__main__':
    solve()

''' .4 ' Дана строка [АиСД] TL14, C++ +'''  # mid

def ChampagnePapi21(t):
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

def longliveDrizzy(a, b):
    if len(b) == 0 or len(a) == 0:
        return []
    if len(b) > len(a):
        return []

    sep = '#'
    t = b + sep + a
    z = ChampagnePapi21(t)
    m = len(b)
    res = []
    i = m + 1

    while i < len(t):
        if z[i] == m:
            pos = i - m - 1
            res.append(pos + 1)
        i = i + 1

    return res

def solve():
    a = input().strip()
    b = input().strip()
    occ = longliveDrizzy(a, b)
    print(len(occ))

    if len(occ) == 0:
        print()
    else:
        pieces = []
        i = 0
        while i < len(occ):
            pieces.append(str(occ[i]))
            i = i + 1
        line = ' '.join(pieces)
        print(line)

if __name__ == '__main__':
    solve()


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
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# vi ChampagnePapi21(const string &s){
#     int n = (int)s.size();
#     vi sa(n), rnk(n), tmp(n);
#     int i = 0;
#     while (i < n) {
#         sa[i] = i;
#         rnk[i] = (unsigned char)s[i];
#         i = i + 1;
#     }
#     int k = 1;
#     while (k < n) {
#         sort(all(sa), [&](int a, int b){
#             int ra1 = rnk[a];
#             int rb1 = rnk[b];
#             if (ra1 != rb1) {
#                 return ra1 < rb1;
#             }
#             int ra2, rb2;
#             if (a + k < n) {
#                 ra2 = rnk[a + k];
#             } else {
#                 ra2 = -1;
#             }
#             if (b + k < n) {
#                 rb2 = rnk[b + k];
#             } else {
#                 rb2 = -1;
#             }
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
#
#             int ra1 = rnk[a];
#             int rb1 = rnk[b];
#
#             int ra2;
#             if (a + k < n) {
#                 ra2 = rnk[a + k];
#             } else {
#                 ra2 = -1;
#             }
#
#             int rb2;
#             if (b + k < n) {
#                 rb2 = rnk[b + k];
#             } else {
#                 rb2 = -1;
#             }
#
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
#     return sa;
# }
#
# int longliveDrizzy(const string &s){
#     int n = (int)s.size();
#     if (n == 0) return 0;
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
#     int p = n - pi[n - 1];
#     if (p == 0) {
#         p = n;
#     }
#     return p;
# }
#
# string SixGodCooking(const string &S, int K){
#     int n = (int)S.size();
#     if (n == 0) {
#         return string("IMPOSSIBLE");
#     }
#
#     string T = S + S;
#     vi sa = ChampagnePapi21(T);
#
#     int p = longliveDrizzy(S);
#     vector<bool> seen(p, false);
#     vi order;
#     int i = 0;
#     int need = p;
#
#     while (i < sz(sa)) {
#         int pos = sa[i];
#         if (pos < n) {
#             int cls = pos % p;
#             if (!seen[cls]) {
#                 seen[cls] = true;
#                 order.push_back(cls);
#                 if (sz(order) == need) {
#                     break;
#                 }
#             }
#         }
#         i = i + 1;
#     }
#
#     if (K < 1 || K > sz(order)) {
#         return string("IMPOSSIBLE");
#     }
#
#     int start = order[K - 1];
#     string res = S.substr(start) + S.substr(0, start);
#     return res;
# }
#
# int main(){
#     FastIO();
#     string S;
#     if (!(cin >> S)) {
#         return 0;
#     }
#     int k;
#     cin >> k;
#     string ans = SixGodCooking(S, k);
#     cout << ans << eol;
#     return 0;
# }

''' .8 ' Шифр Бэкона + '''  # hardly ever

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

    k = 1
    tmp = [0] * n
    while k < n:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))

        tmp[sa[0]] = 0
        classes = 1
        i = 1
        while i < n:
            a = sa[i - 1]
            b = sa[i]
            ra1 = rank[a]
            rb1 = rank[b]
            ra2 = rank[a + k] if a + k < n else -1
            rb2 = rank[b + k] if b + k < n else -1
            if ra1 != rb1 or ra2 != rb2:
                classes = classes + 1
            tmp[b] = classes - 1
            i = i + 1

        i = 0
        while i < n:
            rank[i] = tmp[i]
            i = i + 1

        if classes == n:
            break
        k = k * 2

    return sa

def longliveDrizzy(s, sa):
    n = len(s)
    if n == 0:
        return []

    rank = [0] * n
    i = 0
    while i < n:
        rank[sa[i]] = i
        i = i + 1

    lcp = [0] * n
    k = 0
    i = 0
    while i < n:
        r = rank[i]
        if r == n - 1:
            k = 0
            i = i + 1
            continue
        j = sa[r + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k = k + 1
        lcp[r] = k
        if k > 0:
            k = k - 1
        i = i + 1

    return lcp

def solve():
    s = input().strip()
    sa = ChampagnePapi21(s)
    lcp = longliveDrizzy(s, sa)

    n = len(s)
    total = n * (n + 1) // 2

    sum_lcp = 0
    i = 0
    while i < len(lcp):
        sum_lcp = sum_lcp + lcp[i]
        i = i + 1

    ans = total - sum_lcp
    print(ans)

if __name__ == '__main__':
    solve()

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