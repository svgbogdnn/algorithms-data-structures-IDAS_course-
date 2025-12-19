''' .15 Разность квадратов по модулю [АиСД] + '''

def longlive21(a, b):
    m = 1000007
    x = (a - b) % m
    y = (a + b) % m
    ret = (x * y) % m
    return ret

def solve():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    print(longlive21(a, b))
if __name__ == '__main__':
    solve()
