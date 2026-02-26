''' .14 Фибоначчи по модулю [АиСД] + '''

def longlive21(n):
    if n <= 1:
        return 1
    m = 1000003
    a = 1
    b = 1
    i = 2

    while i <= n:
        c = (a + b) % m
        a = b
        b = c
        i += 1

    return b

def solve():
    n = int(input().strip())
    print(longlive21(n))
if __name__ == '__main__':
    solve()
