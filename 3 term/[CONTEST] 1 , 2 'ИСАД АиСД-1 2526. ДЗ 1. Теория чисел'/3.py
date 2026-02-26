''' .3 Сильно составные числа + '''

def longlive21(n: int):
    cnt = [0] * (n + 1)
    p = 2

    while p <= n:
        if cnt[p] == 0:
            m = p
            while m <= n:
                cnt[m] += 1
                m += p
        p += 1

    res = []
    x = 2

    while x <= n:
        if cnt[x] >= 3:
            res.append(x)
        x += 1

    return res

def solve():
    s = input().strip()
    n = int(s)
    ans = longlive21(n)
    if ans:
        print(' '.join(str(v) for v in ans))
    else:
        print()

if __name__ == '__main__':
    solve()
