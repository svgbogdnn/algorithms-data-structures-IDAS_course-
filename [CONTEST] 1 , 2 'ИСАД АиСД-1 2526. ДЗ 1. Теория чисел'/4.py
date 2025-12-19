''' .4 К-е простое число + '''

def longlive21(n):
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    i = 2

    while i * i <= n:
        if a[i]:
            j = i * i
            while j <= n:
                a[j] = False
                j += i
        i += 1

    p = []
    i = 2
    while i <= n:
        if a[i]:
            p.append(i)
        i += 1

    return p

def solve():
    q = int(input().strip())
    ks = []
    t = 0

    while t < q:
        line = input().strip()
        if not line:
            continue

        for z in line.split():
            ks.append(int(z))
            t += 1
            if t == q:
                break

    primes = longlive21(1299709) #10**5 in da task
    ans = [str(primes[k - 1]) for k in ks]
    print(' '.join(ans))
if __name__ == '__main__':
    solve()
