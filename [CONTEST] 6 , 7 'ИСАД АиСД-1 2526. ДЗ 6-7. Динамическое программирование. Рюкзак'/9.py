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
