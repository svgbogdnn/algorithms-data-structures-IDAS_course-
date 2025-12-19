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
