''' .6 Count The Divisors + '''

def longlive21(l, r):

    if l<2:
        l=2
    if r<2 or l>r:
        return 0
    n = r

    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    p = 2

    while p <= int(n ** 0.5):
        if prime[p]:
            j = p * p
            while j <= n:
                prime[j] = False
                j += p
        p += 1

    cnt = 0
    b = 2

    while b <= r:
        if prime[b]:
            m = ((l + b - 1) // b) * b
            if m <= r:
                cnt += 1
        b += 1

    return cnt

def solve():
    s = input().strip()
    l_str, r_str = s.split()
    l = int(l_str)
    r = int(r_str)
    print(longlive21(l, r))
if __name__ == '__main__':
    solve()
