''' .2 ' Простая последовательность + '''  #light mid

def ChampagnePapi21(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    a = [0] * (n + 1)
    a[0] = 1
    a[1] = 1

    i = 2
    while i <= n:
        if i % 2 == 0:
            k = i // 2
            a[i] = a[k] + a[k - 1]
        else:
            k = i // 2
            a[i] = a[k] - a[k - 1]
        i = i + 1

    ret = a[n]
    return ret

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    print(ans)

if __name__ == '__main__':
    solve()
