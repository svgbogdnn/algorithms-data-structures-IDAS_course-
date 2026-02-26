''' .15 ' Интересное число + ''' #over mid

# #include <bits/stdc++.h>
# using namespace std;
#
# string ChampagnePapi21(int n) {
#     const int size = (n + 1) * n;
#
#     vector<unsigned char> used(size, 0);
#     vector<int> parent(size, -1);
#     vector<signed char> digit(size, -1);
#     deque<int> q;
#
#     int d = 1;
#     while (d <= 9 && d <= n) {
#         int r = d % n;
#         int idx = d * n + r;
#         if (used[idx] == 0) {
#             used[idx] = 1;
#             parent[idx] = -1;
#             digit[idx] = (signed char)d;
#             q.push_back(idx);
#         }
#         d = d + 1;
#     }
#
#     int target = -1;
#
#     while (!q.empty()) {
#         int cur = q.front();
#         q.pop_front();
#
#         int s = cur / n;
#         int r = cur - s * n;
#
#         if (s == n && r == 0) {
#             target = cur;
#             break;
#         }
#
#         int nd = 0;
#         while (nd <= 9) {
#             int ns = s + nd;
#             if (ns > n) break;
#             int nr = (r * 10 + nd) % n;
#             int ni = ns * n + nr;
#             if (used[ni] == 0) {
#                 used[ni] = 1;
#                 parent[ni] = cur;
#                 digit[ni] = (signed char)nd;
#                 q.push_back(ni);
#             }
#             nd = nd + 1;
#         }
#     }
#
#     if (target == -1) return string("0");
#
#     string res;
#     int x = target;
#     while (x != -1) {
#         res.push_back(char('0' + digit[x]));
#         x = parent[x];
#     }
#     reverse(res.begin(), res.end());
#     return res;
# }
#
# void solve() {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#
#     int n;
#     if (!(cin >> n)) return;
#     cout << ChampagnePapi21(n) << '\n';
# }
#
# int main() {
#     solve();
#     return 0;
# }

#TL 19 on .py

from collections import deque
from array import array

def ChampagnePapi21(n):
    size = (n + 1) * n
    used = bytearray(size)
    parent = array('i', [-1] * size)
    digit = array('b', [-1] * size)
    q = deque()

    d = 1
    while d <= 9 and d <= n:
        r = d % n
        idx = d * n + r
        if used[idx] == 0:
            used[idx] = 1
            parent[idx] = -1
            digit[idx] = d
            q.append(idx)
        d = d + 1

    target = -1

    while q:
        cur = q.popleft()
        s = cur // n
        r = cur - s * n
        if s == n and r == 0:
            target = cur
            break
        nd = 0
        while nd <= 9:
            ns = s + nd
            if ns > n:
                break
            nr = (r * 10 + nd) % n
            ni = ns * n + nr
            if used[ni] == 0:
                used[ni] = 1
                parent[ni] = cur
                digit[ni] = nd
                q.append(ni)
            nd = nd + 1

    if target == -1:
        return "0"

    digs = []
    x = target
    while x != -1:
        digs.append(str(digit[x]))
        x = parent[x]
    digs.reverse()

    ret = ''.join(digs)
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()
