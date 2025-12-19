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
