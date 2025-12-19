'''
https://official.contest.yandex.ru/contest/86178/problems/
start 26.11.2025 - finish 08.12.2025 , 5 tasks , 5/5
864 lines
'''

''' .1 ' Куча камней [Отжиг] + ''' #very hard

import sys
import time
import math
import random

def longliveDrizzy(n, w, side, s0, s1, idx):
    wi = w[idx]
    if side[idx] == 0:
        ns0 = s0 - wi
        ns1 = s1 + wi
    else:
        ns0 = s0 + wi
        ns1 = s1 - wi
    ndiff = ns0 - ns1
    if ndiff < 0:
        ndiff = -ndiff
    return ns0, ns1, ndiff

def SixGodCooking(n, w, side, s0, s1, i, j):
    wi = w[i]
    wj = w[j]
    ns0 = s0
    ns1 = s1
    if side[i] == 0:
        ns0 = ns0 - wi
        ns1 = ns1 + wi
    else:
        ns0 = ns0 + wi
        ns1 = ns1 - wi
    if side[j] == 0:
        ns0 = ns0 - wj
        ns1 = ns1 + wj
    else:
        ns0 = ns0 + wj
        ns1 = ns1 - wj
    ndiff = ns0 - ns1
    if ndiff < 0:
        ndiff = -ndiff
    return ns0, ns1, ndiff

def exact_min_diff(weights):
    total = 0
    i = 0
    n = len(weights)
    while i < n:
        total += weights[i]
        i += 1
    dp = 1
    i = 0
    while i < n:
        dp |= dp << weights[i]
        i += 1
    half = total // 2
    s = half
    while s >= 0:
        if (dp >> s) & 1:
            return total - 2 * s
        s -= 1
    return total

def ChampagnePapi21(n, weights):
    pairs = []
    i = 0
    while i < n:
        pairs.append((weights[i], i))
        i = i + 1

    pairs.sort(reverse=True)

    side = [0] * n
    s0 = 0
    s1 = 0
    k = 0
    while k < n:
        w, idx = pairs[k]
        if s0 <= s1:
            side[idx] = 0
            s0 = s0 + w
        else:
            side[idx] = 1
            s1 = s1 + w
        k = k + 1

    diff = s0 - s1
    if diff < 0:
        diff = -diff

    best_side = side[:]
    best_diff = diff
    best_s0 = s0
    best_s1 = s1

    tot = 0
    i = 0
    while i < n:
        tot = tot + weights[i]
        i = i + 1

    seed_val = int(time.time() * 1000003) & 0xFFFFFFFF
    random.seed(seed_val)

    T = float(tot) if tot > 0 else 1.0
    Tend = 1e-4
    alpha = 0.995

    start = time.perf_counter()
    time_limit = 0.2

    inner = 100 + 30 * n

    while T > Tend:
        c = 0
        while c < inner:
            if n >= 2 and random.random() < 0.35:
                i1 = random.randrange(n)
                i2 = random.randrange(n)
                while i2 == i1:
                    i2 = random.randrange(n)
                ns0, ns1, nd = SixGodCooking(n, weights, side, s0, s1, i1, i2)
                delta = nd - diff
                accept = False
                if delta <= 0:
                    accept = True
                else:
                    p = math.exp(-float(delta) / T)
                    if random.random() < p:
                        accept = True
                if accept:
                    if side[i1] == 0:
                        side[i1] = 1
                    else:
                        side[i1] = 0
                    if side[i2] == 0:
                        side[i2] = 1
                    else:
                        side[i2] = 0
                    s0 = ns0
                    s1 = ns1
                    diff = nd
                    if diff < best_diff:
                        best_diff = diff
                        best_side = side[:]
                        best_s0 = s0
                        best_s1 = s1
            else:
                idx = random.randrange(n)
                ns0, ns1, nd = longliveDrizzy(n, weights, side, s0, s1, idx)
                delta = nd - diff
                accept = False
                if delta <= 0:
                    accept = True
                else:
                    p = math.exp(-float(delta) / T)
                    if random.random() < p:
                        accept = True
                if accept:
                    if side[idx] == 0:
                        side[idx] = 1
                    else:
                        side[idx] = 0
                    s0 = ns0
                    s1 = ns1
                    diff = nd
                    if diff < best_diff:
                        best_diff = diff
                        best_side = side[:]
                        best_s0 = s0
                        best_s1 = s1
            c = c + 1

        T = T * alpha
        now = time.perf_counter()
        if now - start > time_limit:
            break

    side = best_side[:]
    s0 = best_s0
    s1 = best_s1
    diff = best_diff

    improved = True
    while improved:
        improved = False
        i = 0
        while i < n:
            ns0, ns1, nd = longliveDrizzy(n, weights, side, s0, s1, i)
            if nd < diff:
                if side[i] == 0:
                    side[i] = 1
                else:
                    side[i] = 0
                s0 = ns0
                s1 = ns1
                diff = nd
                improved = True
            i = i + 1

    sa_result = diff
    exact = exact_min_diff(weights)
    if exact < sa_result:
        return exact
    return sa_result

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    ans = ChampagnePapi21(n, arr)
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()

''' .2 ' Рюкзак [АиСД] + ''' #mid

def ChampagnePapi21(s, weights):
    dp = []
    i = 0
    while i <= s:
        dp.append(False)
        i = i + 1

    dp[0] = True

    i = 0
    while i < len(weights):
        w = weights[i]
        cap = s
        while cap >= w:
            if dp[cap - w]:
                dp[cap] = True
            cap = cap - 1
        i = i + 1

    ans = s
    while ans >= 0:
        if dp[ans]:
            ret = ans
            return ret
        ans = ans - 1

    ret = 0
    return ret

def solve():
    first = input().strip().split()
    s = int(first[0])
    n = int(first[1])

    vals = []
    while len(vals) < n:
        parts = input().strip().split()
        j = 0
        while j < len(parts):
            vals.append(int(parts[j]))
            j = j + 1

    ans = ChampagnePapi21(s, vals)
    print(ans)

if __name__ == '__main__':
    solve()

''' .3 ' Распредели призы + ''' #hard

def ChampagnePapi21(n, k):
    if n % k != 0:
        return None

    m = n // k

    if n == k:
        if n == 1:
            groups = [[]]
            groups[0].append(1)
            return groups
        else:
            return None

    total_sum = n * (n + 1) // 2
    if total_sum % k != 0:
        return None

    groups = []
    i = 0
    while i < k:
        groups.append([])
        i = i + 1

    if m % 2 == 0:
        rows_count = m
        base = 1

        row = 0
        while row < rows_count:
            row_start = base + row * k
            if row % 2 == 0:
                col = 0
                while col < k:
                    value = row_start + col
                    groups[col].append(value)
                    col = col + 1
            else:
                row_end = row_start + k - 1
                col = 0
                while col < k:
                    value = row_end - col
                    groups[col].append(value)
                    col = col + 1
            row = row + 1
    else:
        kk = k
        temp = 3 * kk + 1
        triple_sum = 3 * temp // 2
        half = (kk + 1) // 2
        h = (kk - 1) // 2

        j = 1
        while j <= kk:
            if j <= half:
                a = j
                c3 = 3 * kk - 2 * (j - 1)
                b = triple_sum - a - c3
            else:
                a = j
                b = j + h
                c3 = 4 * kk - 2 * (j - 1)

            idx = j - 1
            groups[idx].append(a)
            groups[idx].append(b)
            groups[idx].append(c3)

            j = j + 1

        base = 3 * kk + 1
        rows_count = m - 3

        row = 0
        while row < rows_count:
            row_start = base + row * kk
            if row % 2 == 0:
                col = 0
                while col < kk:
                    value = row_start + col
                    groups[col].append(value)
                    col = col + 1
            else:
                row_end = row_start + kk - 1
                col = 0
                while col < kk:
                    value = row_end - col
                    groups[col].append(value)
                    col = col + 1
            row = row + 1

    return groups

def solve():
    parts = input().split()
    while len(parts) < 2:
        extra = input().split()
        parts = parts + extra

    n = int(parts[0])
    k = int(parts[1])

    groups = ChampagnePapi21(n, k)

    if groups is None:
        print(0)
    else:
        i = 0
        while i < k:
            g = groups[i]
            line_parts = []
            j = 0
            length = len(g)
            while j < length:
                line_parts.append(str(g[j]))
                j = j + 1
            print(" ".join(line_parts))
            i = i + 1

if __name__ == '__main__':
    solve()

''' .4 ' Разносчик пиццы + ''' #very hard

# #include <bits/stdc++.h>
# using namespace std;
#
# struct Answer {
#     int m;
#     vector<vector<int>> groups;
# };
#
# Answer ChampagnePapi21(int n, long long s, const vector<long long>& w) {
#     int size = 1 << n;
#     vector<int> rides(size, n + 1);
#     vector<long long> last(size, 0);
#     vector<int> parent(size, -1);
#     vector<int> parent_add(size, -1);
#     vector<char> parent_new(size, 0);
#
#     rides[0] = 1;
#     last[0] = 0;
#
#     for (int mask = 0; mask < size; mask = mask + 1) {
#         int r = rides[mask];
#         long long l = last[mask];
#         if (r > n) continue;
#         for (int j = 0; j < n; j = j + 1) {
#             if (mask & (1 << j)) continue;
#             int nm = mask | (1 << j);
#             int nr = r;
#             long long nl = l + w[j];
#             char started = 0;
#             if (nl > s) {
#                 nr = r + 1;
#                 nl = w[j];
#                 started = 1;
#             }
#             if (nr < rides[nm] || (nr == rides[nm] && nl < last[nm])) {
#                 rides[nm] = nr;
#                 last[nm] = nl;
#                 parent[nm] = mask;
#                 parent_add[nm] = j;
#                 parent_new[nm] = started;
#             }
#         }
#     }
#
#     int full = size - 1;
#     int m = rides[full];
#
#     vector<vector<int>> groups;
#     vector<int> cur;
#     int x = full;
#     while (x != 0) {
#         int j = parent_add[x];
#         cur.push_back(j + 1);
#         if (parent_new[x]) {
#             groups.push_back(cur);
#             cur.clear();
#         }
#         x = parent[x];
#     }
#     if (!cur.empty()) groups.push_back(cur);
#     reverse(groups.begin(), groups.end());
#     for (auto& g : groups) reverse(g.begin(), g.end());
#
#     return {m, groups};
# }
#
# void solve() {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#
#     int t;
#     if (!(cin >> t)) return;
#     for (int cs = 0; cs < t; cs = cs + 1) {
#         int n;
#         long long s;
#         cin >> n >> s;
#         vector<long long> w(n);
#         for (int i = 0; i < n; i = i + 1) cin >> w[i];
#
#         auto ans = ChampagnePapi21(n, s, w);
#         cout << ans.m << '\n';
#         for (const auto& g : ans.groups) {
#             cout << g.size();
#             for (int id : g) cout << ' ' << id;
#             cout << '\n';
#         }
#     }
# }
#
# int main() {
#     solve();
#     return 0;
# }

# TL80 on .py

from array import array

def ChampagnePapi21(n, s, w):
    size = 1 << n

    rides = array('i', [n + 1] * size)
    last = array('l', [0] * size)
    parent = array('i', [-1] * size)
    parent_add = array('i', [-1] * size)
    parent_new = array('b', [0] * size)

    rides[0] = 1
    last[0] = 0

    mask = 0
    while mask < size:
        r = rides[mask]
        l = last[mask]
        if r <= n:
            j = 0
            while j < n:
                bit = 1 << j
                if (mask & bit) == 0:
                    nm = mask | bit
                    nr = r
                    nl = l + w[j]
                    started = 0
                    if nl > s:
                        nr = r + 1
                        nl = w[j]
                        started = 1
                    better = False
                    if nr < rides[nm]:
                        better = True
                    elif nr == rides[nm] and nl < last[nm]:
                        better = True
                    if better:
                        rides[nm] = nr
                        last[nm] = nl
                        parent[nm] = mask
                        parent_add[nm] = j
                        parent_new[nm] = started
                j = j + 1
        mask = mask + 1

    full = size - 1
    m = rides[full]

    groups = []
    cur = []
    x = full
    while x != 0:
        j = parent_add[x]
        cur.append(j + 1)
        if parent_new[x] == 1:
            groups.append(cur)
            cur = []
        x = parent[x]
    if cur:
        groups.append(cur)

    groups.reverse()
    i = 0
    while i < len(groups):
        groups[i].reverse()
        i = i + 1

    return m, groups

def solve():
    ts = input().strip()
    t = int(ts)

    case_id = 0
    while case_id < t:
        p = input().strip().split()
        while len(p) < 2:
            add = input().strip().split()
            k = 0
            while k < len(add):
                p.append(add[k])
                k = k + 1
        n = int(p[0])
        s = int(p[1])

        w = []
        while len(w) < n:
            row = input().strip().split()
            j = 0
            while j < len(row):
                w.append(int(row[j]))
                j = j + 1

        m, groups = ChampagnePapi21(n, s, w)
        print(m)
        i = 0
        while i < len(groups):
            g = groups[i]
            out = [str(len(g))]
            j = 0
            while j < len(g):
                out.append(str(g[j]))
                j = j + 1
            print(' '.join(out))
            i = i + 1

        case_id = case_id + 1

if __name__ == '__main__':
    solve()

''' .5 ' Хорошие раскраски + ''' #impossible

# #include <bits/stdc++.h>
# using namespace std;
#
# int n_, m_, c_;
# const int MAXBITS = 270;
#
# struct Pat {
#     vector<int> col;
#     bitset<MAXBITS> bits;
#     int pop;
# };
#
# vector<Pat> pats;
# bitset<MAXBITS> usedBits;
# vector<int> pick;
#
# int pair_idx(int a, int b) {
#     if (a > b) swap(a, b);
#     return a * n_ + b;
# }
#
# int cons_idx(int a, int b, int k) {
#     return pair_idx(a, b) * c_ + (k - 1);
# }
#
# void gen_patterns_rec(int i, vector<int>& cur) {
#     if (i == n_) {
#         Pat p;
#         p.col = cur;
#         p.bits.reset();
#         for (int color = 1; color <= c_; ++color) {
#             int r1 = 0;
#             while (r1 < n_) {
#                 if (cur[r1] == color) {
#                     int r2 = r1 + 1;
#                     while (r2 < n_) {
#                         if (cur[r2] == color) {
#                             int id = cons_idx(r1, r2, color);
#                             p.bits.set(id);
#                         }
#                         ++r2;
#                     }
#                 }
#                 ++r1;
#             }
#         }
#         p.pop = (int)p.bits.count();
#         pats.push_back(move(p));
#         return;
#     }
#     for (int k = 1; k <= c_; ++k) {
#         cur[i] = k;
#         gen_patterns_rec(i + 1, cur);
#     }
# }
#
# bool dfs(int col) {
#     if (col == m_) return true;
#     static vector<int> order;
#     order.clear();
#     for (int i = 0; i < (int)pats.size(); ++i) {
#         if (!(usedBits & pats[i].bits).any())
#             order.push_back(i);
#     }
#     sort(order.begin(), order.end(), [&](int a, int b) {
#         if (pats[a].pop != pats[b].pop) return pats[a].pop < pats[b].pop;
#         return a < b;
#     });
#     for (int id : order) {
#         usedBits |= pats[id].bits;
#         pick[col] = id;
#         if (dfs(col + 1)) return true;
#         usedBits ^= pats[id].bits;
#     }
#     return false;
# }
#
# int main() {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#
#     if (!(cin >> n_ >> m_ >> c_)) return 0;
#
#     if (c_ == 1) {
#         if (n_ > 1 && m_ > 1) {
#             cout << -1 << '\n';
#             return 0;
#         }
#         for (int i = 0; i < n_; ++i) {
#             for (int j = 0; j < m_; ++j) {
#                 if (j) cout << ' ';
#                 cout << 1;
#             }
#             cout << '\n';
#         }
#         return 0;
#     }
#
#     if (c_ == 3 && n_ <= 10 && m_ <= 10) {
#         int base[10][10] = {
#             {1,1,1,1,2,2,3,3,2,3},
#             {1,2,2,3,1,1,1,3,3,2},
#             {3,1,2,3,1,2,2,1,1,3},
#             {3,2,1,2,2,1,3,1,3,1},
#             {1,2,3,3,3,2,3,2,1,1},
#             {3,1,2,2,3,3,1,2,2,1},
#             {2,3,1,2,3,2,1,3,1,2},
#             {2,2,3,1,1,3,2,3,2,1},
#             {3,3,3,1,2,1,2,2,1,2},
#             {2,3,2,1,2,3,1,1,3,3}
#         };
#         for (int i = 0; i < n_; ++i) {
#             for (int j = 0; j < m_; ++j) {
#                 if (j) cout << ' ';
#                 cout << base[i][j];
#             }
#             cout << '\n';
#         }
#         return 0;
#     }
#
#     vector<int> cur(n_, 1);
#     pats.clear();
#     gen_patterns_rec(0, cur);
#     sort(pats.begin(), pats.end(), [&](const Pat& a, const Pat& b) {
#         if (a.pop != b.pop) return a.pop < b.pop;
#         return a.col < b.col;
#     });
#
#     usedBits.reset();
#     pick.assign(m_, -1);
#     bool ok = dfs(0);
#     if (!ok) {
#         cout << -1 << '\n';
#         return 0;
#     }
#
#     vector<vector<int>> grid(n_, vector<int>(m_, 0));
#     for (int j = 0; j < m_; ++j) {
#         const Pat& p = pats[pick[j]];
#         for (int i = 0; i < n_; ++i) grid[i][j] = p.col[i];
#     }
#
#     for (int i = 0; i < n_; ++i) {
#         for (int j = 0; j < m_; ++j) {
#             if (j) cout << ' ';
#             cout << grid[i][j];
#         }
#         cout << '\n';
#     }
#     return 0;
# }

# TL4 on .py

def longliveDrizzy(n, m, c, g, i, j, k):
    r = 0
    while r < i:
        if g[r][j] == k:
            cc = 0
            while cc < j:
                if g[i][cc] == k and g[r][cc] == k:
                    return False
                cc = cc + 1
        r = r + 1
    return True

def SixGodCooking(n, m, c, g):
    best_cnt = c + 1
    bi = -1
    bj = -1
    opts = []

    i = 0
    while i < n:
        j = 0
        while j < m:
            if g[i][j] == 0:
                cur = []
                k = 1
                while k <= c:
                    if longliveDrizzy(n, m, c, g, i, j, k):
                        cur.append(k)
                    k = k + 1
                cnt = len(cur)
                if cnt == 0:
                    return (-1, -1, [])
                if cnt < best_cnt:
                    best_cnt = cnt
                    bi = i
                    bj = j
                    opts = cur
                    if best_cnt == 1:
                        return (bi, bj, opts)
            j = j + 1
        i = i + 1

    return (bi, bj, opts)

def ChampagnePapi21(n, m, c):
    g = []
    i = 0
    while i < n:
        g.append([0] * m)
        i = i + 1

    j = 0
    while j < m:
        g[0][j] = (j % c) + 1
        j = j + 1

    def dfs(filled):
        if filled == n * m:
            return True

        ii, jj, opts = SixGodCooking(n, m, c, g)
        if ii == -1:
            return False

        t = len(opts) - 1
        while t >= 0:
            k = opts[t]
            g[ii][jj] = k
            if dfs(filled + 1):
                return True
            g[ii][jj] = 0
            t = t + -1

        return False

    dfs(m)
    return g

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])
    c = int(parts[2])

    g = ChampagnePapi21(n, m, c)

    i = 0
    while i < n:
        line = []
        j = 0
        while j < m:
            v = g[i][j]
            if v == 0:
                v = 1
            line.append(str(v))
            j = j + 1
        print(' '.join(line))
        i = i + 1

if __name__ == '__main__':
    solve()