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
