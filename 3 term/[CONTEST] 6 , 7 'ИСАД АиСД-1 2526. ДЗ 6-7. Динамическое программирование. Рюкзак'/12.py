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
