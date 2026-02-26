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
