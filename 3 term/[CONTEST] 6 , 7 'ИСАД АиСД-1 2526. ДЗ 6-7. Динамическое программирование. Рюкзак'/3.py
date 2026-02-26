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
