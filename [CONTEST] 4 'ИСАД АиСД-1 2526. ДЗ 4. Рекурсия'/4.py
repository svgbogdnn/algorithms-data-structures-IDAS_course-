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
