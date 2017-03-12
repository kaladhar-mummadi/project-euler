def _hack_getTripet(n):
    a = 2
    high = n//2
    b = 0
    c = 0
    result = 0
    while a < high:
        numerator = ((a-n)*(a-n)) - (a*a)
        denominator = 2*(n-a)
        b = numerator // denominator
        c = n - b - a

        sq = a*a + b*b


        if sq == c*c and b > 0 and c > 0:
            temp = a*b*c
            if result < temp:
                result = temp
        a += 1
    if result == 0:
        print("-1")
    else:
        print(result)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T+1):
        N = int(input())
        _hack_getTripet(N)