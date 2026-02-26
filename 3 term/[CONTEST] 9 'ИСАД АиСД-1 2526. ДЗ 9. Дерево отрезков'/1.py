'''
https://official.contest.yandex.ru/contest/87338/problems/
start 16.12.2025 - finish 27.12.2025 , 7 tasks , 7/7
'''

''' .1 ' Суммы на подотрезках с изменением элемента + ''' #mid

class champagnepapi:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, idx, delta):
        i = idx
        while i <= self.n:
            self.t[i] = self.t[i] + delta
            i = i + (i & -i)

    def sum_prefix(self, idx):
        s = 0
        i = idx
        while i > 0:
            s = s + self.t[i]
            i = i - (i & -i)
        return s

    def sum_range(self, l, r):
        left = self.sum_prefix(l - 1)
        right = self.sum_prefix(r)
        res = right - left
        return res


def ChampagnePapi21(n, a):
    bit = champagnepapi(n)
    i = 1
    while i <= n:
        bit.add(i, a[i])
        i = i + 1
    return bit


def longliveDrizzy(bit, a, idx, x):
    old = a[idx]
    a[idx] = x
    delta = x - old
    bit.add(idx, delta)


def SixGodCooking(bit, l, r):
    res = bit.sum_range(l, r)
    return res


def solve():
    s = input().strip()
    while s == "":
        s = input().strip()
    n = int(s)

    values = []
    while len(values) < n:
        parts = input().split()
        j = 0
        while j < len(parts) and len(values) < n:
            values.append(int(parts[j]))
            j = j + 1

    a = [0] * (n + 1)
    i = 1
    while i <= n:
        a[i] = values[i - 1]
        i = i + 1

    s = input().strip()
    while s == "":
        s = input().strip()
    m = int(s)

    bit = ChampagnePapi21(n, a)
    out = []
    q = 0

    while q < m:
        line = input().strip()
        if line == "":
            continue

        parts = line.split()
        cmd = parts[0]

        if cmd == "u":
            idx = int(parts[1])
            x = int(parts[2])
            longliveDrizzy(bit, a, idx, x)
        else:
            l = int(parts[1])
            r = int(parts[2])
            ans = SixGodCooking(bit, l, r)
            out.append(ans)

        q = q + 1

    if len(out) == 0:
        print()
        return

    strs = []
    i = 0
    while i < len(out):
        strs.append(str(out[i]))
        i = i + 1
    print(" ".join(strs))


if __name__ == "__main__":
    solve()
