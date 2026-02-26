''' .6 ' Информационный стенд + ''' #hard

class champagnepapi:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width

        size = 1
        while size < rows:
            size = size * 2
        self.size = size

        self.tree = [0] * (2 * size)

        i = 0
        while i < size:
            pos = size + i
            if i < rows:
                self.tree[pos] = width
            else:
                self.tree[pos] = -1
            i = i + 1

        v = size - 1
        while v >= 1:
            left = v * 2
            right = left + 1
            val = self.tree[left]
            if self.tree[right] > val:
                val = self.tree[right]
            self.tree[v] = val
            v = v - 1

    def find_first(self, need):
        if self.tree[1] < need:
            return -1

        v = 1
        while v < self.size:
            left = v * 2
            if self.tree[left] >= need:
                v = left
            else:
                v = left + 1

        return v - self.size + 1

    def decrease(self, idx, delta):
        pos = self.size + (idx - 1)
        self.tree[pos] = self.tree[pos] - delta

        v = pos // 2
        while v >= 1:
            left = v * 2
            right = left + 1
            val = self.tree[left]
            if self.tree[right] > val:
                val = self.tree[right]
            self.tree[v] = val
            v = v // 2


def ChampagnePapi21(h, w, n):
    rows = h
    if n < rows:
        rows = n
    return champagnepapi(rows, w)


def longliveDrizzy(seg, need):
    return seg.find_first(need)


def SixGodCooking(seg, row, need):
    seg.decrease(row, need)


def solve():
    inp = input

    h, w, n = inp().split()
    h = int(h)
    w = int(w)
    n = int(n)

    seg = ChampagnePapi21(h, w, n)

    out = []
    i = 0
    while i < n:
        need = int(inp())
        row = longliveDrizzy(seg, need)
        if row == -1:
            out.append("-1")
        else:
            SixGodCooking(seg, row, need)
            out.append(str(row))
        i = i + 1

    print("\n".join(out))


if __name__ == '__main__':
    solve()
