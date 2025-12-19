''' .10 Наибольшая правильная несократимая дробь + '''

def longlive21(n):
    a = (n - 1) // 2

    while a >= 1:
        x = a
        y = n
        while y != 0:
            x, y = y, x % y
        if x == 1:
            return a, n - a
        a -= 1

    return 1, n - 1

def solve():
    n = int(input().strip())
    a, b = longlive21(n)
    print(a, b)
if __name__ == '__main__':
    solve()
