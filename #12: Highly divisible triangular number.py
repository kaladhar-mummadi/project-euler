"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler012
"""
import math
def sieve(n):
    #n = 50
    arr = [True]*(n + 1)
    res = 0
    p = 2
    while p < math.sqrt(n):
        if arr[p]:
            i = p*2
            while i <= n:
                arr[i] = False
                i += p
        p += 1
    p = 2
    while p <= n:
        if arr[p]:
            res += 1
        p += 1
    return arr
def numberOfFactors(primes, n):
    res = 1
    i = 2
    while  i < 100:
        if i < n:
            temp = 1
            while primes[i] and n%i == 0:
                temp += 1
                n //= i
            res *= temp
            i += 1
        else:
             break
    if n > 2:
        res *= 2
    return res
if __name__ == '__main__':
    T = int(input())
    primes = sieve(100)
    for i in range(T):
        N = int(input())
        i = 1
        sum = 1
        while True:
            factors = numberOfFactors(primes, sum)
            if factors > N:
                print(sum)
                break
            i += 1
            sum += i
