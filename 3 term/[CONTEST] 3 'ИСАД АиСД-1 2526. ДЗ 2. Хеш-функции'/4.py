''' .4 ' Дана строка [АиСД] TL14, C++ +'''  # mid

def ChampagnePapi21(t):
    n = len(t)
    z = [0] * n
    l = 0
    r = 0
    i = 1

    while i < n:
        if i <= r:
            k = i - l
            b = r - i + 1
            if z[k] < b:
                z[i] = z[k]
            else:
                z[i] = b
        while i + z[i] < n and t[z[i]] == t[i + z[i]]:
            z[i] = z[i] + 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        i = i + 1

    return z

def longliveDrizzy(a, b):
    if len(b) == 0 or len(a) == 0:
        return []
    if len(b) > len(a):
        return []

    sep = '#'
    t = b + sep + a
    z = ChampagnePapi21(t)
    m = len(b)
    res = []
    i = m + 1

    while i < len(t):
        if z[i] == m:
            pos = i - m - 1
            res.append(pos + 1)
        i = i + 1

    return res

def solve():
    a = input().strip()
    b = input().strip()
    occ = longliveDrizzy(a, b)
    print(len(occ))

    if len(occ) == 0:
        print()
    else:
        pieces = []
        i = 0
        while i < len(occ):
            pieces.append(str(occ[i]))
            i = i + 1
        line = ' '.join(pieces)
        print(line)

if __name__ == '__main__':
    solve()
