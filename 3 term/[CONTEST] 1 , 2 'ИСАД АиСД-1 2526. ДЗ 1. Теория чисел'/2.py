''' .2 Факторизация числа + '''

def longlive21(n: int):
    res = []
    if n <= 1:
        return res

    while n % 2 == 0:
        res.append(2)
        n = n // 2
    i = 3

    while i * i <= n:
        while n % i == 0:
            res.append(i)
            n //= i
        i += 2

    if n > 1:
        res.append(n)
    return res

def solve():
    s = input().strip()
    n = int(s)
    f = longlive21(n)
    if len(f) > 0:
        print(' '.join(str(x) for x in f))
    else:
        print()

if __name__ == '__main__':
    solve()
