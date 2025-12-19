'''
https://official.contest.yandex.ru/contest/83287/problems/
start 31.10.2025 - finish 20.11.2025 , 15 tasks , 15/15
905 lines
'''

''' .1 ' Последняя цифра числа Фибоначчи + ''' #easy

def ChampagnePapi21(n):
    if n <= 1:
        return 1

    a = 1
    b = 1
    i = 2

    while i <= n:
        c = a + b
        c = c % 10
        a = b
        b = c
        i = i + 1

    return b

def solve():
    s = input().strip()
    n = int(s)
    print(ChampagnePapi21(n))

if __name__ == '__main__':
    solve()
