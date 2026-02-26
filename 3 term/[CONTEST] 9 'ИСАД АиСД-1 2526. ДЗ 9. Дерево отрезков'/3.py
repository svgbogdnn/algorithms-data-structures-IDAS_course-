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
