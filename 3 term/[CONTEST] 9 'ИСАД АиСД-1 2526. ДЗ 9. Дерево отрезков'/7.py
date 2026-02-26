''' .7 ' Знакочередование + ''' #hard

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
        res = 0
        i = idx
        while i > 0:
            res = res + self.t[i]
            i = i - (i & -i)
        return res

    def sum_range(self, l, r):
        left = self.sum_prefix(l - 1)
        right = self.sum_prefix(r)
        return right - left


def ChampagnePapi21(index, value):
    if (index % 2) == 1:
        return value
    return -value


def longliveDrizzy(bit, arr, index, new_value):
    old_signed = ChampagnePapi21(index, arr[index])
    new_signed = ChampagnePapi21(index, new_value)
    delta = new_signed - old_signed
    arr[index] = new_value
    bit.add(index, delta)


def SixGodCooking(bit, l, r):
    s = bit.sum_range(l, r)
    if (l % 2) == 1:
        return s
    return -s


def read_numbers(need):
    nums = []
    while len(nums) < need:
        line = input().strip()
        if line == "":
            continue
        parts = line.split()
        i = 0
        while i < len(parts) and len(nums) < need:
            nums.append(int(parts[i]))
            i = i + 1
    return nums


def solve():
    s = input().strip()
    while s == "":
        s = input().strip()
    n = int(s)

    values = read_numbers(n)
    arr = [0] * (n + 1)
    bit = champagnepapi(n)

    i = 1
    while i <= n:
        arr[i] = values[i - 1]
        signed = ChampagnePapi21(i, arr[i])
        bit.add(i, signed)
        i = i + 1

    s = input().strip()
    while s == "":
        s = input().strip()
    m = int(s)

    out = []
    q = 0
    while q < m:
        line = input().strip()
        if line == "":
            continue
        parts = line.split()
        typ = int(parts[0])

        if typ == 0:
            idx = int(parts[1])
            val = int(parts[2])
            longliveDrizzy(bit, arr, idx, val)
        else:
            l = int(parts[1])
            r = int(parts[2])
            ans = SixGodCooking(bit, l, r)
            out.append(str(ans))

        q = q + 1

    if len(out) == 0:
        print()
    else:
        print("\n".join(out))


if __name__ == '__main__':
    solve()
