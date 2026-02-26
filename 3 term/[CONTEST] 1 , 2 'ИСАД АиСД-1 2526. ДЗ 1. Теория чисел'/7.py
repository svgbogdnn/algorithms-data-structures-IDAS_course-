''' .7 GCD + '''

def longlive21(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def solve():
    a = int(input().strip())
    b = int(input().strip())
    print(longlive21(a, b))
if __name__ == '__main__':
    solve()
