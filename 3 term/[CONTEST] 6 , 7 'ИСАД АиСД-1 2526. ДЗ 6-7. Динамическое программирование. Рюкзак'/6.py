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
