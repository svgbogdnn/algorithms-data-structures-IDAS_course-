'''
https://official.contest.yandex.ru/contest/81973/problems
start 23.09.2025 - finish 7.10.2025 , 20 tasks , 20/20
605 lines
'''

''' .1 ' Минимальный делитель числа + '''

def longlive21(n: int):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
def solve():
    s = input().strip()
    n = int(s)
    print(longlive21(n))
if __name__ == '__main__':
    solve()
