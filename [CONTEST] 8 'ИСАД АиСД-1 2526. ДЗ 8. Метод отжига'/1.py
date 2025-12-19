'''
https://official.contest.yandex.ru/contest/86178/problems/
start 26.11.2025 - finish 08.12.2025 , 5 tasks , 5/5
864 lines
'''

''' .1 ' Куча камней [Отжиг] + ''' #very hard

import sys
import time
import math
import random

def longliveDrizzy(n, w, side, s0, s1, idx):
    wi = w[idx]
    if side[idx] == 0:
        ns0 = s0 - wi
        ns1 = s1 + wi
    else:
        ns0 = s0 + wi
        ns1 = s1 - wi
    ndiff = ns0 - ns1
    if ndiff < 0:
        ndiff = -ndiff
    return ns0, ns1, ndiff

def SixGodCooking(n, w, side, s0, s1, i, j):
    wi = w[i]
    wj = w[j]
    ns0 = s0
    ns1 = s1
    if side[i] == 0:
        ns0 = ns0 - wi
        ns1 = ns1 + wi
    else:
        ns0 = ns0 + wi
        ns1 = ns1 - wi
    if side[j] == 0:
        ns0 = ns0 - wj
        ns1 = ns1 + wj
    else:
        ns0 = ns0 + wj
        ns1 = ns1 - wj
    ndiff = ns0 - ns1
    if ndiff < 0:
        ndiff = -ndiff
    return ns0, ns1, ndiff

def exact_min_diff(weights):
    total = 0
    i = 0
    n = len(weights)
    while i < n:
        total += weights[i]
        i += 1
    dp = 1
    i = 0
    while i < n:
        dp |= dp << weights[i]
        i += 1
    half = total // 2
    s = half
    while s >= 0:
        if (dp >> s) & 1:
            return total - 2 * s
        s -= 1
    return total

def ChampagnePapi21(n, weights):
    pairs = []
    i = 0
    while i < n:
        pairs.append((weights[i], i))
        i = i + 1

    pairs.sort(reverse=True)

    side = [0] * n
    s0 = 0
    s1 = 0
    k = 0
    while k < n:
        w, idx = pairs[k]
        if s0 <= s1:
            side[idx] = 0
            s0 = s0 + w
        else:
            side[idx] = 1
            s1 = s1 + w
        k = k + 1

    diff = s0 - s1
    if diff < 0:
        diff = -diff

    best_side = side[:]
    best_diff = diff
    best_s0 = s0
    best_s1 = s1

    tot = 0
    i = 0
    while i < n:
        tot = tot + weights[i]
        i = i + 1

    seed_val = int(time.time() * 1000003) & 0xFFFFFFFF
    random.seed(seed_val)

    T = float(tot) if tot > 0 else 1.0
    Tend = 1e-4
    alpha = 0.995

    start = time.perf_counter()
    time_limit = 0.2

    inner = 100 + 30 * n

    while T > Tend:
        c = 0
        while c < inner:
            if n >= 2 and random.random() < 0.35:
                i1 = random.randrange(n)
                i2 = random.randrange(n)
                while i2 == i1:
                    i2 = random.randrange(n)
                ns0, ns1, nd = SixGodCooking(n, weights, side, s0, s1, i1, i2)
                delta = nd - diff
                accept = False
                if delta <= 0:
                    accept = True
                else:
                    p = math.exp(-float(delta) / T)
                    if random.random() < p:
                        accept = True
                if accept:
                    if side[i1] == 0:
                        side[i1] = 1
                    else:
                        side[i1] = 0
                    if side[i2] == 0:
                        side[i2] = 1
                    else:
                        side[i2] = 0
                    s0 = ns0
                    s1 = ns1
                    diff = nd
                    if diff < best_diff:
                        best_diff = diff
                        best_side = side[:]
                        best_s0 = s0
                        best_s1 = s1
            else:
                idx = random.randrange(n)
                ns0, ns1, nd = longliveDrizzy(n, weights, side, s0, s1, idx)
                delta = nd - diff
                accept = False
                if delta <= 0:
                    accept = True
                else:
                    p = math.exp(-float(delta) / T)
                    if random.random() < p:
                        accept = True
                if accept:
                    if side[idx] == 0:
                        side[idx] = 1
                    else:
                        side[idx] = 0
                    s0 = ns0
                    s1 = ns1
                    diff = nd
                    if diff < best_diff:
                        best_diff = diff
                        best_side = side[:]
                        best_s0 = s0
                        best_s1 = s1
            c = c + 1

        T = T * alpha
        now = time.perf_counter()
        if now - start > time_limit:
            break

    side = best_side[:]
    s0 = best_s0
    s1 = best_s1
    diff = best_diff

    improved = True
    while improved:
        improved = False
        i = 0
        while i < n:
            ns0, ns1, nd = longliveDrizzy(n, weights, side, s0, s1, i)
            if nd < diff:
                if side[i] == 0:
                    side[i] = 1
                else:
                    side[i] = 0
                s0 = ns0
                s1 = ns1
                diff = nd
                improved = True
            i = i + 1

    sa_result = diff
    exact = exact_min_diff(weights)
    if exact < sa_result:
        return exact
    return sa_result

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    ans = ChampagnePapi21(n, arr)
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()
