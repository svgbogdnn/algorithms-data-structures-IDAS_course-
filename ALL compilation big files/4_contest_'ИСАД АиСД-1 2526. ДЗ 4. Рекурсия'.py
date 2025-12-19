'''
https://official.contest.yandex.ru/contest/83285/problems/
start 16.10.2025 - finish 12.11.2025 , 10 tasks , 10/10
403 lines
'''

''' .1 ' Без массивов + ''' #light mid

import sys
sys.setrecursionlimit(1000000)
def ChampagnePapi21(s, i):
    n = len(s)
    if i >= n:
        return i
    if s[i] == ' ':
        j = i + 1
        return ChampagnePapi21(s, j)
    return i

def longliveDrizzy(s, i):
    n = len(s)
    if i >= n:
        return 0, i

    sign = 1
    if s[i] == '-':
        sign = -1
        i = i + 1
    elif s[i] == '+':
        i = i + 1

    def read_digits(s, i, acc):
        n = len(s)
        if i >= n:
            return acc, i
        ch = s[i]
        if ch < '0' or ch > '9':
            return acc, i
        d = ord(ch) - ord('0')
        acc = acc * 10 + d
        j = i + 1
        return read_digits(s, j, acc)

    val, j = read_digits(s, i, 0)
    val = sign * val
    return val, j

def SixGodCooking(s, i, cnt):
    if cnt == 0:
        return i
    i = ChampagnePapi21(s, i)
    val, j = longliveDrizzy(s, i)
    k = SixGodCooking(s, j, cnt - 1)
    print(val, end=' ')
    return k

def solve():
    t = input().strip()
    n = int(t)
    line = input()
    SixGodCooking(line, 0, n)
    print()

if __name__ == '__main__':
    solve()

''' .2 ' Быстрое возведение в степень + ''' #very easy

def ChampagnePapi21(a, n):
    if n == 0:
        return 1.0
    if n < 0:
        val = ChampagnePapi21(a, -n)
        res = 1.0 / val
        return res
    half = ChampagnePapi21(a, n // 2)
    sq = half * half
    if n % 2 == 0:
        return sq
    mul = a * sq
    return mul

def solve():
    parts = input().strip().split()
    if len(parts) == 1:
        a = float(parts[0])
        s = input().strip()
        n = int(s)
    else:
        a = float(parts[0])
        n = int(parts[1])
    ans = ChampagnePapi21(a, n)
    text = '{:.15g}'.format(ans)
    print(text)

if __name__ == '__main__':
    solve()

''' .3 ' Двоичные строки заданной длины в обратном порядке + ''' #very easy

def longliveDrizzy(n, cur, length, res):
    if length == n:
        res.append(cur)
        return
    longliveDrizzy(n, cur + '1', length + 1, res)
    longliveDrizzy(n, cur + '0', length + 1, res)

def ChampagnePapi21(n):
    res = []
    longliveDrizzy(n, '', 0, res)
    return res

def solve():
    s = input().strip()
    n = int(s)
    arr = ChampagnePapi21(n)
    i = 0
    while i < len(arr):
        print(arr[i])
        i = i + 1

if __name__ == '__main__':
    solve()

''' .4 ' Двоичные строки заданной длины + ''' #very easy

def longliveDrizzy(n, cur, length):
    if length == n:
        print(cur)
        return
    longliveDrizzy(n, cur + '0', length + 1)
    longliveDrizzy(n, cur + '1', length + 1)

def ChampagnePapi21(n):
    longliveDrizzy(n, '', 0)

def solve():
    s = input().strip()
    n = int(s)
    ChampagnePapi21(n)

if __name__ == '__main__':
    solve()

''' .5 ' Генератор + ''' #very easy

def longliveDrizzy(n, k, cur, length):
    if length == n:
        line = ''
        i = 0
        while i < n:
            line = line + str(cur[i]) + ' '
            i = i + 1
        print(line)
        return
    v = 1
    while v <= k:
        cur.append(v)
        longliveDrizzy(n, k, cur, length + 1)
        cur.pop()
        v = v + 1

def ChampagnePapi21(n, k):
    cur = []
    longliveDrizzy(n, k, cur, 0)

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    k = int(parts[1])
    ChampagnePapi21(n, k)

if __name__ == '__main__':
    solve()

''' .6 ' Ханойские башни + ''' #very very easy

def ChampagnePapi21(n, a, b, c):
    if n == 0:
        return
    ChampagnePapi21(n - 1, a, c, b)
    print(n, a, c)
    ChampagnePapi21(n - 1, b, a, c)

def solve():
    s = input().strip()
    n = int(s)
    ChampagnePapi21(n, 1, 2, 3)

if __name__ == '__main__':
    solve()

''' .7 ' Фишки + ''' #middle (because of issue w output)

def longliveDrizzy(n, out):
    if n > 0:
        longliveDrizzy(n - 1, out)
        SixGodCooking(n - 2, out)
        out.append(n)
        longliveDrizzy(n - 2, out)

def SixGodCooking(n, out):
    if n > 0:
        SixGodCooking(n - 2, out)
        out.append(-n)
        longliveDrizzy(n - 2, out)
        SixGodCooking(n - 1, out)

def ChampagnePapi21(n):
    out = []
    longliveDrizzy(n, out)
    return out

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)

    if ans:
        print(' '.join(str(v) for v in ans))
    else:
        print()

if __name__ == '__main__':
    solve()

''' .8 ' Разбиение на неубывающие слагаемые, обратный порядок + ''' #easy

import sys
sys.setrecursionlimit(1000000)

def longliveDrizzy(rem, mn, cur):
    if rem == 0:
        i = 0
        line = []
        while i < len(cur):
            line.append(str(cur[i]))
            i = i + 1
        print(' '.join(line))
        return
    v = rem
    if v < mn:
        v = mn
    x = v
    while x >= mn:
        cur.append(x)
        if rem - x >= 0:
            longliveDrizzy(rem - x, x, cur)
        cur.pop()
        x = x - 1

def ChampagnePapi21(n):
    cur = []
    longliveDrizzy(n, 1, cur)

def solve():
    s = input().strip()
    n = int(s)
    ChampagnePapi21(n)

if __name__ == '__main__':
    solve()

''' .9 ' Разбиение на невозрастающие слагаемые, лексикографический порядок + ''' #easy

def longliveDrizzy(rem, maxv, cur):
    if rem == 0:
        pieces = []
        i = 0
        while i < len(cur):
            pieces.append(str(cur[i]))
            i = i + 1
        if len(pieces) == 0:
            print()
        else:
            print(' '.join(pieces))
        return

    limit = maxv
    if rem < limit:
        limit = rem

    x = 1
    while x <= limit:
        cur.append(x)
        longliveDrizzy(rem - x, x, cur)
        cur.pop()
        x = x + 1

def ChampagnePapi21(n):
    cur = []
    longliveDrizzy(n, n, cur)

def solve():
    s = input().strip()
    n = int(s)
    ChampagnePapi21(n)

if __name__ == '__main__':
    solve()

''' .10 ' Куча камней + ''' #light hard

def ChampagnePapi21(arr):
    n = len(arr)
    res = []
    mask = 0
    limit = 1 << n
    while mask < limit:
        s = 0
        i = 0
        while i < n:
            if ((mask >> i) & 1) == 1:
                s = s + arr[i]
            i = i + 1
        res.append(s)
        mask = mask + 1
    return res

def longliveDrizzy(w):
    n = len(w)
    mid = n // 2
    left = []
    right = []
    i = 0
    while i < mid:
        left.append(w[i])
        i = i + 1
    while i < n:
        right.append(w[i])
        i = i + 1

    ls = ChampagnePapi21(left)
    rs = ChampagnePapi21(right)

    rs.sort()
    total = 0
    i = 0
    while i < n:
        total = total + w[i]
        i = i + 1

    target2 = total // 2
    best = None

    j = 0
    while j < len(ls):
        need = target2 - ls[j]
        l = 0
        r = len(rs)
        while l < r:
            m = (l + r) // 2
            if rs[m] < need:
                l = m + 1
            else:
                r = m
        cand1 = None
        cand2 = None
        if l < len(rs):
            cand1 = rs[l]
        if l - 1 >= 0:
            cand2 = rs[l - 1]

        if cand1 is not None:
            cur = ls[j] + cand1
            diff = total - 2 * cur
            if diff < 0:
                diff = -diff
            if best is None or diff < best:
                best = diff

        if cand2 is not None:
            cur = ls[j] + cand2
            diff = total - 2 * cur
            if diff < 0:
                diff = -diff
            if best is None or diff < best:
                best = diff

        j = j + 1

    if best is None:
        best = total
    return best

def SixGodCooking():
    s = input().strip()
    n = int(s)
    vals = []
    while len(vals) < n:
        line = input().strip()
        if line == '':
            continue
        parts = line.split()
        i = 0
        while i < len(parts) and len(vals) < n:
            vals.append(int(parts[i]))
            i = i + 1
    ans = longliveDrizzy(vals)
    print(ans)

if __name__ == '__main__':
    SixGodCooking()