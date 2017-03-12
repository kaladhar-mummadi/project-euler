prime_number_arr = []
sum_arr = [0] * 2000001
def getPrimeNumbers():
    global prime_number_arr
    global sum_arr
    N = 2000001
    numbers = [True] * N
    i = 2
    while i*i <= N:
        if numbers[i]:
            j = i * 2
            while j < N:
                numbers[j] = False
                j += i
        i += 1
    i = 2
    prev = 0
    j = 0
    while i < N:
        if numbers[i]:
            prime_number_arr.append(i)
            while j < i:
                sum_arr[j] = prev
                j += 1
            prev = prev + i
            sum_arr[j] = prev
        i += 1
    while j < N:
        sum_arr[j] = prev
        j += 1
def getSum(n):
    result = 0
    result = sum_arr[n]
    print(result)
if __name__ == '__main__':
    getPrimeNumbers()
    T = int(input())
    for _ in range(T):
        N = int(input())
        getSum(N)