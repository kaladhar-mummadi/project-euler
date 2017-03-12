def calcSumOfDivisors(maxLimit):
    sumOfDivisors = [1]*(maxLimit+ 1)
    i = 2
    while i <= maxLimit:
        j = i*2
        while j <= maxLimit:
            sumOfDivisors[j] += i
            j += i
        i += 1
    sumOfDivisors[0] = 0
    sumOfDivisors[1] = 0
    return sumOfDivisors
def getAllAmicableNumbers(arr, limit, maxLimit):
    i = 2
    amicableNumbers = []
    while i <= limit:
        if i in amicableNumbers:
            i += 1
            continue
        firstSum = arr[i]
        if firstSum > maxLimit:
            i += 1
            continue
        secondSum = arr[firstSum]
        if i == secondSum and firstSum != secondSum:
            if firstSum <= limit:
                amicableNumbers.append(firstSum)
            if secondSum <= limit:
                amicableNumbers.append(secondSum)
        i += 1
    return amicableNumbers

def getSumOfAmicableNumbers(arr, limit):
    res =0
    i = 2
    for num in arr:
        if num <= limit:
            res += num
    return res
def hackerrank():
    sumOfDivisorsArray = calcSumOfDivisors(100000)
    amicableNumbers = getAllAmicableNumbers(sumOfDivisorsArray, 100000, 100000)
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(getSumOfAmicableNumbers(amicableNumbers, N))


def projectEuler():
    print("")

if __name__ == '__main__':
    hackerrank()
    #projectEuler()