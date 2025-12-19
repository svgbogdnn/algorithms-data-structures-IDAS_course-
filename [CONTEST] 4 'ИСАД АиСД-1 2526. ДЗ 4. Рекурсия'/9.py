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
