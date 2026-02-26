''' .4 ' Количество инверсий + ''' #hard

def ChampagnePapi21(n, m, a, b):
    arr = [0] * n
    cur = 0
    mask = 4294967295

    i = 0
    while i < n:
        cur = (cur * a + b) & mask
        arr[i] = (cur >> 8) % m
        i = i + 1

    return arr


def longliveDrizzy(arr):
    n = len(arr)
    if n <= 1:
        return 0

    temp = [0] * n
    inv = 0
    width = 1

    while width < n:
        left = 0
        while left < n:
            mid = left + width
            right = mid + width

            if mid > n:
                mid = n
            if right > n:
                right = n

            if mid >= right:
                i = left
                while i < right:
                    temp[i] = arr[i]
                    i = i + 1
                left = right
                continue

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i = i + 1
                else:
                    temp[k] = arr[j]
                    inv = inv + (mid - i)
                    j = j + 1
                k = k + 1

            while i < mid:
                temp[k] = arr[i]
                i = i + 1
                k = k + 1

            while j < right:
                temp[k] = arr[j]
                j = j + 1
                k = k + 1

            left = right

        tmp = arr
        arr = temp
        temp = tmp

        width = width * 2

    return inv


def SixGodCooking(n, m, a, b):
    arr = ChampagnePapi21(n, m, a, b)
    res = longliveDrizzy(arr)
    return res


def solve():
    first = input().strip()
    while first == "":
        first = input().strip()
    parts = first.split()
    n = int(parts[0])
    m = int(parts[1])

    second = input().strip()
    while second == "":
        second = input().strip()
    parts = second.split()
    a = int(parts[0])
    b = int(parts[1])

    ans = SixGodCooking(n, m, a, b)
    print(ans)


if __name__ == '__main__':
    solve()
