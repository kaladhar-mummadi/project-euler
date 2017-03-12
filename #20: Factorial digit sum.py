"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler020

calculate large factorial numbers function
"""
factorials = [[1], [1]]
def multiplyWithArrayInteger(multiple, multiplier):
    i = len(multiple) - 1
    val = []
    k = 0
    product = 0
    while i>=0 :
        product += (multiplier * multiple[i])
        val.append(product%10)
        product //= 10
        i -= 1
    while product !=0 :
        val.append(product%10)
        product //= 10

    return val[::-1]

def getSum(arr):
    res = 0
    for i in arr:
        res += i
    return res

def calcFactorial(maxNum):
    if maxNum == None:
        maxNum = 100
    global factorials
    i = 2
    while i <= maxNum:
        factorials.append(multiplyWithArrayInteger(factorials[i-1], i))
        i += 1


def hackerrank():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(getSum(factorials[n]))


def projectEuler():
    print(getSum(factorials[100]))

if __name__ == '__main__':
    calcFactorial(1000)
    hackerrank()
    #projectEuler()