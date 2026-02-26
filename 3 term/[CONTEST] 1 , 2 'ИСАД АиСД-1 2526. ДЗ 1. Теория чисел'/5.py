''' .5 Решето Эратосфена + '''

def longlive21(n):
    if n < 2:
        return 0
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    p = 2

    while p <= int(n ** 0.5):
        if prime[p]:
            j = p * p
            step = p
            while j <= n:
                prime[j] = False
                j += step
        p += 1

    cnt = 0
    for v in prime:
        if v:
            cnt += 1
    return cnt

def solve():
    s = input().strip()
    x = int(s)
    print(longlive21(x))
if __name__ == '__main__':
    solve()
