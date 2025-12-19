''' .3 ' N в степени N + ''' #easy

def ChampagnePapi21(a, n, m):
    if m == 1:
        return 0
    a = a % m
    res = 1 % m
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        n = n // 2
    return res

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])
    ans = ChampagnePapi21(n, n, m)
    print(ans)

if __name__ == '__main__':
    solve()
