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
