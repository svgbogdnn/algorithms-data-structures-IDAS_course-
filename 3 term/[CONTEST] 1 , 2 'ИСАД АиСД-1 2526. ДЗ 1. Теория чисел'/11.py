''' .11 Последняя цифра числа Фибоначчи + '''

def longlive21(n):
    if n <= 1:
        return 1
    a = 1
    b = 1
    i = 2
    while i <= n:
        c = (a + b) % 10
        a = b
        b = c
        i += 1
    return b

def solve():
    s = input().strip()
    n = int(s)
    print(longlive21(n))
if __name__ == '__main__':
    solve()
