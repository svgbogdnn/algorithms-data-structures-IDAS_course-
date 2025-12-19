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
