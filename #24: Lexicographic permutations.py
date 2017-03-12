import math

def getPermutation(str, n):
    arr = list(str)
    length = len(str)
    res = []
    i = length
    j = 0
    while n > 1:
        factValue = math.factorial(length-1)
        quo = (n-1) // factValue
        # if quo == 0:
        #     res.append(arr[i - length])
        #     length -= 1
        #     continue
        singleChar = arr[quo]
        res.append(singleChar)
        arr.pop(quo)

        length -= 1
        if quo != 0:
            n -= (quo*factValue)

    for i in arr:
        res.append(i)
    return res

def hackerrank():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print("".join(getPermutation("abcdefghijklm", N)))

def projectEuler():
    print("")

if __name__ == '__main__':
    hackerrank()
    projectEuler()