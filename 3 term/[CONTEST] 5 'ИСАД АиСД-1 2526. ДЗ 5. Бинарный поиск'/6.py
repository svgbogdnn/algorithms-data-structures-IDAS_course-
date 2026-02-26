''' .6 ' Вырубка леса +''' #easy

def ChampagnePapi21(a, k, b, m, d):
    x1 = d // k
    x2 = d // m
    w1 = d - x1
    w2 = d - x2
    cut1 = a * w1
    cut2 = b * w2
    total = cut1 + cut2
    return total

def longliveDrizzy(a, k, b, m, x):
    left = 0
    right = 1
    while ChampagnePapi21(a, k, b, m, right) < x:
        right = right * 2

    while left < right:
        mid = (left + right) // 2
        got = ChampagnePapi21(a, k, b, m, mid)
        if got >= x:
            right = mid
        else:
            left = mid + 1

    return left

def solve():
    parts = input().strip().split()
    a = int(parts[0])
    k = int(parts[1])
    b = int(parts[2])
    m = int(parts[3])
    x = int(parts[4])
    ans = longliveDrizzy(a, k, b, m, x)
    print(ans)

if __name__ == '__main__':
    solve()
