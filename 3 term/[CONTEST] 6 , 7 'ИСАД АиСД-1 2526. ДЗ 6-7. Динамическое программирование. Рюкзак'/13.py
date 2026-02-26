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
