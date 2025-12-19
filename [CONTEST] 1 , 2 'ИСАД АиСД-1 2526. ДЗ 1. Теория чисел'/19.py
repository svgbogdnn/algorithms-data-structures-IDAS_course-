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
