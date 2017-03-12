import math
def sieve(n):
    arr = [True]*(n + 1)
    res = []
    p = 2
    arr[0]= False
    arr[1] = False
    while p < math.sqrt(n):
        if arr[p]:
            i = p*2
            while i <= n:
                arr[i] = False
                i += p
        p += 1
    p = 2
    while p <= n:
        if arr[p]:
            res.append(p)
        p += 1
    return res
def getRecurringLength(primes):
    res = [0]*10001
    res[3] = 2
    for denominator in primes:
        if res[denominator] != 0 :
            continue
        repeatedNumbers = []
        checkAlreadyCalculated = [False] * 100000
        quotient = 1
        numerator = quotient * 10
        repeatedLength = 0
        while checkAlreadyCalculated[numerator] == False:
            remainder = numerator % denominator
            repeatedNumbers.append(numerator)
            checkAlreadyCalculated[numerator] = True
            repeatedLength += 1
            if remainder == 0:
                numerator = repeatedNumbers[0]
                break
            numerator = remainder * 10
        firstIndex = repeatedNumbers.index(numerator)
        length = repeatedLength - firstIndex
        res[denominator] = length
    return res
def getMaxBeforeThisNum(arr, N):
    max = 0
    res = 0
    i = 0
    while i < N:
        if max < arr[i]:
            max = arr[i]
            res = i
        i += 1
    return res
def hackerrank():
    primes = sieve(10000)
    arrayOfLengths = getRecurringLength(primes)
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(getMaxBeforeThisNum(arrayOfLengths, N))

def projectEuler():
    print("")

if __name__ == '__main__':
    hackerrank()
    #projectEuler()