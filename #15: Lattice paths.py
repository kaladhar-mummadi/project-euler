MOD = 1000000007
def getFactoWithModOne(n):
    result = 1
    while n!=0 :
        temp = n % 1000000007
        result *= temp
        result %= 1000000007
        n -= 1
    return result
def getFactoWithMod(n,k):
    result = 1
    while n!= k:
        temp = n % 1000000007
        result *= temp
        result %= 1000000007
        n -= 1
    return  result

def pow(a, b):
    x = 1
    y = a
    while b > 0:
        if b%2 == 1:
            x = x*y
            if x > MOD:
                x %= MOD
        y = y*y
        if y > MOD:
            y %= MOD
        b //= 2
    return x
def inverseEuler(n):
    return pow(n, MOD-2)
def c(n,r):
    f = [1]*(n+1)
    i = 2
    while i <= n:
        f[i] = (f[i-1]*i) % MOD
        i += 1
    return (f[n]*(inverseEuler(f[r]) * inverseEuler(f[n-r])) % MOD) % MOD

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = input().split(' ')
        n, m = [int(n), int(m)]
        up = n + m
        down = n if n > m else m
        # numerator = getFactoWithMod(up, down)
        # denominator = getFactoWithModOne(down)
        print(c(up, down))
