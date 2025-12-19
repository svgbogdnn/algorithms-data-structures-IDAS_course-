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
