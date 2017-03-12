prime_number_arr = []

def getPrimeNumbers():
    global prime_number_arr
    N = 110000
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
if __name__ == '__main__':
    getPrimeNumbers()
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(prime_number_arr[N - 1])