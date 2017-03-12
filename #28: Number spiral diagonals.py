mod = 1000000007

def power(x,y,m) :
    if y == 0:
        return 1
    p = power(x,y//2,m)
    p = (p * p) % m
    if y%2 == 0:
        return p
    else:
        return ((x * p) % m)
def modInverse(a , m):
    return power(a, m-2,m)

def getSum(n):
    # (16x3 + 30x2 + 26x + 3)/3
    second_coeff = (n*n) % mod
    first_coeff = (second_coeff * n ) % mod
    sum = (((first_coeff*16) % mod) + ((second_coeff * 30) % mod) + ((26*n) % mod) + 3) % mod
    return (sum * modInverse(3,mod)) % mod


def hackerrank():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(getSum((N-1)//2))


def projectEuler():
    print("")


if __name__ == '__main__':
    hackerrank()
    projectEuler()

