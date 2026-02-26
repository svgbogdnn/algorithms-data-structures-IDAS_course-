''' .B ' Обход двоичного дерева [АиСД] [Сумма] '''

def ChampagnePapi21(keys, left, right):
    n = len(keys)
    sums = [0] * n
    stack = [(0, 0)]

    while stack:
        v, seen = stack.pop()
        if seen == 1:
            total = keys[v]

            l = left[v]
            if l != -1:
                total = total + sums[l]

            r = right[v]
            if r != -1:
                total = total + sums[r]

            sums[v] = total
        else:
            stack.append((v, 1))

            r = right[v]
            if r != -1:
                stack.append((r, 0))

            l = left[v]
            if l != -1:
                stack.append((l, 0))

    return sums


def solve():
    n = int(input())

    keys = [0] * n
    left = [0] * n
    right = [0] * n

    read_line = input
    i = 0
    while i < n:
        parts = read_line().split()
        keys[i] = int(parts[0])
        left[i] = int(parts[1])
        right[i] = int(parts[2])
        i = i + 1

    sums = ChampagnePapi21(keys, left, right)

    out = []
    i = 0
    while i < n:
        out.append(str(sums[i]))
        i = i + 1

    print(" ".join(out))


if __name__ == '__main__':
    solve()