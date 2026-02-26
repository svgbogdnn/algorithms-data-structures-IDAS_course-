'''
https://official.contest.yandex.ru/contest/83285/problems/
start 16.10.2025 - finish 12.11.2025 , 10 tasks , 10/10
403 lines
'''

''' .1 ' Без массивов + ''' #light mid

import sys
sys.setrecursionlimit(1000000)
def ChampagnePapi21(s, i):
    n = len(s)
    if i >= n:
        return i
    if s[i] == ' ':
        j = i + 1
        return ChampagnePapi21(s, j)
    return i

def longliveDrizzy(s, i):
    n = len(s)
    if i >= n:
        return 0, i

    sign = 1
    if s[i] == '-':
        sign = -1
        i = i + 1
    elif s[i] == '+':
        i = i + 1

    def read_digits(s, i, acc):
        n = len(s)
        if i >= n:
            return acc, i
        ch = s[i]
        if ch < '0' or ch > '9':
            return acc, i
        d = ord(ch) - ord('0')
        acc = acc * 10 + d
        j = i + 1
        return read_digits(s, j, acc)

    val, j = read_digits(s, i, 0)
    val = sign * val
    return val, j

def SixGodCooking(s, i, cnt):
    if cnt == 0:
        return i
    i = ChampagnePapi21(s, i)
    val, j = longliveDrizzy(s, i)
    k = SixGodCooking(s, j, cnt - 1)
    print(val, end=' ')
    return k

def solve():
    t = input().strip()
    n = int(t)
    line = input()
    SixGodCooking(line, 0, n)
    print()

if __name__ == '__main__':
    solve()
