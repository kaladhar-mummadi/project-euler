def sum(numbers, N):
    result  = []
    extra = 0
    for i in range(49,-1,-1):
        digit = 0
        for j in range(N):
            digit += numbers[j][i]
        digit += extra
        extra = int(digit / 10)
        digit %= 10
        result.append(digit)
    extra = str(extra)[::-1]
    result.append(extra)
    result = ''.join([str(i) for i in result])[::-1]
    return result[0:10]
    #return ''.join([str(i) for i in result[len_result:len_result - 11:-1]])
if __name__ == '__main__':
    N = int(input())
    numbers = []
    for _ in range(N):
        num = [int(x) for x in input()]
        numbers.append(num)
    print(sum(numbers, N))