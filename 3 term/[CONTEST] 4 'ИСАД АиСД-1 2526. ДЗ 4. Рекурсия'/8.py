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
