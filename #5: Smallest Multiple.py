def gcd(a , b):
    if b == 0:
        return a
    else:
        val = gcd(b , a % b)
        return val
def lcm(a , b):
    if a == 0:
        return b
    lc = (a * b) // gcd(b,a)
    return lcm(a - 1, lc)
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        result = lcm(N - 1, N)
        print(result)
