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
