''' .F ' Двоичное дерево поиска 2 [АиСД] '''

import sys


class champagnepapi:
    __slots__ = ('root',)

    def __init__(self):
        self.root = None


class drizzy:
    __slots__ = ('key', 'left', 'right', 'height', 'size')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1


def _height(node):
    if node is None:
        return 0
    return node.height


def _size(node):
    if node is None:
        return 0
    return node.size


def _update(node):
    left_h = _height(node.left)
    right_h = _height(node.right)

    if left_h > right_h:
        node.height = left_h + 1
    else:
        node.height = right_h + 1

    node.size = _size(node.left) + _size(node.right) + 1


def _balance_factor(node):
    return _height(node.right) - _height(node.left)


def _rotate_left(x):
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    _update(x)
    _update(y)

    return y


def _rotate_right(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    _update(y)
    _update(x)

    return x


def _rebalance(node):
    _update(node)
    bf = _balance_factor(node)

    if bf > 1:
        if _balance_factor(node.right) < 0:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)

    if bf < -1:
        if _balance_factor(node.left) > 0:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)

    return node


def _insert(node, key):
    if node is None:
        return drizzy(key)

    if key < node.key:
        node.left = _insert(node.left, key)
    elif key > node.key:
        node.right = _insert(node.right, key)
    else:
        return node

    return _rebalance(node)


def _get_min(node):
    cur = node
    while cur.left is not None:
        cur = cur.left
    return cur


def _remove_min(node):
    if node.left is None:
        return node.right

    node.left = _remove_min(node.left)
    return _rebalance(node)


def _delete(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = _delete(node.left, key)
        return _rebalance(node)

    if key > node.key:
        node.right = _delete(node.right, key)
        return _rebalance(node)

    left = node.left
    right = node.right

    if right is None:
        return left

    min_node = _get_min(right)
    min_node.right = _remove_min(right)
    min_node.left = left
    return _rebalance(min_node)


def _exists(node, key):
    cur = node
    while cur is not None:
        if key < cur.key:
            cur = cur.left
        elif key > cur.key:
            cur = cur.right
        else:
            return True
    return False


def _next(node, key):
    cur = node
    cand = None

    while cur is not None:
        if cur.key > key:
            cand = cur.key
            cur = cur.left
        else:
            cur = cur.right

    return cand


def _prev(node, key):
    cur = node
    cand = None

    while cur is not None:
        if cur.key < key:
            cand = cur.key
            cur = cur.right
        else:
            cur = cur.left

    return cand


def _kth(node, k):
    if node is None:
        return None
    if k <= 0:
        return None
    if k > _size(node):
        return None

    cur = node
    while cur is not None:
        left_sz = _size(cur.left)

        if k == left_sz + 1:
            return cur.key

        if k <= left_sz:
            cur = cur.left
        else:
            k = k - (left_sz + 1)
            cur = cur.right

    return None


def ChampagnePapi21(tree, action, value):
    if action == 'insert':
        tree.root = _insert(tree.root, value)
        return None

    if action == 'delete':
        tree.root = _delete(tree.root, value)
        return None

    if action == 'exists':
        if _exists(tree.root, value):
            return 'true'
        return 'false'

    if action == 'next':
        ans = _next(tree.root, value)
        if ans is None:
            return 'none'
        return str(ans)

    if action == 'prev':
        ans = _prev(tree.root, value)
        if ans is None:
            return 'none'
        return str(ans)

    if action == 'kth':
        ans = _kth(tree.root, value)
        if ans is None:
            return 'none'
        return str(ans)

    return None


def solve():
    sys.setrecursionlimit(300000)

    tree = champagnepapi()
    out = []
    read_line = input

    while True:
        try:
            line = read_line()
        except EOFError:
            break

        parts = line.split()
        if not parts:
            continue

        action = parts[0]
        value = int(parts[1])

        res = ChampagnePapi21(tree, action, value)
        if res is not None:
            out.append(res)

    if out:
        print('\n'.join(out))


if __name__ == '__main__':
    solve()