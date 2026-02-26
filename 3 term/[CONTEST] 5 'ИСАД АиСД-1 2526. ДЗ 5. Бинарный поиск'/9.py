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
