import math
prime_number_arr = []
def getPrimeNumbers():
    global prime_number_arr
    N = 1000000
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
    while i < N:
        if numbers[i]:
            prime_number_arr.append(i)
        i += 1

def primeFactors(N):
    factors = []
    root = int(math.sqrt(N))
    for i in prime_number_arr:
        mod = N % i
        while mod == 0:
            factors.append(i)
            N = int(N / i)
            mod = N%i
        if i > root:
            if N != 1:
                factors.append(N)
            break
    if len(factors) == 0:
        print(N)
    else:
        print(factors[-1])

if __name__ == '__main__':
    getPrimeNumbers()
    T = int(input())
    for _ in range(T):
        N = int(input())
        primeFactors(N)
