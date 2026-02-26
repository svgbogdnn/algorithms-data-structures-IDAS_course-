'''
https://official.contest.yandex.ru/contest/83286/problems/
start 18.10.2025 - finish 16.11.2025 , 10 tasks , 9/10
522 lines
'''

''' .1 ' Быстрый поиск в массиве + ''' #easy

from bisect import bisect_left, bisect_right
def ChampagnePapi21(a):
    a.sort()
    return a

def longliveDrizzy(a, l, r):
    i1 = bisect_left(a, l)
    i2 = bisect_right(a, r)
    cnt = i2 - i1
    return cnt

def solve():
    s = input().strip()
    n = int(s)
    parts = input().strip().split()
    a = []
    i = 0

    while i < n:
        a.append(int(parts[i]))
        i = i + 1
    a = ChampagnePapi21(a)
    s = input().strip()
    k = int(s)
    out = []
    i = 0

    while i < k:
        lr = input().strip().split()
        l = int(lr[0])
        r = int(lr[1])
        val = longliveDrizzy(a, l, r)
        out.append(str(val))
        i = i + 1

    print(' '.join(out))

if __name__ == '__main__':
    solve()
