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
