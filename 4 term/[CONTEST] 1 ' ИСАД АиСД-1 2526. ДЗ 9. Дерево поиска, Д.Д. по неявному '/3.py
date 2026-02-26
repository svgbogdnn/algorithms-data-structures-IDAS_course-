''' C ' Проверка свойства дерева поиска [АиСД] '''

def ChampagnePapi21(keys, left, right):
    n = len(keys)
    if n == 0:
        return True

    low_init = -(1 << 63)
    high_init = 1 << 63

    stack = [(0, low_init, high_init)]
    ok = True

    while stack and ok:
        v, low, high = stack.pop()
        key = keys[v]

        if key <= low or key >= high:
            ok = False
            break

        l = left[v]
        r = right[v]

        if r != -1:
            stack.append((r, key, high))
        if l != -1:
            stack.append((l, low, key))

    return ok


def solve():
    read_line = input
    s = read_line().strip()

    if not s:
        return

    n = int(s)
    if n == 0:
        print('CORRECT')
        return

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    i = 0
    while i < n:
        parts = read_line().split()
        keys[i] = int(parts[0])
        left[i] = int(parts[1])
        right[i] = int(parts[2])
        i = i + 1

    ok = ChampagnePapi21(keys, left, right)
    if ok:
        print('CORRECT')
    else:
        print('INCORRECT')


if __name__ == '__main__':
    solve()