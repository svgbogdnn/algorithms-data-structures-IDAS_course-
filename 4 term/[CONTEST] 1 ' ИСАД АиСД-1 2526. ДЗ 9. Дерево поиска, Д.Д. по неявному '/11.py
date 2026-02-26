''' .K* ' Строим дерамиду ' '''


def ChampagnePapi21(a, b):
    n = len(a)

    order = []
    i = 0
    while i < n:
        order.append(i)
        i = i + 1

    order.sort(key=lambda j: a[j])

    parent = [-1] * n
    left = [-1] * n
    right = [-1] * n

    stack = []

    i = 0
    while i < n:
        v = order[i]
        last = -1

        while stack and b[stack[-1]] > b[v]:
            last = stack.pop()

        if stack:
            p = stack[-1]
            parent[v] = p
            right[p] = v

        if last != -1:
            parent[last] = v
            left[v] = last

        stack.append(v)
        i = i + 1

    return parent, left, right


def solve():
    line = input().strip()
    while line == "":
        line = input().strip()

    n = int(line)
    a = [0] * n
    b = [0] * n

    i = 0
    while i < n:
        parts = input().split()
        if not parts:
            continue
        a[i] = int(parts[0])
        b[i] = int(parts[1])
        i = i + 1

    parent, left, right = ChampagnePapi21(a, b)

    print("YES")

    i = 0
    while i < n:
        p = parent[i]
        l = left[i]
        r = right[i]

        if p == -1:
            p_out = 0
        else:
            p_out = p + 1

        if l == -1:
            l_out = 0
        else:
            l_out = l + 1

        if r == -1:
            r_out = 0
        else:
            r_out = r + 1

        print(str(p_out) + " " + str(l_out) + " " + str(r_out))
        i = i + 1


if __name__ == "__main__":
    solve()