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
