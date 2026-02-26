''' .18 Поделить и сложить [АиСД] + '''

def invm(a, m):
    x0, x1 = 1, 0
    b = m

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1

    ret = x0 % m
    return ret

def longlive21(a, n, m):
    if m == 1:
        return 0
    from math import gcd
    if gcd(a, m) != 1:
        return -1

    r = invm(a % m, m)
    t = r % m
    s = 0
    k = 1

    while k <= n:
        s = (s + (k * t) % m) % m
        t = (t * r) % m
        k += 1

    return s

def solve():
    s = input().split()
    a = int(s[0])
    n = int(s[1])
    m = int(s[2])
    print(longlive21(a, n, m))
if __name__ == '__main__':
    solve()
