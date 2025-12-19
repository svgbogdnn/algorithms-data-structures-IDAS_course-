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
