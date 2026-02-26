''' .12 Быстрое возведение в степень + '''

def longlive21(a, n):
    if n == 0:
        return 1

    neg = n < 0
    if neg: e = -n
    else: e = n
    res = 1
    x = a

    while e > 0:
        if (e % 2) == 1:
            res *= x
        x = x * x
        e = e // 2

    if neg:
        return 1 / res

    return res

def solve():
    a = float(input().strip())
    n = int(input().strip())
    print(longlive21(a, n))
if __name__ == '__main__':
    solve()
