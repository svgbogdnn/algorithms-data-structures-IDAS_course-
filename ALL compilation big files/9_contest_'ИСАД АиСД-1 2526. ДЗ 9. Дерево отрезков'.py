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

''' .2 ' Количество максимумов на отрезке + ''' #hard

def ChampagnePapi21(a_max, a_cnt, b_max, b_cnt):
    if a_max > b_max:
        return a_max, a_cnt
    if b_max > a_max:
        return b_max, b_cnt
    return a_max, a_cnt + b_cnt


def longliveDrizzy(values):
    n = len(values)
    size = 1
    while size < n:
        size = size * 2

    max_tree = [-1] * (2 * size)
    cnt_tree = [0] * (2 * size)

    i = 0
    while i < n:
        pos = size + i
        max_tree[pos] = values[i]
        cnt_tree[pos] = 1
        i = i + 1

    v = size - 1
    while v >= 1:
        left = v * 2
        right = left + 1
        mx, ct = ChampagnePapi21(
            max_tree[left],
            cnt_tree[left],
            max_tree[right],
            cnt_tree[right],
        )
        max_tree[v] = mx
        cnt_tree[v] = ct
        v = v - 1

    return size, max_tree, cnt_tree


def SixGodCooking(l, r, size, max_tree, cnt_tree):
    l = l + size
    r = r + size

    res_max = -1
    res_cnt = 0

    while l <= r:
        if (l % 2) == 1:
            res_max, res_cnt = ChampagnePapi21(
                res_max,
                res_cnt,
                max_tree[l],
                cnt_tree[l],
            )
            l = l + 1

        if (r % 2) == 0:
            res_max, res_cnt = ChampagnePapi21(
                res_max,
                res_cnt,
                max_tree[r],
                cnt_tree[r],
            )
            r = r - 1

        l = l // 2
        r = r // 2

    return res_max, res_cnt


def read_numbers(need):
    nums = []
    while len(nums) < need:
        line = input().strip()
        if not line:
            continue
        parts = line.split()
        i = 0
        while i < len(parts) and len(nums) < need:
            nums.append(int(parts[i]))
            i = i + 1
    return nums


def solve():
    n_line = input().strip()
    while not n_line:
        n_line = input().strip()
    n = int(n_line)

    values = read_numbers(n)
    size, max_tree, cnt_tree = longliveDrizzy(values)

    k_line = input().strip()
    while not k_line:
        k_line = input().strip()
    k = int(k_line)

    out = []
    i = 0
    while i < k:
        parts = input().strip().split()
        if not parts:
            continue
        l = int(parts[0])
        r = int(parts[1])
        mx, ct = SixGodCooking(l - 1, r - 1, size, max_tree, cnt_tree)
        out.append(str(mx) + ' ' + str(ct))
        i = i + 1

    if len(out) == 0:
        print()
    else:
        print('\n'.join(out))


if __name__ == '__main__':
    solve()

''' .3 ' Максимумы на подотрезках + ''' #hard

def ChampagnePapi21(a, b):
    if a > b:
        return a
    return b


def longliveDrizzy(values):
    n = len(values)
    size = 1

    while size < n:
        size = size * 2

    tree = [0] * (2 * size)

    i = 0
    while i < n:
        tree[size + i] = values[i]
        i = i + 1

    v = size - 1
    while v >= 1:
        left = v * 2
        right = left + 1
        tree[v] = ChampagnePapi21(tree[left], tree[right])
        v = v - 1

    return size, tree


def SixGodCooking(l, r, size, tree):
    l = l + size
    r = r + size

    res = 0

    while l <= r:
        if (l % 2) == 1:
            res = ChampagnePapi21(res, tree[l])
            l = l + 1

        if (r % 2) == 0:
            res = ChampagnePapi21(res, tree[r])
            r = r - 1

        l = l // 2
        r = r // 2

    return res


def read_numbers(need):
    nums = []
    while len(nums) < need:
        line = input().strip()
        if not line:
            continue

        parts = line.split()
        i = 0
        while i < len(parts) and len(nums) < need:
            nums.append(int(parts[i]))
            i = i + 1

    return nums


def solve():
    s = input().strip()
    while not s:
        s = input().strip()
    n = int(s)

    values = read_numbers(n)
    size, tree = longliveDrizzy(values)

    s = input().strip()
    while not s:
        s = input().strip()
    k = int(s)

    out = []
    i = 0
    while i < k:
        line = input().strip()
        if not line:
            continue

        parts = line.split()
        l = int(parts[0])
        r = int(parts[1])

        ans = SixGodCooking(l - 1, r - 1, size, tree)
        out.append(str(ans))

        i = i + 1

    print(" ".join(out))


if __name__ == '__main__':
    solve()

''' .4 ' Количество инверсий + ''' #hard

def ChampagnePapi21(n, m, a, b):
    arr = [0] * n
    cur = 0
    mask = 4294967295

    i = 0
    while i < n:
        cur = (cur * a + b) & mask
        arr[i] = (cur >> 8) % m
        i = i + 1

    return arr


def longliveDrizzy(arr):
    n = len(arr)
    if n <= 1:
        return 0

    temp = [0] * n
    inv = 0
    width = 1

    while width < n:
        left = 0
        while left < n:
            mid = left + width
            right = mid + width

            if mid > n:
                mid = n
            if right > n:
                right = n

            if mid >= right:
                i = left
                while i < right:
                    temp[i] = arr[i]
                    i = i + 1
                left = right
                continue

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i = i + 1
                else:
                    temp[k] = arr[j]
                    inv = inv + (mid - i)
                    j = j + 1
                k = k + 1

            while i < mid:
                temp[k] = arr[i]
                i = i + 1
                k = k + 1

            while j < right:
                temp[k] = arr[j]
                j = j + 1
                k = k + 1

            left = right

        tmp = arr
        arr = temp
        temp = tmp

        width = width * 2

    return inv


def SixGodCooking(n, m, a, b):
    arr = ChampagnePapi21(n, m, a, b)
    res = longliveDrizzy(arr)
    return res


def solve():
    first = input().strip()
    while first == "":
        first = input().strip()
    parts = first.split()
    n = int(parts[0])
    m = int(parts[1])

    second = input().strip()
    while second == "":
        second = input().strip()
    parts = second.split()
    a = int(parts[0])
    b = int(parts[1])

    ans = SixGodCooking(n, m, a, b)
    print(ans)


if __name__ == '__main__':
    solve()

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
