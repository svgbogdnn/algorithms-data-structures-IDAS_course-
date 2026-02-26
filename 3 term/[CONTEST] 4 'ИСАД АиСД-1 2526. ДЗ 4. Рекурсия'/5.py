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
