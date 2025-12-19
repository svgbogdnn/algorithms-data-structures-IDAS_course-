'''
https://official.contest.yandex.ru/contest/83286/problems/
start 18.10.2025 - finish 16.11.2025 , 10 tasks , 9/10
522 lines
'''

''' .1 ' Быстрый поиск в массиве + ''' #easy

from bisect import bisect_left, bisect_right
def ChampagnePapi21(a):
    a.sort()
    return a

def longliveDrizzy(a, l, r):
    i1 = bisect_left(a, l)
    i2 = bisect_right(a, r)
    cnt = i2 - i1
    return cnt

def solve():
    s = input().strip()
    n = int(s)
    parts = input().strip().split()
    a = []
    i = 0

    while i < n:
        a.append(int(parts[i]))
        i = i + 1
    a = ChampagnePapi21(a)
    s = input().strip()
    k = int(s)
    out = []
    i = 0

    while i < k:
        lr = input().strip().split()
        l = int(lr[0])
        r = int(lr[1])
        val = longliveDrizzy(a, l, r)
        out.append(str(val))
        i = i + 1

    print(' '.join(out))

if __name__ == '__main__':
    solve()

''' .2 ' Корень кубического уравнения + ''' ##middle

def SixGodCooking(a, b, c, d, x):
    val = a * x * x * x + b * x * x + c * x + d
    return val


def longliveDrizzy(a, b, c, d):
    left = -2000.0
    right = 2000.0

    fl = SixGodCooking(a, b, c, d, left)
    fr = SixGodCooking(a, b, c, d, right)

    if fl == 0.0:
        return left
    if fr == 0.0:
        return right

    i = 0
    while fl * fr > 0.0 and i < 60:
        left = left * 2.0
        right = right * 2.0
        fl = SixGodCooking(a, b, c, d, left)
        fr = SixGodCooking(a, b, c, d, right)
        i = i + 1

    j = 0
    while j < 200:
        mid = (left + right) / 2.0
        fm = SixGodCooking(a, b, c, d, mid)

        if fm == 0.0:
            return mid

        if fl * fm < 0.0:
            right = mid
            fr = fm
        else:
            left = mid
            fl = fm

        j = j + 1

    ret = (left + right) / 2.0
    return ret


def ChampagnePapi21(a, b, c, d):
    root = longliveDrizzy(a, b, c, d)
    return root


def solve():
    s = input().strip().split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])

    ans = ChampagnePapi21(a, b, c, d)
    print("{:.10f}".format(ans))


if __name__ == '__main__':
    solve()

''' .3 ' N в степени N + ''' #easy

def ChampagnePapi21(a, n, m):
    if m == 1:
        return 0
    a = a % m
    res = 1 % m
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        n = n // 2
    return res

def solve():
    parts = input().strip().split()
    n = int(parts[0])
    m = int(parts[1])
    ans = ChampagnePapi21(n, n, m)
    print(ans)

if __name__ == '__main__':
    solve()

''' .4 ' Дипломы + ''' #easy

def longliveDrizzy(w, h, side, n):
    a = side // w
    b = side // h
    cnt = a * b
    return cnt >= n

def ChampagnePapi21(w, h, n):
    left = 0
    right = max(w, h) * n
    while left < right:
        mid = (left + right) // 2
        ok = longliveDrizzy(w, h, mid, n)
        if ok:
            right = mid
        else:
            left = mid + 1
    return left

def solve():
    parts = input().strip().split()
    w = int(parts[0])
    h = int(parts[1])
    n = int(parts[2])
    ans = ChampagnePapi21(w, h, n)
    print(ans)

if __name__ == '__main__':
    solve()

''' .5 ' Коровы с характером + ''' #light mid

def longliveDrizzy(pos, k, dist):
    count = 1
    last = pos[0]
    i = 1
    n = len(pos)

    while i < n:
        if pos[i] - last >= dist:
            count = count + 1
            last = pos[i]
            if count >= k:
                return True
        i = i + 1

    return False

def ChampagnePapi21(pos, k):
    left = 0
    right = pos[-1] - pos[0]

    while left < right:
        mid = (left + right + 1) // 2
        ok = longliveDrizzy(pos, k, mid)
        if ok:
            left = mid
        else:
            right = mid - 1

    return left

def solve():
    first = input().strip().split()
    n = int(first[0])
    k = int(first[1])
    parts = input().strip().split()
    pos = []
    i = 0

    while i < n:
        pos.append(int(parts[i]))
        i = i + 1

    ans = ChampagnePapi21(pos, k)
    print(ans)

if __name__ == '__main__':
    solve()

''' .6 ' Вырубка леса +''' #easy

def ChampagnePapi21(a, k, b, m, d):
    x1 = d // k
    x2 = d // m
    w1 = d - x1
    w2 = d - x2
    cut1 = a * w1
    cut2 = b * w2
    total = cut1 + cut2
    return total

def longliveDrizzy(a, k, b, m, x):
    left = 0
    right = 1
    while ChampagnePapi21(a, k, b, m, right) < x:
        right = right * 2

    while left < right:
        mid = (left + right) // 2
        got = ChampagnePapi21(a, k, b, m, mid)
        if got >= x:
            right = mid
        else:
            left = mid + 1

    return left

def solve():
    parts = input().strip().split()
    a = int(parts[0])
    k = int(parts[1])
    b = int(parts[2])
    m = int(parts[3])
    x = int(parts[4])
    ans = longliveDrizzy(a, k, b, m, x)
    print(ans)

if __name__ == '__main__':
    solve()

''' .7 ' Веревочки + ''' #mid

def longliveDrizzy(arr, k, L):
    if L <= 0:
        return False
    total = 0
    i = 0

    while i < len(arr):
        total = total + (arr[i] // L)
        i = i + 1
    return total >= k

def ChampagnePapi21(arr, k):
    left = 0
    right = 0
    i = 0
    while i < len(arr):
        if arr[i] > right:
            right = arr[i]
        i = i + 1

    while left < right:
        mid = (left + right + 1) // 2
        ok = longliveDrizzy(arr, k, mid)
        if ok:
            left = mid
        else:
            right = mid - 1

    return left

def solve():
    first = input().strip().split()
    n = int(first[0])
    k = int(first[1])

    ropes = []
    i = 0
    while i < n:
        s = input().strip()
        val = int(s)
        ropes.append(val)
        i = i + 1

    ans = ChampagnePapi21(ropes, k)
    print(ans)

if __name__ == '__main__':
    solve()


''' .8 ' Безопасная поездка ' WA92 WA90''' #hard

import math
def ChampagnePapi21(a, b, seg_len, v, t0):
    travel = seg_len / v
    t = t0 + travel
    per = a + b

    q = math.floor(t / per)
    r = t - per * q

    wait = 0.0
    if r < a or abs(r - a) <= 1e-12:
        wait = a - r
        if wait < 0.0:
            wait = 0.0

    t_new = t + wait
    return t_new

def longliveDrizzy(T, D, lights, v):
    if v <= 0.0:
        return False

    t = 0.0
    prev = 0.0
    i = 0

    while i < len(lights):
        a, b, p = lights[i]
        t = ChampagnePapi21(a, b, p - prev, v, t)
        prev = p
        i = i + 1

    t = t + (D - prev) / v
    return t <= T + 1e-12

def SixGodCooking(T, D, all_lights):
    lights = []
    i = 0
    while i < len(all_lights):
        a, b, p = all_lights[i]
        if p <= D:
            lights.append((a, b, p))
        i = i + 1

    if len(lights) > 1:
        lights.sort(key=lambda z: z[2])

    hi = 1.0
    i = 0
    while i < 200 and not longliveDrizzy(T, D, lights, hi):
        hi = hi * 2.0
        i = i + 1

    if not longliveDrizzy(T, D, lights, hi):
        return -1.0

    lo = 0.0
    j = 0
    while j < 200:
        mid = (lo + hi) / 2.0
        ok = longliveDrizzy(T, D, lights, mid)
        if ok:
            hi = mid
        else:
            lo = mid
        j = j + 1

    return hi

def solve():
    first = input().strip().split()
    T = float(first[0])
    D = float(first[1])
    N = int(first[2])

    all_lights = []
    i = 0
    while i < N:
        parts = input().strip().split()
        a = float(parts[0])
        b = float(parts[1])
        p = float(parts[2])
        all_lights.append((a, b, p))
        i = i + 1

    ans = SixGodCooking(T, D, all_lights)
    if ans < 0.0:
        print("-1.0")
    else:
        print("{:.15f}".format(ans))

if __name__ == '__main__':
    solve()

''' .9 ' Покрытие K отрезками + ''' #mid

def longliveDrizzy(a, k, L):
    n = len(a)
    i = 0
    used = 0

    while i < n and used < k:
        used = used + 1
        limit = a[i] + L
        i = i + 1
        while i < n and a[i] <= limit:
            i = i + 1

    return i == n

def ChampagnePapi21(points, k):
    points.sort()
    left = 0
    right = points[-1] - points[0]

    while left < right:
        mid = (left + right) // 2
        ok = longliveDrizzy(points, k, mid)
        if ok:
            right = mid
        else:
            left = mid + 1

    return left

def solve():
    first = input().strip().split()
    n = int(first[0])
    k = int(first[1])

    parts = []
    while len(parts) < n:
        parts = parts + input().strip().split()

    pts = []
    i = 0
    while i < n:
        pts.append(int(parts[i]))
        i = i + 1

    ans = ChampagnePapi21(pts, k)
    print(ans)

if __name__ == '__main__':
    solve()

''' .10 ' Железнодорожная задача + ''' #impossible

def query(d):
    print(f"? {d}", flush=True)
    response = input().strip().split()
    return response[0], response[1]


def answer(p):
    print(f"! {p}", flush=True)
    exit(0)


def get_properties(seat):
    level = "low" if seat % 2 == 1 else "high"
    section = "main" if seat <= 36 else "side"
    return level, section


level0, section0 = query(0)

candidates = [p for p in range(1, 55) if get_properties(p) == (level0, section0)]

if len(candidates) == 1:
    answer(candidates[0])

total_offset = 0
queries_used = 1

test_offsets = [18, -18, 9, -9, 4, -4]

for d in test_offsets:
    if len(candidates) == 1 or queries_used >= 6:
        break

    new_candidates = []
    for p in candidates:
        new_pos = p + total_offset + d
        if 1 <= new_pos <= 54:
            new_candidates.append(p)

    if not new_candidates:
        continue

    level_new, section_new = query(d)
    queries_used += 1
    total_offset += d

    filtered = []
    for p in new_candidates:
        expected = get_properties(p + total_offset)
        if expected == (level_new, section_new):
            filtered.append(p)

    if filtered:
        candidates = filtered

    if len(candidates) == 1:
        answer(candidates[0])

answer(candidates[0] if candidates else 1)