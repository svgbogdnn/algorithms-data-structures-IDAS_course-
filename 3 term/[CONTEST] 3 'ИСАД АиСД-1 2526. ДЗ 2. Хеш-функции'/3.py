''' .3 ' Сравнения подстрок [АиСД] + '''  # mid

def ChampagnePapi21(s):
    n = len(s)
    p1 = 1000000007
    p2 = 1000000009
    x = 263

    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)

    i = 1
    while i <= n:
        c = ord(s[i - 1])
        pref1[i] = (pref1[i - 1] * x + c) % p1
        pref2[i] = (pref2[i - 1] * x + c) % p2
        pow1[i] = (pow1[i - 1] * x) % p1
        pow2[i] = (pow2[i - 1] * x) % p2
        i = i + 1

    state = (pref1, pref2, pow1, pow2, p1, p2)
    return state


def longliveDrizzy(pref, pw, mod, l, r):
    left = l - 1
    right = r
    a = pref[right]
    b = (pref[left] * pw[right - left]) % mod
    val = a - b
    val = val % mod
    return val


def solve():
    s = input().strip()
    state = ChampagnePapi21(s)
    pref1, pref2, pow1, pow2, p1, p2 = state
    line = input().strip()
    m = int(line)

    i = 0
    while i < m:
        parts = input().strip().split()
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
        d = int(parts[3])

        h1 = longliveDrizzy(pref1, pow1, p1, a, b)
        h2 = longliveDrizzy(pref1, pow1, p1, c, d)
        if h1 != h2:
            print('No')
            i = i + 1
            continue

        g1 = longliveDrizzy(pref2, pow2, p2, a, b)
        g2 = longliveDrizzy(pref2, pow2, p2, c, d)
        if g1 != g2:
            print('No')
        else:
            print('Yes')

        i = i + 1

if __name__ == '__main__':
    solve()
