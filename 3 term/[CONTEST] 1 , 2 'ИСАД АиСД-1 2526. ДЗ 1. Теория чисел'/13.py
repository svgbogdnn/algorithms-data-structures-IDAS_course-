''' .13 Обратное по простому модулю [АиСД] + '''

def longlive21(a):
    return pow(a, 1000000009 - 2, 1000000009)

def solve():
    t = int(input().strip())
    xs = []
    got = 0

    while got < t:
        line = input().strip()
        if not line:
            continue

        for z in line.split():
            xs.append(int(z))
            got += 1
            if got == t:
                break

    for a in xs:
        print(longlive21(a))

if __name__ == '__main__':
    solve()
