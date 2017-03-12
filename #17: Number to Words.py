words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion",
    "1000000000000": "Trillion"
}
def insertSpace(prev, extra) :
    if prev == "":
        res = extra
    else:
        res = prev + " " +extra
    return  res
def getWordUpToHundres(num):
    res = ""
    n = int(num)
    if n == 0:
        return words[0]
    i = 10
    quo = n % i
    while quo != n:
        i = i*10
        quo = n % i
    i //= 10
    while i != 0:
        dig = n // i
        if i == 100:
            res = insertSpace(words[dig], words[i])
            # if n % 100 != 0 :
            #     res += "and"  // for euler
        elif n > 9 and n < 20:
            res = insertSpace(res, words[n])
            break
        elif i == 10 and dig!= 0:
            res = insertSpace(res, words[dig*10])
        elif i == 1 and n != 0:
            res = insertSpace(res, words[dig])
        n = n%i
        i //= 10
    return res

def getWord(n):
    res = ""
    length = len(n)
    i = length
    j = 0
    while i > 0:
        if i > 12 and n[j:j + 3] != "000":
            res = insertSpace(res, insertSpace(getWordUpToHundres(n[j:length - 12]), words["1000000000000"]))
        elif i > 9 and n[j:j + 3] != "000":
            res = insertSpace(res, insertSpace(getWordUpToHundres(n[j:length - 9]), words[1000000000]))
        elif i > 6 and n[j:j + 3] != "000":
            res = insertSpace(res, insertSpace(getWordUpToHundres(n[j:length - 6]),  words[1000000]))
        elif i > 3 and n[j:j + 3] != "000":
            res = insertSpace(res, insertSpace(getWordUpToHundres(n[j:length - 3]), words[1000]))
        elif i > 0 and n[j:j + 3] != "000":
            res = insertSpace(res, getWordUpToHundres(n[j:length - 0]))
        temp = i % 3
        temp = 3 if temp == 0 else temp
        i = i - temp
        j = j + temp
    return res


def hackerRank():
    T = int(input())
    for _ in range(T):
        N = input()
        print(getWord(N))
def euler():
    res = ""
    i = 1
    while i < 1001:
        res += getWord(str(i))
        i += 1
    res = res.replace(" ", "")
    print(len(res))

if __name__ == '__main__':
    hackerRank()
    #euler()