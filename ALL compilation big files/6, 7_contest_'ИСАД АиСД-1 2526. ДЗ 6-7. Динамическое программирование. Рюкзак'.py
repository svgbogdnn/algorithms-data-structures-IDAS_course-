'''
https://official.contest.yandex.ru/contest/83287/problems/
start 31.10.2025 - finish 20.11.2025 , 15 tasks , 15/15
905 lines
'''

''' .1 ' Последняя цифра числа Фибоначчи + ''' #easy

def ChampagnePapi21(n):
    if n <= 1:
        return 1

    a = 1
    b = 1
    i = 2

    while i <= n:
        c = a + b
        c = c % 10
        a = b
        b = c
        i = i + 1

    return b

def solve():
    s = input().strip()
    n = int(s)
    print(ChampagnePapi21(n))

if __name__ == '__main__':
    solve()

''' .2 ' Простая последовательность + '''  #light mid

def ChampagnePapi21(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    a = [0] * (n + 1)
    a[0] = 1
    a[1] = 1

    i = 2
    while i <= n:
        if i % 2 == 0:
            k = i // 2
            a[i] = a[k] + a[k - 1]
        else:
            k = i // 2
            a[i] = a[k] - a[k - 1]
        i = i + 1

    ret = a[n]
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()

''' .3 ' Мячик на лесенке + ''' #light mid

def ChampagnePapi21(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    i = 3
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        i = i + 1

    ret = dp[n]
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()

''' .4 ' Черепашка + ''' #slightly hard

def ChampagnePapi21(n, m, grid):
    dp = []
    i = 0
    while i < n:
        dp.append([0] * m)
        i = i + 1

    dp[0][0] = grid[0][0]

    j = 1
    while j < m:
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        j = j + 1

    i = 1
    while i < n:
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        i = i + 1

    i = 1
    while i < n:
        j = 1
        while j < m:
            up = dp[i - 1][j]
            left = dp[i][j - 1]
            best_prev = up if up >= left else left
            dp[i][j] = best_prev + grid[i][j]
            j = j + 1
        i = i + 1

    ret = dp[n - 1][m - 1]
    return ret

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])

    grid = []
    i = 0
    while i < n:
        row_vals = input().strip().split()
        row = []
        k = 0
        while k < m:
            row.append(int(row_vals[k]))
            k = k + 1
        grid.append(row)
        i = i + 1

    ans = ChampagnePapi21(n, m, grid)
    print(ans)

if __name__ == '__main__':
    solve()

''' .5 ' Треугольник Паскаля + ''' #slightly hard

def ChampagnePapi21(n):
    if n == 0:
        return []

    rows = []
    prev = [1]
    rows.append(prev)

    r = 2
    while r <= n:
        cur = []
        j = 0
        while j < r:
            if j == 0 or j == r - 1:
                val = 1
            else:
                val = prev[j - 1] + prev[j]
            cur.append(val)
            j = j + 1
        rows.append(cur)
        prev = cur
        r = r + 1

    ret = rows
    return ret

def solve():
    s = input().strip()
    n = int(s)
    rows = ChampagnePapi21(n)

    i = 0
    while i < len(rows):
        row = rows[i]
        parts = []
        j = 0
        while j < len(row):
            parts.append(str(row[j]))
            j = j + 1
        print(' '.join(parts))
        i = i + 1

if __name__ == '__main__':
    solve()

''' .6 ' Платная лестница + ''' #mid

def ChampagnePapi21(n, costs):
    arr = [0]
    i = 0
    while i < n:
        arr.append(costs[i])
        i = i + 1

    dp = [0] * (n + 1)
    if n >= 1:
        dp[1] = arr[1]

    i = 2
    while i <= n:
        a = dp[i - 1]
        b = dp[i - 2]
        best = a if a <= b else b
        dp[i] = arr[i] + best
        i = i + 1

    ret = dp[n]
    return ret

def solve():
    s = input().strip()
    n = int(s)

    nums = []
    while len(nums) < n:
        parts = input().strip().split()
        j = 0
        while j < len(parts):
            nums.append(int(parts[j]))
            j = j + 1

    ans = ChampagnePapi21(n, nums)
    print(ans)

if __name__ == '__main__':
    solve()

''' .7 ' Гвоздики + ''' #slightly hard

def ChampagnePapi21(n, coords):
    a = []
    i = 0
    while i < n:
        a.append(coords[i])
        i = i + 1

    a.sort()

    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = a[1] - a[0]

    if n >= 3:
        dp[3] = a[2] - a[0]
    if n >= 4:
        dp[4] = dp[2] + (a[3] - a[2])

    k = 5
    while k <= n:
        v1 = dp[k - 2] + (a[k - 1] - a[k - 2])
        v2 = dp[k - 3] + (a[k - 1] - a[k - 3])
        best = v1 if v1 <= v2 else v2
        dp[k] = best
        k = k + 1

    ret = dp[n]
    return ret

def solve():
    s = input().strip()
    n = int(s)

    nums = []
    while len(nums) < n:
        parts = input().strip().split()
        j = 0
        while j < len(parts):
            nums.append(int(parts[j]))
            j = j + 1

    ans = ChampagnePapi21(n, nums)
    print(ans)

if __name__ == '__main__':
    solve()

''' .8 ' Взрывоопасность + ''' #over easy

def ChampagnePapi21(n):
    if n == 0:
        return 1
    if n == 1:
        return 3

    f0 = 1
    f1 = 3
    i = 2

    while i <= n:
        f2 = 2 * f1 + 2 * f0
        f0 = f1
        f1 = f2
        i = i + 1

    ret = f1
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()

''' .9 ' Калькулятор + ''' #hard

def ChampagnePapi21(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    if n >= 1:
        dp[1] = 0
        prev[1] = 0

    i = 2
    while i <= n:
        best = dp[i - 1] + 1
        parent = i - 1

        if i % 2 == 0:
            cand = dp[i // 2] + 1
            if cand < best:
                best = cand
                parent = i // 2

        if i % 3 == 0:
            cand = dp[i // 3] + 1
            if cand < best:
                best = cand
                parent = i // 3

        dp[i] = best
        prev[i] = parent
        i = i + 1

    ret = (dp, prev)
    return ret

def longliveDrizzy(n, prev):
    path = []
    x = n
    while x >= 1:
        path.append(x)
        if x == 1:
            break
        x = prev[x]

    path.reverse()
    ret = path
    return ret

def solve():
    s = input().strip()
    n = int(s)

    dp, prev = ChampagnePapi21(n)
    print(dp[n])

    path = longliveDrizzy(n, prev)
    parts = []
    i = 0
    while i < len(path):
        parts.append(str(path[i]))
        i = i + 1
    print(' '.join(parts))

if __name__ == '__main__':
    solve()

''' .10 ' Банкомат + ''' #reinforced hard

def SixGodCooking(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    ret = a
    return ret

def longliveDrizzy(vals):
    if len(vals) == 0:
        return 0
    g = vals[0]
    i = 1
    while i < len(vals):
        g = SixGodCooking(g, vals[i])
        i = i + 1
    ret = g
    return ret

def ChampagnePapi21(n, coins, s):
    use = []
    i = 0
    while i < n:
        v = coins[i]
        if v <= s:
            use.append(v)
        i = i + 1

    if len(use) == 0:
        return (-1, [])

    use = sorted(set(use))

    g = longliveDrizzy(use)
    if s % g != 0:
        return (-1, [])

    dp = [s + 1] * (s + 1)
    par = [-1] * (s + 1)
    dp[0] = 0

    j = 0
    while j < len(use):
        c = use[j]
        a = c
        while a <= s:
            prev = dp[a - c] + 1
            if prev < dp[a]:
                dp[a] = prev
                par[a] = c
            a = a + 1
        j = j + 1

    if dp[s] == s + 1:
        return (-1, [])

    path = []
    x = s
    while x > 0:
        c = par[x]
        path.append(c)
        x = x - c

    ret_cnt = dp[s]
    ret_list = path
    return (ret_cnt, ret_list)

def solve():
    s1 = input().strip()
    n = int(s1)

    vals = []
    while len(vals) < n:
        parts = input().strip().split()
        k = 0
        while k < len(parts):
            vals.append(int(parts[k]))
            k = k + 1

    s2 = input().strip()
    target = int(s2)

    cnt, lst = ChampagnePapi21(n, vals, target)
    if cnt == -1:
        print(-1)
        return

    print(cnt)
    out = []
    i = 0
    while i < len(lst):
        out.append(str(lst[i]))
        i = i + 1
    print(' '.join(out))

if __name__ == '__main__':
    solve()

''' .11 ' Рюкзак + ''' #mid

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

''' .12 ' Шашку - в дамки + ''' #mid

def ChampagnePapi21(x, y):
    size = 8

    dp = []
    i = 0
    while i <= size:
        row = []
        j = 0
        while j <= size:
            row.append(0)
            j = j + 1
        dp.append(row)
        i = i + 1

    c = 1
    while c <= size:
        dp[size][c] = 1
        c = c + 1

    r = size - 1
    while r >= 1:
        c = 1
        while c <= size:
            left = 0
            right = 0
            if c - 1 >= 1:
                left = dp[r + 1][c - 1]
            if c + 1 <= size:
                right = dp[r + 1][c + 1]
            dp[r][c] = left + right
            c = c + 1
        r = r - 1

    ret = dp[y][x]
    return ret

def solve():
    parts = input().strip().split()
    x = int(parts[0])
    y = int(parts[1])
    ans = ChampagnePapi21(x, y)
    print(ans)

if __name__ == '__main__':
    solve()

''' .13 ' Рюкзак с ценой предметов + ''' #mid

def ChampagnePapi21(n, m, weights, values):
    dp = []
    w = 0
    while w <= m:
        dp.append(0)
        w = w + 1

    i = 0
    while i < n:
        wi = weights[i]
        vi = values[i]
        cap = m
        while cap >= wi:
            cand = dp[cap - wi] + vi
            if cand > dp[cap]:
                dp[cap] = cand
            cap = cap - 1
        i = i + 1

    ret = dp[m]
    return ret

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])

    weights = []
    while len(weights) < n:
        row = input().strip().split()
        j = 0
        while j < len(row):
            weights.append(int(row[j]))
            j = j + 1

    values = []
    while len(values) < n:
        row = input().strip().split()
        j = 0
        while j < len(row):
            values.append(int(row[j]))
            j = j + 1

    ans = ChampagnePapi21(n, m, weights, values)
    print(ans)

if __name__ == '__main__':
    solve()

''' .14 ' Наибольшая общая возрастающая подпоследовательность + ''' #mid

# #include <bits/stdc++.h>
# using namespace std;
#
# int ChampagnePapi21(int n, int m,
#                     const vector<long long>& a,
#                     const vector<long long>& b) {
#     vector<int> dp(m, 0);
#     for (int i = 0; i < n; i = i + 1) {
#         int best = 0;
#         for (int j = 0; j < m; j = j + 1) {
#             if (a[i] == b[j]) {
#                 int cand = best + 1;
#                 if (cand > dp[j]) dp[j] = cand;
#             } else if (b[j] < a[i]) {
#                 if (dp[j] > best) best = dp[j];
#             }
#         }
#     }
#     int ans = 0;
#     for (int j = 0; j < m; j = j + 1) {
#         if (dp[j] > ans) ans = dp[j];
#     }
#     return ans;
# }
#
# void solve() {
#     ios::sync_with_stdio(false);
#     cin.tie(nullptr);
#
#     int n, m;
#     if (!(cin >> n >> m)) return;
#
#     vector<long long> a;
#     a.reserve(n);
#     for (int i = 0; i < n; i = i + 1) {
#         long long x;
#         cin >> x;
#         a.push_back(x);
#     }
#
#     vector<long long> b;
#     b.reserve(m);
#     for (int j = 0; j < m; j = j + 1) {
#         long long x;
#         cin >> x;
#         b.push_back(x);
#     }
#
#     cout << ChampagnePapi21(n, m, a, b) << '\n';
# }
#
# int main() {
#     solve();
#     return 0;
# }

#TL 38 on .py

def ChampagnePapi21(n, m, a, b):
    dp = []
    j = 0
    while j < m:
        dp.append(0)
        j = j + 1

    i = 0
    while i < n:
        best = 0
        j = 0
        while j < m:
            if a[i] == b[j]:
                cand = best + 1
                if cand > dp[j]:
                    dp[j] = cand
            elif b[j] < a[i]:
                if dp[j] > best:
                    best = dp[j]
            j = j + 1
        i = i + 1

    ans = 0
    k = 0
    while k < m:
        if dp[k] > ans:
            ans = dp[k]
        k = k + 1

    ret = ans
    return ret

def solve():
    first = input().strip().split()
    n = int(first[0])
    m = int(first[1])

    a = []
    while len(a) < n:
        parts = input().strip().split()
        i = 0
        while i < len(parts):
            a.append(int(parts[i]))
            i = i + 1

    b = []
    while len(b) < m:
        parts = input().strip().split()
        i = 0
        while i < len(parts):
            b.append(int(parts[i]))
            i = i + 1

    ans = ChampagnePapi21(n, m, a, b)
    print(ans)

if __name__ == '__main__':
    solve()

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