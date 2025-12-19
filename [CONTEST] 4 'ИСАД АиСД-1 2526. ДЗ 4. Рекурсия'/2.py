''' .2 ' Быстрое возведение в степень + ''' #very easy

def ChampagnePapi21(a, n):
    if n == 0:
        return 1.0
    if n < 0:
        val = ChampagnePapi21(a, -n)
        res = 1.0 / val
        return res
    half = ChampagnePapi21(a, n // 2)
    sq = half * half
    if n % 2 == 0:
        return sq
    mul = a * sq
    return mul

def solve():
    parts = input().strip().split()
    if len(parts) == 1:
        a = float(parts[0])
        s = input().strip()
        n = int(s)
    else:
        a = float(parts[0])
        n = int(parts[1])
    ans = ChampagnePapi21(a, n)
    text = '{:.15g}'.format(ans)
    print(text)

if __name__ == '__main__':
    solve()
