''' .20 Последовательность + '''

def longlive21(a1, n):
    a1 = a1 % 10000
    if n == 1:
        return a1

    pos = {}
    seq = []
    x = a1

    while x not in pos:
        pos[x] = len(seq)
        seq.append(x)
        x = (x * x) % 10000

    start = pos[x]
    L = len(seq)
    cyc = L - start
    idx = n - 1

    if idx < L:
        return seq[idx]
    idx = (idx - start) % cyc + start

    ret = seq[idx]
    return ret

def solve():
    s = input().split()
    a1 = int(s[0])
    n = int(s[1])
    print(longlive21(a1, n))
if __name__ == '__main__':
    solve()
