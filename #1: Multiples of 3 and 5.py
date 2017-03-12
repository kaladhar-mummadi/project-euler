T = int(input())
def sumDivisibleBy(n ,p) :
    num  = int(p/n)
    sum = num * (num + 1)
    sum = sum >> 1
    return int(n * sum)
for _ in range(T):
    N = int(input())
    result = sumDivisibleBy(3, N - 1) + sumDivisibleBy(5, N - 1) - sumDivisibleBy(15, N - 1)
    print(result)

