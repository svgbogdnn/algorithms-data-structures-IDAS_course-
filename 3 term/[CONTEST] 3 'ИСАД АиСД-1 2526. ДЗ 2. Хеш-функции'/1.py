'''
https://official.contest.yandex.ru/contest/81974/problems
start 23.09.2025 - finish 12.10.2025 , 9 tasks
2155 lines
'''

''' .1 ' Телефонная книга + '''  # easy

def ChampagnePapi21(n):
    size = 10000000
    book = [None] * size
    out = []
    i = 0

    while i < n:
        parts = input().strip().split()
        cmd = parts[0]

        if cmd == 'add':
            number = int(parts[1])
            name = parts[2]
            book[number] = name

        elif cmd == 'del':
            number = int(parts[1])
            book[number] = None

        else:
            number = int(parts[1])
            name = book[number]
            if name is None:
                out.append('not found')
            else:
                out.append(name)

        i = i + 1

    return out

def solve():
    s = input().strip()
    n = int(s)
    ans = ChampagnePapi21(n)
    i = 0
    m = len(ans)

    while i < m:
        print(ans[i])
        i = i + 1

if __name__ == '__main__':
    solve()
