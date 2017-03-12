def isLeap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    return False
def getDayOfMonth(year, month):
    if month == 1 or month == 2:
        year -= 1
        month += 12
    k = year % 100
    j = year // 100
    return ((1 + ((13*(month + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7 )
def sundayOnFirstTwo():
    normalMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    res = 0
    y1, m1 , d1 = input().split(' ')
    y1, m1, d1 = [int(y1), int(m1), int(d1)]
    y2, m2 , d2 = input().split(' ')
    y2, m2, d2 = [int(y2), int(m2), int(d2)]
    dayOfTheMonth = getDayOfMonth(y1, m1)
    days = 0
    initMod = 7 - abs(dayOfTheMonth - 1)
    while y1 <= y2:
        while m1 < 12:
            if m1 == 2 and isLeap(y1):
                days = 29
            else:
                days = normalMonths[m1 - 1]
            modValue = days%7
            if modValue == initMod:
                res += 1
            initMod = 7 - abs(modValue - 1)

            m1 += 1
            if y1 == y2 and m1 >= (m2 - 1):
                break
        y1 += 1
    return res


def sundayOnFirst():
    normalMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    res = 0
    y1, m1 , d1 = input().split(' ')
    y1, m1, d1 = [int(y1), int(m1), int(d1)]
    y2, m2 , d2 = input().split(' ')
    y2, m2, d2 = [int(y2), int(m2), int(d2)]
    yearStart = y1
    monthStart = m1 - 1
    days = normalMonths[monthStart]
    monthStart += 1
    dayStart = getDayOfMonth(y1, m1)
    initialMod = 7 - abs(dayStart - 1)
    if dayStart == 1 and d1 == 1:
        res += 1
    while yearStart <= y2:
        # if days %7 == 6:
        #     temp = yearStart - y1
        #     remaining = y2 - yearStart
        #     res += (remaining // temp) * res
        #     yearStart = y2 - (remaining % temp)

        while monthStart < 12:
            if yearStart == y2 and monthStart >= (m2 - 1):
                break

            elif monthStart == 1 and isLeap(yearStart):
                days += 29
            else:
                days += normalMonths[monthStart]
            # if yearStart == y2 and monthStart == (m2 - 1):
            #     days =days - normalMonths[monthStart]
            if res == 0 and days % initialMod == 0:
                days = 0
                res += 1
            elif days%7 == 0:
                days = 0
                res += 1
            monthStart += 1
        if res == 0 and days % initialMod == 1:
            days = 0
            res += 1
        if res == 0 and days !=0 and days % initialMod == 0:
                days = 0
                res += 1
        elif days!=0 and days%7 == 0:
            days = 0
            res += 1
        monthStart = 0
        yearStart += 1
    return res
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        print(sundayOnFirstTwo())
