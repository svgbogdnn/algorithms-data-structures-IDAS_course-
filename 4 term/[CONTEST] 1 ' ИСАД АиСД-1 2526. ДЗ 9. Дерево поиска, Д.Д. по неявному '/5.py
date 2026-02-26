''' E ' Двоичное дерево поиска [АиСД] '''

import sys


class champagnepapi:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        left_h = self._height(node.left)
        right_h = self._height(node.right)

        if left_h > right_h:
            node.height = left_h + 1
        else:
            node.height = right_h + 1

    def _balance_factor(self, node):
        right_h = self._height(node.right)
        left_h = self._height(node.left)
        return right_h - left_h

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rebalance(self, node):
        self._update_height(node)
        bf = self._balance_factor(node)

        if bf == 2:
            child_bf = self._balance_factor(node.right)
            if child_bf < 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        if bf == -2:
            child_bf = self._balance_factor(node.left)
            if child_bf > 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        return node

    def _insert(self, node, key):
        if node is None:
            return self.Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        return self._rebalance(node)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _get_min(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def _remove_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._remove_min(node.left)
        return self._rebalance(node)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
            return self._rebalance(node)

        if key > node.key:
            node.right = self._delete(node.right, key)
            return self._rebalance(node)

        left = node.left
        right = node.right

        if right is None:
            return left

        min_node = self._get_min(right)
        min_node.right = self._remove_min(right)
        min_node.left = left

        return self._rebalance(min_node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def exists(self, key):
        cur = self.root

        while cur is not None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return True

        return False


def ChampagnePapi21(tree, action, value):
    if action == 'insert':
        tree.insert(value)
        return None

    if action == 'delete':
        tree.delete(value)
        return None

    if action == 'exists':
        ok = tree.exists(value)
        if ok:
            return 'true'
        return 'false'

    return None


def solve():
    sys.setrecursionlimit(300000)

    tree = champagnepapi()
    out = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        line = line.strip()
        if line == '':
            continue

        parts = line.split()
        if len(parts) < 2:
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