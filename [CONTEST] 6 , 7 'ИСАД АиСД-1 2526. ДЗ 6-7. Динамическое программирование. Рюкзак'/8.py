''' .8 ' Взрывоопасность + ''' #over easy

def ChampagnePapi21(n):
    if n == 0:
        return 1
    if n == 1:
        return 3

    f0 = 1
    f1 = 3
    i = 2

    while i <= n:
        f2 = 2 * f1 + 2 * f0
        f0 = f1
        f1 = f2
        i = i + 1

    ret = f1
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()
