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
