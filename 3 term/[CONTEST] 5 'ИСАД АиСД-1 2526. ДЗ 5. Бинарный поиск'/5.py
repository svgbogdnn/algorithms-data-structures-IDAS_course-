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
