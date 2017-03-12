def getFactors(n):
    i = 100
    factors = []
    mod = n % i
    while i < 1000:
        div = (n / i ) / 100
        if mod == 0 and (div > 0 and div < 10):
            factors.append(i)
            factors.append(int(n/i))
            break
        i += 1
        mod = n % i
    return factors
def createPalinLessThan(n):
    i = int(n / 1000)

    while i > 100:
        palin = int(str(i) + str(i)[::-1])
        if palin < n:
            factors = getFactors(palin)
            if len(factors) == 2:
                print(palin)
                break
        i -= 1
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        createPalinLessThan(N)