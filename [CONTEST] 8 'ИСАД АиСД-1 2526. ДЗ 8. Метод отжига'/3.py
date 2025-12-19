''' .3 ' Распредели призы + ''' #hard

def ChampagnePapi21(n, k):
    if n % k != 0:
        return None

    m = n // k

    if n == k:
        if n == 1:
            groups = [[]]
            groups[0].append(1)
            return groups
        else:
            return None

    total_sum = n * (n + 1) // 2
    if total_sum % k != 0:
        return None

    groups = []
    i = 0
    while i < k:
        groups.append([])
        i = i + 1

    if m % 2 == 0:
        rows_count = m
        base = 1

        row = 0
        while row < rows_count:
            row_start = base + row * k
            if row % 2 == 0:
                col = 0
                while col < k:
                    value = row_start + col
                    groups[col].append(value)
                    col = col + 1
            else:
                row_end = row_start + k - 1
                col = 0
                while col < k:
                    value = row_end - col
                    groups[col].append(value)
                    col = col + 1
            row = row + 1
    else:
        kk = k
        temp = 3 * kk + 1
        triple_sum = 3 * temp // 2
        half = (kk + 1) // 2
        h = (kk - 1) // 2

        j = 1
        while j <= kk:
            if j <= half:
                a = j
                c3 = 3 * kk - 2 * (j - 1)
                b = triple_sum - a - c3
            else:
                a = j
                b = j + h
                c3 = 4 * kk - 2 * (j - 1)

            idx = j - 1
            groups[idx].append(a)
            groups[idx].append(b)
            groups[idx].append(c3)

            j = j + 1

        base = 3 * kk + 1
        rows_count = m - 3

        row = 0
        while row < rows_count:
            row_start = base + row * kk
            if row % 2 == 0:
                col = 0
                while col < kk:
                    value = row_start + col
                    groups[col].append(value)
                    col = col + 1
            else:
                row_end = row_start + kk - 1
                col = 0
                while col < kk:
                    value = row_end - col
                    groups[col].append(value)
                    col = col + 1
            row = row + 1

    return groups

def solve():
    parts = input().split()
    while len(parts) < 2:
        extra = input().split()
        parts = parts + extra

    n = int(parts[0])
    k = int(parts[1])

    groups = ChampagnePapi21(n, k)

    if groups is None:
        print(0)
    else:
        i = 0
        while i < k:
            g = groups[i]
            line_parts = []
            j = 0
            length = len(g)
            while j < length:
                line_parts.append(str(g[j]))
                j = j + 1
            print(" ".join(line_parts))
            i = i + 1

if __name__ == '__main__':
    solve()
