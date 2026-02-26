''' .17 Сложить и поделить [АиСД] + '''

def longlive21(a, b, c, d):
    m = 1000000007
    a %= m
    b %= m
    c %= m
    d %= m
    num = ((a * d) + (b * c)) % m
    den = (b * d) % m
    inv = pow(den, m - 2, m)
    ret = (num * inv) % m
    return ret

def solve():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    print(longlive21(a, b, c, d))
if __name__ == '__main__':
    solve()
