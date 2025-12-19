''' .5 ' Range Variation Query + ''' #hard

class champagnepapi:
    def __init__(self, values):
        self.n = len(values)
        size = 1
        while size < self.n:
            size = size * 2
        self.size = size

        total = 2 * size
        self.min_tree = [10 ** 18] * total
        self.max_tree = [-(10 ** 18)] * total

        i = 0
        while i < self.n:
            pos = size + i
            val = values[i]
            self.min_tree[pos] = val
            self.max_tree[pos] = val
            i = i + 1

        v = size - 1
        while v >= 1:
            left = v * 2
            right = left + 1

            mn = self.min_tree[left]
            if self.min_tree[right] < mn:
                mn = self.min_tree[right]

            mx = self.max_tree[left]
            if self.max_tree[right] > mx:
                mx = self.max_tree[right]

            self.min_tree[v] = mn
            self.max_tree[v] = mx
            v = v - 1

    def set_value(self, idx, value):
        pos = self.size + idx
        self.min_tree[pos] = value
        self.max_tree[pos] = value

        v = pos // 2
        while v >= 1:
            left = v * 2
            right = left + 1

            mn = self.min_tree[left]
            if self.min_tree[right] < mn:
                mn = self.min_tree[right]

            mx = self.max_tree[left]
            if self.max_tree[right] > mx:
                mx = self.max_tree[right]

            self.min_tree[v] = mn
            self.max_tree[v] = mx

            v = v // 2

    def query_min_max(self, l, r):
        l = l + self.size
        r = r + self.size

        mn = 10 ** 18
        mx = -(10 ** 18)

        while l <= r:
            if (l % 2) == 1:
                if self.min_tree[l] < mn:
                    mn = self.min_tree[l]
                if self.max_tree[l] > mx:
                    mx = self.max_tree[l]
                l = l + 1

            if (r % 2) == 0:
                if self.min_tree[r] < mn:
                    mn = self.min_tree[r]
                if self.max_tree[r] > mx:
                    mx = self.max_tree[r]
                r = r - 1

            l = l // 2
            r = r // 2

        return mn, mx


def ChampagnePapi21(n):
    values = [0] * n
    i = 1
    while i <= n:
        x1 = (i * i) % 12345
        x2 = (i * i * i) % 23456
        val = x1 + x2
        values[i - 1] = val
        i = i + 1
    return values


def longliveDrizzy(values):
    tree = champagnepapi(values)
    return tree


def SixGodCooking(tree, l, r):
    mn, mx = tree.query_min_max(l, r)
    res = mx - mn
    return res


def solve():
    s = input().strip()
    while s == "":
        s = input().strip()
    k = int(s)

    values = ChampagnePapi21(100000)
    tree = longliveDrizzy(values)

    out = []
    i = 0
    while i < k:
        line = input().strip()
        if line == "":
            continue
        parts = line.split()
        x = int(parts[0])
        y = int(parts[1])

        if x > 0:
            ans = SixGodCooking(tree, x - 1, y - 1)
            out.append(str(ans))
        else:
            idx = -x
            tree.set_value(idx - 1, y)

        i = i + 1

    if len(out) == 0:
        print()
        return

    print("\n".join(out))


if __name__ == '__main__':
    solve()
