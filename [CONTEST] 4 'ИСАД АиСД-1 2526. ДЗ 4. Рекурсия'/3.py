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
