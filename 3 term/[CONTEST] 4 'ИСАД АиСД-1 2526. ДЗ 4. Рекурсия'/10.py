''' .10 ' Куча камней + ''' #light hard

def ChampagnePapi21(arr):
    n = len(arr)
    res = []
    mask = 0
    limit = 1 << n
    while mask < limit:
        s = 0
        i = 0
        while i < n:
            if ((mask >> i) & 1) == 1:
                s = s + arr[i]
            i = i + 1
        res.append(s)
        mask = mask + 1
    return res

def longliveDrizzy(w):
    n = len(w)
    mid = n // 2
    left = []
    right = []
    i = 0
    while i < mid:
        left.append(w[i])
        i = i + 1
    while i < n:
        right.append(w[i])
        i = i + 1

    ls = ChampagnePapi21(left)
    rs = ChampagnePapi21(right)

    rs.sort()
    total = 0
    i = 0
    while i < n:
        total = total + w[i]
        i = i + 1

    target2 = total // 2
    best = None

    j = 0
    while j < len(ls):
        need = target2 - ls[j]
        l = 0
        r = len(rs)
        while l < r:
            m = (l + r) // 2
            if rs[m] < need:
                l = m + 1
            else:
                r = m
        cand1 = None
        cand2 = None
        if l < len(rs):
            cand1 = rs[l]
        if l - 1 >= 0:
            cand2 = rs[l - 1]

        if cand1 is not None:
            cur = ls[j] + cand1
            diff = total - 2 * cur
            if diff < 0:
                diff = -diff
            if best is None or diff < best:
                best = diff

        if cand2 is not None:
            cur = ls[j] + cand2
            diff = total - 2 * cur
            if diff < 0:
                diff = -diff
            if best is None or diff < best:
                best = diff

        j = j + 1

    if best is None:
        best = total
    return best

def SixGodCooking():
    s = input().strip()
    n = int(s)
    vals = []
    while len(vals) < n:
        line = input().strip()
        if line == '':
            continue
        parts = line.split()
        i = 0
        while i < len(parts) and len(vals) < n:
            vals.append(int(parts[i]))
            i = i + 1
    ans = longliveDrizzy(vals)
    print(ans)

if __name__ == '__main__':
    SixGodCooking()
