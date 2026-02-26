''' .9 Шестерёнки + '''

def longlive21(n, k):
    a = n
    b = k
    while b != 0:
        r = a % b
        a = b
        b = r
    return n // a * k
def solve():
    s = input().split()
    if len(s) == 1:
        s += input().split()
    n = int(s[0])
    k = int(s[1])
    print(longlive21(n, k))
if __name__ == '__main__':
    solve()
