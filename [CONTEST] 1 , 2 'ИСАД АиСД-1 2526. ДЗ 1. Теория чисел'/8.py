''' .8 Наименьшее общее кратное [АиСД] + '''

def longlive21(a1, b1):
    a = a1
    b = b1
    while b != 0:
        a, b = b, a % b
    return a1 // a * b1

def solve():
    s = input().split()
    if len(s) == 2:
        A = int(s[0])
        B = int(s[1])
    else:
        A = int(s[0])
        B = int(input().strip())
    print(longlive21(A, B))

if __name__ == '__main__':
    solve()
