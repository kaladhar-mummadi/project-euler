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

def isAbundant(num, sumOfDivisors):
    abundantNumbers = []
    abundantTruthValue = [False]*28123
    global nonAbundantNumbers
    global finalNums
    i = 0
    if num > 28123:
        print("YES")
        return
    while i <= 28123:
        if sumOfDivisors[i] > i:
            abundantTruthValue[i] = True
            abundantNumbers.append(i)
        i += 1
    i = 0
    res = False
    while True:
        if abundantNumbers[i] >= num:
            break
        if abundantTruthValue[num-abundantNumbers[i]]:
            res = True
            break
        i += 1
    if res:
        print("YES")
    else:
        print("NO")
finalNums = []
def sumOfNonAbundant(sumOfDivisors):
    abundantNumbers = []
    num = 28124
    abundantTruthValue = [False]*num
    abundantTruthValue[0] = True
    global finalNums
    i = 0
    while i < num:
        if sumOfDivisors[i] > i:
            abundantTruthValue[i] = True
            abundantNumbers.append(i)
        i += 1

    for number in range(num):
        i = 0
        res = False
        #print(number)
        while True:
            if abundantNumbers[i] >= number:
                break
            if abundantTruthValue[number-abundantNumbers[i]]:
                res = True
                break
            i += 1
        if not res:
            finalNums.append(number)
    print(abundantNumbers)
    print(finalNums)
def hackerrank():
    sumOfDivisors = calcSumOfDivisors(28123)
    T = int(input())
    for _ in range(T):
        N = int(input())
        isAbundant(N, sumOfDivisors)

def projectEuler():
    res = 0
    sumOfDivisors = calcSumOfDivisors(28123)
    sumOfNonAbundant(sumOfDivisors)
    for i in finalNums:
        res += i
    print(res)


if __name__ == '__main__':
    #hackerrank()
    projectEuler()