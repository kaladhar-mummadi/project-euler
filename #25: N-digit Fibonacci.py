import math
"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler025


http://www.had2know.com/academics/number-digits-length-fibonacci-number.html
"""
# fibs = [[0] , [1]]
# fibsWIthLength = {1 : 0}
def getSUmOfTwoLargeNumbersInArray(arr1, arr2):
    val = []
    i = len(arr1) - 1
    j = len(arr2) - 1
    sum = 0
    k = 0
    while i >=0 and j >= 0:
        sum += arr1[i] + arr2[j]
        if sum < 10:
            val.append(sum)
            k += 1
            sum //= 10
        else:
            val.append(sum % 10)
            k += 1
            sum //= 10
        i -= 1
        j -= 1
    while i>=0:
        sum += arr1[i]
        if sum < 10:
            val.append(sum)
            k += 1
            sum //= 10
        else:
            val.append(sum % 10)
            k += 1
            sum //= 10
        i -= 1
    while j >=0:
        sum += arr2[j]
        if sum < 10:
            val.append(sum)
            k += 1
            sum //= 10
        else:
            val.append(sum % 10)
            k += 1
            sum //= 10
        j -= 1
    while sum != 0:
        val.append(sum%10)
        k += 1
        sum //= 10
    return [val[::-1],k]

# def generateFibSeris():
#
#     k = 2
#     hihgLength = 1
#     firstNum = fibs[0]
#     secondNum = fibs[1]
#     while hihgLength <= 5000:
#         num, numberLength = getSUmOfTwoLargeNumbersInArray(firstNum, secondNum)
#         firstNum = secondNum
#         secondNum = num
#         if numberLength not in fibsWIthLength:
#             fibsWIthLength[numberLength] = k
#         hihgLength = numberLength
#         k += 1
#
#
def hackerrank():
    T = int(input())
    for _ in range(T):
        N = int(input())
        binets(N)
def goldenSection():

    i = 2
    length = 1
    arr = {1:1}
    while length != 5000:
        first = 1 + math.sqrt(5)
        second = 1 - math.sqrt(5)
        val = (pow(first,i) - pow(second,i)) // (pow(2,i) * math.sqrt(5))
        tempLength = math.log10(val)
        if i not in arr:
            arr[tempLength] = i
        i += 1


def binets(N) :
    phi = (1+math.sqrt(5))/2
    print(int(math.ceil((N-1 + math.log10(5)/2) / math.log10(phi))))

def projectEuler():
    print("")

if __name__ == '__main__':
    #generateFibSeris()
    hackerrank()
    #goldenSection()
    projectEuler()