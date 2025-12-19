''' .5 ' Треугольник Паскаля + ''' #slightly hard

def ChampagnePapi21(n):
    if n == 0:
        return []

    rows = []
    prev = [1]
    rows.append(prev)

    r = 2
    while r <= n:
        cur = []
        j = 0
        while j < r:
            if j == 0 or j == r - 1:
                val = 1
            else:
                val = prev[j - 1] + prev[j]
            cur.append(val)
            j = j + 1
        rows.append(cur)
        prev = cur
        r = r + 1

    ret = rows
    return ret

def solve():
    s = input().strip()
    n = int(s)
    rows = ChampagnePapi21(n)

    i = 0
    while i < len(rows):
        row = rows[i]
        parts = []
        j = 0
        while j < len(row):
            parts.append(str(row[j]))
            j = j + 1
        print(' '.join(parts))
        i = i + 1

if __name__ == '__main__':
    solve()
