'''
https://official.contest.yandex.ru/contest/81973/problems
start 23.09.2025 - finish 7.10.2025 , 20 tasks , 20/20
605 lines
'''

''' .1 ' Минимальный делитель числа + '''

def longlive21(n: int):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
def solve():
    s = input().strip()
    n = int(s)
    print(longlive21(n))
if __name__ == '__main__':
    solve()

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

''' .4 К-е простое число + '''

def longlive21(n):
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    i = 2

    while i * i <= n:
        if a[i]:
            j = i * i
            while j <= n:
                a[j] = False
                j += i
        i += 1

    p = []
    i = 2
    while i <= n:
        if a[i]:
            p.append(i)
        i += 1

    return p

def solve():
    q = int(input().strip())
    ks = []
    t = 0

    while t < q:
        line = input().strip()
        if not line:
            continue

        for z in line.split():
            ks.append(int(z))
            t += 1
            if t == q:
                break

    primes = longlive21(1299709) #10**5 in da task
    ans = [str(primes[k - 1]) for k in ks]
    print(' '.join(ans))
if __name__ == '__main__':
    solve()

''' .5 Решето Эратосфена + '''

def longlive21(n):
    if n < 2:
        return 0
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    p = 2

    while p <= int(n ** 0.5):
        if prime[p]:
            j = p * p
            step = p
            while j <= n:
                prime[j] = False
                j += step
        p += 1

    cnt = 0
    for v in prime:
        if v:
            cnt += 1
    return cnt

def solve():
    s = input().strip()
    x = int(s)
    print(longlive21(x))
if __name__ == '__main__':
    solve()

''' .6 Count The Divisors + '''

def longlive21(l, r):

    if l<2:
        l=2
    if r<2 or l>r:
        return 0
    n = r

    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    p = 2

    while p <= int(n ** 0.5):
        if prime[p]:
            j = p * p
            while j <= n:
                prime[j] = False
                j += p
        p += 1

    cnt = 0
    b = 2

    while b <= r:
        if prime[b]:
            m = ((l + b - 1) // b) * b
            if m <= r:
                cnt += 1
        b += 1

    return cnt

def solve():
    s = input().strip()
    l_str, r_str = s.split()
    l = int(l_str)
    r = int(r_str)
    print(longlive21(l, r))
if __name__ == '__main__':
    solve()

''' .7 GCD + '''

def longlive21(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def solve():
    a = int(input().strip())
    b = int(input().strip())
    print(longlive21(a, b))
if __name__ == '__main__':
    solve()

''' .8 Наименьшее общее кратное [АиСД] + '''

def longlive21(a1, b1):
    a = a1
    b = b1
    while b != 0:
        a, b = b, a % b
    return a1 // a * b1

def solve():
    s = input().split()
    if len(s) == 2:
        A = int(s[0])
        B = int(s[1])
    else:
        A = int(s[0])
        B = int(input().strip())
    print(longlive21(A, B))

if __name__ == '__main__':
    solve()

''' .9 Шестерёнки + '''

def longlive21(n, k):
    a = n
    b = k
    while b != 0:
        r = a % b
        a = b
        b = r
    return n // a * k
def solve():
    s = input().split()
    if len(s) == 1:
        s += input().split()
    n = int(s[0])
    k = int(s[1])
    print(longlive21(n, k))
if __name__ == '__main__':
    solve()

''' .10 Наибольшая правильная несократимая дробь + '''

def longlive21(n):
    a = (n - 1) // 2

    while a >= 1:
        x = a
        y = n
        while y != 0:
            x, y = y, x % y
        if x == 1:
            return a, n - a
        a -= 1

    return 1, n - 1

def solve():
    n = int(input().strip())
    a, b = longlive21(n)
    print(a, b)
if __name__ == '__main__':
    solve()

''' .11 Последняя цифра числа Фибоначчи + '''

def longlive21(n):
    if n <= 1:
        return 1
    a = 1
    b = 1
    i = 2
    while i <= n:
        c = (a + b) % 10
        a = b
        b = c
        i += 1
    return b

def solve():
    s = input().strip()
    n = int(s)
    print(longlive21(n))
if __name__ == '__main__':
    solve()

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

''' .13 Обратное по простому модулю [АиСД] + '''

def longlive21(a):
    return pow(a, 1000000009 - 2, 1000000009)

def solve():
    t = int(input().strip())
    xs = []
    got = 0

    while got < t:
        line = input().strip()
        if not line:
            continue

        for z in line.split():
            xs.append(int(z))
            got += 1
            if got == t:
                break

    for a in xs:
        print(longlive21(a))

if __name__ == '__main__':
    solve()

''' .14 Фибоначчи по модулю [АиСД] + '''

def longlive21(n):
    if n <= 1:
        return 1
    m = 1000003
    a = 1
    b = 1
    i = 2

    while i <= n:
        c = (a + b) % m
        a = b
        b = c
        i += 1

    return b

def solve():
    n = int(input().strip())
    print(longlive21(n))
if __name__ == '__main__':
    solve()

''' .15 Разность квадратов по модулю [АиСД] + '''

def longlive21(a, b):
    m = 1000007
    x = (a - b) % m
    y = (a + b) % m
    ret = (x * y) % m
    return ret

def solve():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    print(longlive21(a, b))
if __name__ == '__main__':
    solve()

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

''' .19 Дружественные числа + '''

def longlive21(m, n):

    if m > n:
        m, n = n, m
    spf = list(range(n + 1))
    i = 2

    while i * i <= n:
        if spf[i] == i:
            j = i * i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1

    out = []
    a = m

    while a <= n:
        y = a
        s = 1
        while y > 1:
            p = spf[y]
            c = 0
            while y % p == 0:
                y //= p
                c += 1
            s *= (p ** (c + 1) - 1) // (p - 1)

        b = s - a
        if b > a and b <= n and b >= m:
            y = b
            s2 = 1
            while y > 1:
                p = spf[y]
                c = 0

                while y % p == 0:
                    y //= p
                    c += 1
                s2 *= (p ** (c + 1) - 1) // (p - 1)
            if s2 - b == a:
                out.append((a, b))
        a += 1

    return out


def solve():
    s = input().split()
    m = int(s[0])
    n = int(s[1])
    ans = longlive21(m, n)

    if not ans:
        print("Absent")
        return
    for a, b in ans:
        print(a, b)

if __name__ == '__main__':
    solve()

''' .20 Последовательность + '''

def longlive21(a1, n):
    a1 = a1 % 10000
    if n == 1:
        return a1

    pos = {}
    seq = []
    x = a1

    while x not in pos:
        pos[x] = len(seq)
        seq.append(x)
        x = (x * x) % 10000

    start = pos[x]
    L = len(seq)
    cyc = L - start
    idx = n - 1

    if idx < L:
        return seq[idx]
    idx = (idx - start) % cyc + start

    ret = seq[idx]
    return ret

def solve():
    s = input().split()
    a1 = int(s[0])
    n = int(s[1])
    print(longlive21(a1, n))
if __name__ == '__main__':
    solve()