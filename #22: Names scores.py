def hackerrank():
    N = int(input())
    strArray = []
    for _ in range(N):
        strArray.append(input())
    strArray = sorted(strArray)
    Q = int(input())
    for _ in range(Q):
        query = input()
        position = strArray.index(query) + 1
        i = 0
        res = 0
        base = ord('A') - 1
        while i < len(query):
            res += (ord(query[i]) - base)
            i += 1
        print(position*res)



def projectEuler():
    strArray = input().replace("\"","").split(',')
    strArray = sorted(strArray)
    totalSum = 0
    for j in range(len(strArray)):
        i = 0
        res = 0
        query = strArray[j]
        base = ord('A') - 1
        while i < len(query):
            res += (ord(query[i]) - base)
            i += 1
        totalSum += ((j+1)*res)
    print(totalSum)


if __name__ == '__main__':
    #hackerrank()
    projectEuler()