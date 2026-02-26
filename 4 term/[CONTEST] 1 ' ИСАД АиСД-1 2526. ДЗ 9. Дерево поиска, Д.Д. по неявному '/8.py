#TL10

''' .H ' Следующий '''

import sys


class champagnepapi:
    __slots__ = ('key', 'prio', 'left', 'right')

    def __init__(self, key, prio):
        self.key = key
        self.prio = prio
        self.left = None
        self.right = None


def ChampagnePapi21(root, key):
    if root is None:
        return None, None

    if root.key < key:
        a, b = ChampagnePapi21(root.right, key)
        root.right = a
        return root, b

    a, b = ChampagnePapi21(root.left, key)
    root.left = b
    return a, root


def longliveDrizzy(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.prio < right.prio:
        left.right = longliveDrizzy(left.right, right)
        return left

    right.left = longliveDrizzy(left, right.left)
    return right


def SixGodCooking(root, key, prio):
    left, mid = ChampagnePapi21(root, key)
    mid, right = ChampagnePapi21(mid, key + 1)

    if mid is None:
        node = champagnepapi(key, prio)
        merged = longliveDrizzy(left, node)
        merged = longliveDrizzy(merged, right)
        return merged

    merged = longliveDrizzy(left, mid)
    merged = longliveDrizzy(merged, right)
    return merged


def get_next(root, key):
    cur = root
    ans = None

    while cur is not None:
        if cur.key >= key:
            ans = cur.key
            cur = cur.left
        else:
            cur = cur.right

    return ans


def _rand(seed):
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed


def solve():
    sys.setrecursionlimit(1000000)

    s = input().strip()
    while s == '':
        s = input().strip()

    n = int(s)

    root = None
    seed = 123456789
    last_was_query = False
    last = 0
    out = []

    i = 0
    while i < n:
        parts = input().split()
        op = parts[0]
        x = int(parts[1])

        if op == '+':
            if last_was_query:
                x = (x + last) % 1000000000

            seed = _rand(seed)
            root = SixGodCooking(root, x, seed)
            last_was_query = False
        else:
            ans = get_next(root, x)
            if ans is None:
                out.append('-1')
                last = -1
            else:
                out.append(str(ans))
                last = ans
            last_was_query = True

        i = i + 1

    if out:
        print('\n'.join(out))


if __name__ == '__main__':
    solve()