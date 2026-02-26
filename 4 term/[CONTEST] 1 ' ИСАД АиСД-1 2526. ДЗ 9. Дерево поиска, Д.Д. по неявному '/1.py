''' .A ' Обход двоичного дерева [АиСД] '''

def ChampagnePapi21(keys, left, right):
    res = []
    stack = []
    cur = 0

    while cur != -1 or stack:
        if cur != -1:
            stack.append(cur)
            cur = left[cur]
        else:
            cur = stack.pop()
            res.append(keys[cur])
            cur = right[cur]

    return res


def longliveDrizzy(keys, left, right):
    res = []
    stack = [0]

    while stack:
        v = stack.pop()
        res.append(keys[v])

        r = right[v]
        if r != -1:
            stack.append(r)

        l = left[v]
        if l != -1:
            stack.append(l)

    return res


def SixGodCooking(keys, left, right):
    res = []
    stack = [(0, 0)]

    while stack:
        v, seen = stack.pop()
        if seen == 1:
            res.append(keys[v])
        else:
            stack.append((v, 1))

            r = right[v]
            if r != -1:
                stack.append((r, 0))

            l = left[v]
            if l != -1:
                stack.append((l, 0))

    return res


def solve():
    first = input().strip()
    while first == "":
        first = input().strip()
    n = int(first)

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    i = 0
    while i < n:
        parts = input().strip().split()
        while len(parts) < 3:
            extra = input().strip().split()
            j = 0
            while j < len(extra):
                parts.append(extra[j])
                j = j + 1

        keys[i] = int(parts[0])
        left[i] = int(parts[1])
        right[i] = int(parts[2])

        i = i + 1

    inorder = ChampagnePapi21(keys, left, right)
    preorder = longliveDrizzy(keys, left, right)
    postorder = SixGodCooking(keys, left, right)

    out1 = []
    i = 0
    while i < len(inorder):
        out1.append(str(inorder[i]))
        i = i + 1
    print(" ".join(out1))

    out2 = []
    i = 0
    while i < len(preorder):
        out2.append(str(preorder[i]))
        i = i + 1
    print(" ".join(out2))

    out3 = []
    i = 0
    while i < len(postorder):
        out3.append(str(postorder[i]))
        i = i + 1
    print(" ".join(out3))


if __name__ == '__main__':
    solve()