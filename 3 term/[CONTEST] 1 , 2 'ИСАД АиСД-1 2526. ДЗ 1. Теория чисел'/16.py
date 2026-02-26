''' .16 Факториал по модулю [АиСД] + '''

def longlive21(n):
    m = 1000003
    if n >= m:
        return 0
    r = 1
    i = 2

    while i <= n:
        r = (r * i) % m
        i += 1
    return r

def solve():
    n = int(input().strip())
    print(longlive21(n))
if __name__ == '__main__':
    solve()
