''' .2 ' Хеширование цепочками + '''  # mid

def longliveDrizzy(s, m):
    p = 1000000007 # p=1000000007 — простое число
    x = 263 #a x=263
    power = 1
    h = 0
    i = 0
    n = len(s)

    while i < n:
        code = ord(s[i])
        addv = (code * power) % p
        h = (h + addv) % p
        power = (power * x) % p
        i = i + 1

    idx = h % m
    return idx

def ChampagnePapi21(m, q):
    table = []
    i = 0
    while i < m:
        table.append([])
        i = i + 1
    out = []
    j = 0

    while j < q:
        parts = input().strip().split()
        cmd = parts[0]

        if cmd == 'check':
            idx = int(parts[1])
            chain = table[idx]
            if len(chain) == 0:
                out.append('')
            else:
                pieces = []
                t = 0
                while t < len(chain):
                    pieces.append(chain[t])
                    t = t + 1
                line = ' '.join(pieces)
                out.append(line)

        elif cmd == 'add':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            found = False
            t = 0
            while t < len(chain):
                if chain[t] == s:
                    found = True
                    break
                t = t + 1
            if not found:
                chain.insert(0, s)

        elif cmd == 'del':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            t = 0
            pos = -1
            while t < len(chain):
                if chain[t] == s:
                    pos = t
                    break
                t = t + 1
            if pos != -1:
                chain.pop(pos)

        elif cmd == 'find':
            s = parts[1]
            idx = longliveDrizzy(s, m)
            chain = table[idx]
            t = 0
            found = False
            while t < len(chain):
                if chain[t] == s:
                    found = True
                    break
                t = t + 1
            if found:
                out.append('yes')
            else:
                out.append('no')

        j = j + 1

    return out


def solve():
    s = input().strip()
    m = int(s)
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(m, n)
    i = 0
    k = len(ans)
    while i < k:
        print(ans[i])
        i = i + 1

if __name__ == '__main__':
    solve()
