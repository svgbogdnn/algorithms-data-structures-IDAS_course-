''' .I ' И снова сумма... '''

import sys


class champagnepapi:
    __slots__ = ('key', 'prio', 'left', 'right', 'sum')

    def __init__(self, key, prio):
        self.key = key
        self.prio = prio
        self.left = None
        self.right = None
        self.sum = key


def _subtree_sum(node):
    if node is None:
        return 0
    return node.sum


def _update(node):
    if node is None:
        return
    node.sum = node.key + _subtree_sum(node.left) + _subtree_sum(node.right)


def ChampagnePapi21(root, key):
    if root is None:
        return None, None

    if root.key < key:
        left_part, right_part = ChampagnePapi21(root.right, key)
        root.right = left_part
        _update(root)
        return root, right_part

    left_part, right_part = ChampagnePapi21(root.left, key)
    root.left = right_part
    _update(root)
    return left_part, root


def longliveDrizzy(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.prio < right.prio:
        left.right = longliveDrizzy(left.right, right)
        _update(left)
        return left

    right.left = longliveDrizzy(left, right.left)
    _update(right)
    return right


def SixGodCooking(root, key, prio):
    left, mid = ChampagnePapi21(root, key)
    mid, right = ChampagnePapi21(mid, key + 1)

    if mid is None:
        mid = champagnepapi(key, prio)

    merged = longliveDrizzy(left, mid)
    merged = longliveDrizzy(merged, right)
    return merged


def _range_sum(root, left_key, right_key):
    left, mid = ChampagnePapi21(root, left_key)
    mid, right = ChampagnePapi21(mid, right_key + 1)

    ans = _subtree_sum(mid)

    mid = longliveDrizzy(mid, right)
    root = longliveDrizzy(left, mid)

    return root, ans


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
    out = []
    last = 0
    after_query = False
    seed = 123456789
    mod = 1000000000

    i = 0
    while i < n:
        line = input().strip()
        if line == '':
            continue

        parts = line.split()
        op = parts[0]

        if op == '+':
            x = int(parts[1])
            if after_query:
                x = (x + last) % mod
            seed = _rand(seed)
            root = SixGodCooking(root, x, seed)
            after_query = False
        else:
            l = int(parts[1])
            r = int(parts[2])
            if l > r:
                t = l
                l = r
                r = t
            root, ans = _range_sum(root, l, r)
            out.append(str(ans))
            last = ans
            after_query = True

        i = i + 1

    if out:
        print('\n'.join(out))


if __name__ == '__main__':
    solve()