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
