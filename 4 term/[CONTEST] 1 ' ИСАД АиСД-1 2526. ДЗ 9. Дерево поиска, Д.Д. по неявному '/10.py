''' .J ' K-й максимум '''
import sys


class champagnepapi:
    __slots__ = ("root", "seed")

    def __init__(self):
        self.root = None
        self.seed = 123456789


class drizzy:
    __slots__ = ("key", "prio", "left", "right", "size")

    def __init__(self, key, prio):
        self.key = key
        self.prio = prio
        self.left = None
        self.right = None
        self.size = 1


def ChampagnePapi21(root, key):
    if root is None:
        return None, None

    if root.key < key:
        left_part, right_part = ChampagnePapi21(root.right, key)
        root.right = left_part
        update_node(root)
        return root, right_part

    left_part, right_part = ChampagnePapi21(root.left, key)
    root.left = right_part
    update_node(root)
    return left_part, root


def longliveDrizzy(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.prio < right.prio:
        left.right = longliveDrizzy(left.right, right)
        update_node(left)
        return left

    right.left = longliveDrizzy(left, right.left)
    update_node(right)
    return right


def SixGodCooking(tree, key):
    left, mid_right = ChampagnePapi21(tree.root, key)
    mid, right = ChampagnePapi21(mid_right, key + 1)

    if mid is None:
        tree.seed = next_seed(tree.seed)
        mid = drizzy(key, tree.seed)

    merged = longliveDrizzy(left, mid)
    tree.root = longliveDrizzy(merged, right)


def node_size(node):
    if node is None:
        return 0
    return node.size


def update_node(node):
    if node is None:
        return
    left_sz = node_size(node.left)
    right_sz = node_size(node.right)
    node.size = left_sz + right_sz + 1


def next_seed(seed):
    seed = seed * 1103515245 + 12345
    seed = seed & 0x7fffffff
    return seed


def delete_key(tree, key):
    left, mid_right = ChampagnePapi21(tree.root, key)
    mid, right = ChampagnePapi21(mid_right, key + 1)
    tree.root = longliveDrizzy(left, right)


def kth_max(root, k):
    cur = root

    while cur is not None:
        right_sz = node_size(cur.right)

        if k <= right_sz:
            cur = cur.right
        elif k == right_sz + 1:
            return cur.key
        else:
            k = k - (right_sz + 1)
            cur = cur.left

    return None


def solve():
    sys.setrecursionlimit(1000000)

    s = input().strip()
    while s == "":
        s = input().strip()

    n = int(s)
    tree = champagnepapi()
    out = []

    i = 0
    while i < n:
        line = input().strip()
        while line == "":
            line = input().strip()

        parts = line.split()
        c = int(parts[0])
        k = int(parts[1])

        if c == 1:
            SixGodCooking(tree, k)
        elif c == -1:
            delete_key(tree, k)
        else:
            ans = kth_max(tree.root, k)
            out.append(str(ans))

        i = i + 1

    print("\n".join(out))


if __name__ == "__main__":
    solve()